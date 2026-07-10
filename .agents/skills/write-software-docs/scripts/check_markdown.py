#!/usr/bin/env python3
"""Check Markdown structure and flag likely documentation-quality problems."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


MARKDOWN_EXTENSIONS = {".md", ".mdx"}
FENCE_RE = re.compile(r"^(?:\s*>\s*)*\s*(`{3,}|~{3,})(.*)$")
HEADING_RE = re.compile(r"^(#{1,6})\s+\S")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(r"\b(?:TODO|FIXME|XXX)\b", re.IGNORECASE)
SCHEME_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
URL_RE = re.compile(r"https?://\S+")

BRITISH_FORMS = {
    "analyse": "analyze",
    "analysed": "analyzed",
    "artefact": "artifact",
    "artefacts": "artifacts",
    "authorisation": "authorization",
    "authorise": "authorize",
    "authorised": "authorized",
    "behaviour": "behavior",
    "behaviours": "behaviors",
    "cancelled": "canceled",
    "cancelling": "canceling",
    "catalogue": "catalog",
    "catalogued": "cataloged",
    "centre": "center",
    "centres": "centers",
    "colour": "color",
    "colours": "colors",
    "customise": "customize",
    "customised": "customized",
    "customisation": "customization",
    "defence": "defense",
    "enrol": "enroll",
    "enrolment": "enrollment",
    "favour": "favor",
    "favoured": "favored",
    "favourite": "favorite",
    "favourites": "favorites",
    "focussed": "focused",
    "focussing": "focusing",
    "fulfil": "fulfill",
    "fulfilment": "fulfillment",
    "grey": "gray",
    "humour": "humor",
    "initialise": "initialize",
    "initialised": "initialized",
    "labelled": "labeled",
    "labour": "labor",
    "learnt": "learned",
    "licence": "license",
    "localise": "localize",
    "localised": "localized",
    "modelling": "modeling",
    "neighbour": "neighbor",
    "neighbours": "neighbors",
    "normalise": "normalize",
    "normalised": "normalized",
    "offence": "offense",
    "optimise": "optimize",
    "optimised": "optimized",
    "optimisation": "optimization",
    "organisation": "organization",
    "organise": "organize",
    "organised": "organized",
    "practise": "practice",
    "programme": "program",
    "realise": "realize",
    "realised": "realized",
    "recognise": "recognize",
    "recognised": "recognized",
    "serialise": "serialize",
    "serialised": "serialized",
    "signalled": "signaled",
    "signalling": "signaling",
    "specialise": "specialize",
    "specialised": "specialized",
    "spelt": "spelled",
    "standardise": "standardize",
    "standardised": "standardized",
    "summarise": "summarize",
    "summarised": "summarized",
    "travelling": "traveling",
    "traveller": "traveler",
    "utilise": "utilize",
    "utilised": "utilized",
    "visualise": "visualize",
    "visualised": "visualized",
    "visualisation": "visualization",
    "whilst": "while",
}

BRITISH_RE = re.compile(
    r"\b(" + "|".join(re.escape(british) for british in BRITISH_FORMS) + r")\b",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    severity: str
    message: str


def collect_markdown_paths(raw_paths: list[str]) -> tuple[list[Path], list[str]]:
    paths: set[Path] = set()
    errors: list[str] = []

    for raw_path in raw_paths:
        path = Path(raw_path)
        if not path.exists():
            errors.append(f"{path}: path does not exist")
            continue
        if path.is_dir():
            paths.update(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file()
                and candidate.suffix.lower() in MARKDOWN_EXTENSIONS
            )
        elif path.suffix.lower() in MARKDOWN_EXTENSIONS:
            paths.add(path)
        else:
            errors.append(f"{path}: expected a Markdown or MDX file")

    return sorted(paths), errors


def strip_link_destination(raw_destination: str) -> str:
    destination = raw_destination.strip()
    if not destination:
        return ""
    if destination.startswith("<") and ">" in destination:
        destination = destination[1 : destination.index(">")]
    else:
        destination = destination.split(maxsplit=1)[0]
    return unquote(destination)


def check_local_link(path: Path, line: int, raw_destination: str) -> Finding | None:
    destination = strip_link_destination(raw_destination)
    if (
        not destination
        or destination.startswith("#")
        or destination.startswith("/")
        or SCHEME_RE.match(destination)
        or destination.startswith("{")
    ):
        return None

    target_text = destination.split("#", 1)[0].split("?", 1)[0]
    if not target_text:
        return None

    target = path.parent / target_text
    if target.exists():
        return None

    return Finding(
        path,
        line,
        "warning",
        f"relative link target does not exist: {target_text}",
    )


def inspect_markdown(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return [Finding(path, 1, "error", "file is not valid UTF-8")]
    except OSError as exc:
        return [Finding(path, 1, "error", f"cannot read file: {exc}")]

    in_frontmatter = bool(lines and lines[0].strip() == "---")
    in_fence = False
    fence_character = ""
    fence_length = 0
    fence_start = 0
    previous_heading_level = 0
    h1_count = 0

    for line_number, line in enumerate(lines, start=1):
        if in_frontmatter:
            if line_number > 1 and line.strip() == "---":
                in_frontmatter = False
            continue

        fence_match = FENCE_RE.match(line)
        if in_fence:
            if fence_match:
                marker = fence_match.group(1)
                suffix = fence_match.group(2).strip()
                if (
                    marker[0] == fence_character
                    and len(marker) >= fence_length
                    and not suffix
                ):
                    in_fence = False
            continue

        if fence_match:
            marker = fence_match.group(1)
            info_string = fence_match.group(2).strip()
            in_fence = True
            fence_character = marker[0]
            fence_length = len(marker)
            fence_start = line_number
            if not info_string:
                findings.append(
                    Finding(
                        path,
                        line_number,
                        "warning",
                        "fenced code block has no language identifier",
                    )
                )
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            level = len(heading_match.group(1))
            if level == 1:
                h1_count += 1
                if h1_count > 1:
                    findings.append(
                        Finding(
                            path,
                            line_number,
                            "error",
                            "page contains more than one level-one heading",
                        )
                    )
            if previous_heading_level and level > previous_heading_level + 1:
                findings.append(
                    Finding(
                        path,
                        line_number,
                        "error",
                        f"heading level skips from h{previous_heading_level} to h{level}",
                    )
                )
            previous_heading_level = level

        prose = INLINE_CODE_RE.sub("", line)
        prose = URL_RE.sub("", prose)

        if PLACEHOLDER_RE.search(prose):
            findings.append(
                Finding(
                    path,
                    line_number,
                    "warning",
                    "possible unresolved placeholder",
                )
            )

        for spelling_match in BRITISH_RE.finditer(prose):
            british = spelling_match.group(1)
            american = BRITISH_FORMS[british.lower()]
            findings.append(
                Finding(
                    path,
                    line_number,
                    "warning",
                    f"possible British spelling '{british}'; prefer '{american}'",
                )
            )

        for link_match in LINK_RE.finditer(line):
            finding = check_local_link(path, line_number, link_match.group(1))
            if finding:
                findings.append(finding)

    if in_frontmatter:
        findings.append(
            Finding(path, 1, "error", "YAML frontmatter is not closed")
        )
    if in_fence:
        findings.append(
            Finding(path, fence_start, "error", "fenced code block is not closed")
        )

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check Markdown or MDX files for structural errors, unresolved "
            "placeholders, likely British spellings, and broken relative links."
        )
    )
    parser.add_argument("paths", nargs="+", help="Files or directories to check")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a nonzero status for warnings as well as errors",
    )
    args = parser.parse_args()

    paths, path_errors = collect_markdown_paths(args.paths)
    if path_errors:
        for error in path_errors:
            print(f"error: {error}")
        return 2
    if not paths:
        print("error: no Markdown or MDX files found")
        return 2

    findings = [
        finding
        for path in paths
        for finding in inspect_markdown(path)
    ]

    for finding in findings:
        print(
            f"{finding.path}:{finding.line}: "
            f"{finding.severity}: {finding.message}"
        )

    error_count = sum(finding.severity == "error" for finding in findings)
    warning_count = sum(finding.severity == "warning" for finding in findings)
    print(
        f"Checked {len(paths)} file(s): "
        f"{error_count} error(s), {warning_count} warning(s)"
    )

    if error_count or (args.strict and warning_count):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
