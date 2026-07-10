---
name: write-software-docs
description: >-
  Create, rewrite, or review clear, source-backed software documentation,
  including READMEs, quickstarts, tutorials, how-to guides, manuals,
  troubleshooting pages, and CLI, API, configuration, or library references.
  Use for Markdown or MDX documentation that should lead readers to an early
  working result, preserve repository conventions, explain behavior plainly,
  and include verified examples when the subject supports them.
---

# Write practical software documentation

## Aim for a working result

Get the reader from intent to a verified result quickly. Then provide enough
detail to repeat, adapt, and troubleshoot the task.

Be concise, practical, and companionable. Be slightly amused by the machine,
never by the reader. Borrow the teaching strengths of hands-on computer
manuals without copying their prose, dated assumptions, or jokes.

## Follow the evidence

Use this order of precedence:

1. Follow the user's request and supplied facts.
2. Treat current implementation, public schemas, tests, command help, and
   version metadata as the strongest product evidence.
3. Preserve repository documentation conventions, fixed product terms,
   frontmatter, MDX components, generated regions, and stable anchors.
4. Apply this skill's defaults where the project is silent.

When sources conflict, identify the conflict. Do not quietly choose the most
convenient claim.

Use American English for all prose unless the user explicitly requests another
locale. Use forms such as `behavior`, `color`, `humor`, `organize`,
`analyze`, `center`, `license`, `canceled`, and `traveling`. Preserve exact
spelling in code, commands, identifiers, UI labels, product names, and direct
quotations.

## Work evidence first

1. **Inspect the context.**
   - Read the target page and nearby documentation.
   - Read repository instructions and style guidance.
   - Inspect the sources that define the documented behavior: command
     definitions, `--help` output, API specifications, public types,
     configuration loading, tests, and supported-version metadata.
2. **Identify the reader and purpose.**
   - Decide whether each section teaches, guides a task, explains a concept,
     provides lookup information, or resolves a failure.
   - Treat this classification as planning data. Never print a mode marker,
     checklist, or hidden style dictionary in the finished document.
3. **Separate facts from gaps.**
   - Record the supported version and the evidence for commands, defaults,
     paths, outputs, limits, compatibility, and failure behavior.
   - Do not turn an inference into a product promise.
4. **Plan the shortest useful path.**
   - Put prerequisites and consequential warnings before the action they
     affect.
   - Put the primary path first. Move alternatives and background later.
   - Include only sections that help this reader complete or understand the
     stated job.
5. **Draft action, result, and reason.**
   - Tell the reader what to do.
   - Show the observable result.
   - Explain why it happened when that explanation helps the next decision.
6. **Verify before delivery.**
   - Run safe examples when the environment permits.
   - Confirm that the shown command exposes the claimed result. For example,
     a status-code check must actually display the status code.
   - Check local links, heading hierarchy, code fences, placeholders, and
     changed anchors.
   - Run `python3 scripts/check_markdown.py --strict <paths>` when editing
     local Markdown or MDX files. If an exact product string or quotation
     causes a language warning, verify that exception rather than rewriting
     the source text.

If a required fact remains unknown, omit it, qualify it, or report the gap
outside the deliverable. Add `TODO` only when the user explicitly asks for a
draft with unresolved placeholders.

## Select the page shape

Choose the structure by reader need, not by a universal template:

- Use a **README or landing page** to orient, provide the smallest credible
  first success, and route readers onward.
- Use a **tutorial or quickstart** to teach through a controlled,
  end-to-end experience.
- Use a **how-to or manual page** to help a capable reader complete a
  specific task.
- Use an **explanation or concept page** to build a mental model or discuss
  tradeoffs.
- Use a **reference page** for exact, complete lookup information.
- Use a **troubleshooting page** to diagnose a visible symptom and verify
  recovery.

For detailed structures and mixed-page guidance, read
`references/document-types.md`. Do not load that file for a small edit whose
structure is already clear.

## Write for scanning and comprehension

- Lead with the outcome, action, or decision. Avoid a history lesson before
  the reader knows why the page matters.
- Use present tense and active voice. Address the reader as `you` in task
  documentation.
- Define a new term at first use, then use one consistent name.
- Keep each paragraph about one topic. Vary sentence length enough to avoid
  choppy, mechanical prose.
- Put distinguishing information in the first sentence of a paragraph.
- Remove throat-clearing, marketing claims, repeated summaries, and
  unnecessary "what you will do" lists.
- Avoid `just`, `simply`, `obviously`, and `easy` when they dismiss real
  complexity. Do not ban a word when its literal use is the clearest wording.

Read `references/voice-and-style.md` when creating substantial prose,
calibrating tone, or revising text that feels stiff. Read
`references/original-examples.md` only when a concrete pattern would help.

## Use headings that match the content

- Start task headings with a plain verb: "Install the CLI" or "Rotate the
  key."
- Use noun phrases for concepts and lookup sections: "Configuration
  precedence" or "Error responses."
- Use sentence case.
- Use one descriptive level-one heading per page.
- Keep heading levels in order and make the headings useful as a standalone
  outline.
- Preserve established anchors when editing. Change them only when the
  benefit outweighs broken links.

## Write procedures deliberately

- Number two or more ordered actions.
- Write a one-action instruction as a sentence or bullet, not a one-item
  numbered list.
- Put one primary action in each step. Combine small actions only when they
  occur in the same place and cannot be misunderstood.
- State the action first and its result second.
- Mark optional steps with `Optional:`.
- Prefer one accessible primary path. Put meaningful alternatives after it.
- State where an action occurs before telling the reader to perform it.

## Use examples when they prove something

- Include a runnable example for an executable task.
- Do not force runnable examples into policy, glossary, index, release-note,
  or purely conceptual pages.
- Keep examples minimal, complete, copyable, and correct for the stated
  version and environment.
- Use `curl` first for an HTTP API when it is the clearest universal client.
  Use the product's primary language or interface for other APIs.
- Label fenced code blocks with a language. Label terminal output as `text`
  or `console`.
- Distinguish literal values from placeholders and explain every placeholder.
- Show expected output when it helps the reader prove success. Never present
  illustrative output as captured output.
- Never invent a flag, endpoint, field, return value, default, or error.

## Present reference information for lookup

- State the supported version or compatibility range when it matters.
- Document defaults, configuration locations, precedence, limits, units,
  side effects, and security implications at the point of use.
- Use a table when readers need to compare repeated fields.
- Avoid a table when prose or a short list is easier to scan, especially on a
  narrow screen.
- Include only applicable columns. Do not create a six-column table merely
  because six fields exist.
- Introduce a table with a sentence that explains what it contains.

## Troubleshoot calmly

Structure each entry around:

- **Symptom:** what the reader can observe.
- **Likely cause:** a supported, testable explanation.
- **Fix:** the exact recovery action.
- **Verify:** how to confirm recovery when it is not self-evident.

Prefer a diagnostic command or visible check over vague advice. Include only
realistic failures supported by evidence. Put security, data-loss, and cost
warnings beside the risky action, not in a distant final section.

## Keep the tone humane

- Use clear American English and a patient, matter-of-fact voice.
- Keep humor off by default. Use it only when the user or product voice
  permits it.
- Limit humor to one light aside per page.
- Direct any joke at predictable machine behavior, never at the reader.
- Do not joke in warnings, error explanations, security guidance, incident
  response, or troubleshooting.
- Avoid sarcasm, mockery, artificial cheerleading, and culture-specific
  wordplay that obscures the meaning.

## Preserve terminology

Use the repository's established names. If no glossary exists and terminology
is materially ambiguous, read `references/terminology-template.md` and build a
small working dictionary for the task. Keep that dictionary internal unless
the user asks for a glossary or style guide.

## Produce clean output

- Match the repository's Markdown or MDX dialect and callout syntax.
- Preserve meaningful links, code contracts, frontmatter fields, and
  generated markers.
- Do not emit internal modes, evidence notes, checklists, or terminology
  dictionaries into reader-facing documentation.
- Do not add empty sections to satisfy a template.
- When reviewing documentation, report evidence-backed findings instead of
  rewriting files unless the user requests changes.
- When rewriting, preserve facts and scope. Restructure only as much as the
  request and reader outcome require.

## Run the final check

Before delivery, confirm:

- Every product claim is supported and version-correct.
- The first useful action or answer appears early.
- Prerequisites and consequential warnings appear before the affected action.
- Executable examples are copyable and their claimed results are observable.
- Headings form a useful outline and match their section type.
- Terminology remains consistent.
- American English is used outside exact product text.
- Links, code fences, heading levels, and local conventions remain valid.
- No internal metadata, accidental placeholders, irrelevant sections, or
  invented facts remain.

For substantial pages, multi-page work, or documentation audits, read
`references/review-rubric.md` and use its quality gates.
