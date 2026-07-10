# Review documentation quality

Use this rubric for substantial pages, multi-page changes, documentation
audits, and forward tests. Score the artifact, not the author's effort.

## Apply critical quality gates

Treat any of these as a failed review regardless of the numerical score:

- An invented or version-incorrect flag, endpoint, field, default, limit,
  response, compatibility claim, or error.
- A destructive, security-sensitive, or costly action without a timely
  warning.
- A supposedly runnable example that cannot perform or expose the claimed
  result.
- Reader-facing internal metadata, evaluation notes, hidden modes, or working
  terminology dictionaries.
- An unresolved placeholder in an artifact presented as finished.
- A rewrite that damages generated regions, contracts, required frontmatter,
  or established links without explicit justification.
- Non-American prose spelling when the user has not requested another locale.

## Score the artifact

### Factual support and version fidelity — 30 points

- Support every product claim with appropriate evidence.
- Match commands, defaults, output, limitations, and compatibility to the
  stated version.
- Distinguish captured behavior from illustrative examples.
- State material uncertainty without turning it into a promise.

### Reader outcome and time to first success — 20 points

- Identify the reader and job accurately.
- Put the first useful answer or action early.
- Place prerequisites and consequential warnings before the affected action.
- End task flows with an observable verification.

### Examples and troubleshooting — 15 points

- Make executable examples complete, minimal, and copyable.
- Make claimed results observable through the shown command or interface.
- Use realistic troubleshooting entries with testable causes and recovery.
- Omit examples and troubleshooting when the subject does not support them.

### Information architecture and scanning — 15 points

- Use only sections that serve the page purpose.
- Make headings form a clear outline.
- Use numbered lists, bullets, tables, and prose according to their meaning.
- Keep reference information easy to locate.

### Repository conventions and accessibility — 10 points

- Preserve Markdown or MDX conventions, frontmatter, components, generated
  regions, terminology, and useful anchors.
- Use correct heading hierarchy, descriptive links, code-fence languages, and
  meaningful text alternatives for images.
- Avoid tables or visual-only instructions that impede narrow screens or
  assistive technology.

### Voice, clarity, and locale — 10 points

- Use direct, specific, humane prose.
- Vary sentence length without becoming verbose or choppy.
- Remove marketing language, dismissive wording, and reader-directed jokes.
- Use American English outside exact product text unless the user requests
  another locale.

Use 85 points as a practical passing target, provided every critical gate
passes.

## Forward-test the skill

Give a fresh agent the skill and a realistic task. Do not reveal the suspected
failure or desired answer. Test at least these cases after a substantial
revision:

1. **Mixed README:** Supply install, first-run, configuration, security, and
   reference facts. Check that the page reaches a verified result early
   without internal modes or bloated templates.
2. **Existing MDX edit:** Supply a page with frontmatter, components,
   generated markers, and stable links. Check preservation and edit scope.
3. **HTTP reference:** Supply exact request, response, limits, and errors.
   Check that the verification command exposes the claimed status and body.
4. **Non-executable policy or concept:** State explicitly that no commands or
   parameters exist. Check that the page uses natural noun headings and does
   not apologize for missing examples.
5. **Incomplete evidence:** Omit a tempting default or error detail. Check
   that the output neither invents it nor leaves an accidental placeholder.

Include at least one task that contains American spellings such as `behavior`
and verify that the output preserves the requested locale.

Compare artifacts with this rubric. Revise the skill only for failures that
generalize beyond one fixture.
