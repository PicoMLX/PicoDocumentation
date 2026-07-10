# Choose a document structure

Read this file when creating a page, reorganizing a substantial page, or
deciding how mixed documentation should work. Select useful sections; do not
copy a whole template by default.

## Contents

- [Match the reader's need](#match-the-readers-need)
- [Shape a README or landing page](#shape-a-readme-or-landing-page)
- [Shape a tutorial or quickstart](#shape-a-tutorial-or-quickstart)
- [Shape a how-to or manual page](#shape-a-how-to-or-manual-page)
- [Shape an explanation or concept page](#shape-an-explanation-or-concept-page)
- [Shape a reference page](#shape-a-reference-page)
- [Shape troubleshooting](#shape-troubleshooting)
- [Edit an existing page](#edit-an-existing-page)

## Match the reader's need

| Page type | Reader need | Primary measure of success |
|---|---|---|
| README or landing page | "What is this, and can I use it?" | The reader reaches a credible first result and knows where to go next. |
| Tutorial or quickstart | "Help me learn by doing." | The reader completes a controlled lesson and understands the next step. |
| How-to or manual page | "Help me complete this task." | The reader completes and verifies a real-world goal. |
| Explanation or concept page | "Help me understand this." | The reader gains a useful mental model or can evaluate a tradeoff. |
| Reference page | "Give me the exact facts." | The reader finds an accurate answer quickly. |
| Troubleshooting page | "Help me recover." | The reader identifies the cause, applies a fix, and verifies recovery. |

Treat the type as an internal planning choice. Never print a type or mode
marker in the deliverable.

## Shape a README or landing page

Treat a README as a deliberate mixture rather than forcing it into one mode.
Use the smallest useful subset of:

1. Product name and concrete value.
2. Compatibility or prerequisites that determine whether the reader can
   continue.
3. The shortest supported install, run, and verification path.
4. One representative use case.
5. Common configuration or operational facts.
6. Security implications that affect first use.
7. Links to deeper tutorials, reference, support, contribution, or license
   information.

Keep exhaustive option tables and long conceptual explanations in linked
pages when the repository supports them. A small project may reasonably keep
them in the README.

## Shape a tutorial or quickstart

Use a stable, controlled path:

1. State the learning outcome.
2. List only prerequisites that block progress.
3. Establish a known starting state.
4. Lead the reader through ordered actions.
5. Show observable results at meaningful checkpoints.
6. Explain only what the reader needs at that point.
7. Verify the final result.
8. Provide cleanup and next steps when they matter.

Optimize a tutorial for successful learning, not for every production
variation. Move alternatives and exhaustive options elsewhere.

## Shape a how-to or manual page

Assume the reader has basic product knowledge. Organize around one practical
goal:

1. State the outcome and important constraints.
2. Put prerequisites, permissions, and risks before the procedure.
3. Give the shortest supported primary path.
4. Show the expected result.
5. Explain meaningful alternatives after the primary path.
6. Include realistic troubleshooting or rollback only when supported.

Avoid turning a how-to page into a lesson or complete reference.

## Shape an explanation or concept page

Build a mental model:

1. State what the concept explains and why it matters.
2. Define its boundaries and relationship to neighboring concepts.
3. Explain the mechanism, rationale, or tradeoffs.
4. Use a diagram or illustrative example only when it improves understanding.
5. Link to tasks and reference information rather than reproducing them.

Do not force numbered steps, runnable commands, expected terminal output, or
troubleshooting into a page that does not describe an executable task.

## Shape a reference page

Optimize for accurate lookup. Use stable names, parallel structures, and
meaningful ordering. Include fields only when they apply.

For CLI reference, consider:

- Command form and subcommands.
- Arguments, options, types, defaults, constraints, and repeatability.
- Configuration and environment-variable precedence.
- Exit status, output streams, side effects, examples, and errors.

For HTTP API reference, consider:

- Method, path, authentication, headers, parameters, and limits.
- Request and response schemas.
- One minimal request whose shown output is observable.
- Success and error status codes, error shape, retries, and idempotency.

For library reference, consider:

- Signature, availability, types, defaults, ownership, side effects, errors,
  concurrency behavior, and a minimal example.

For configuration reference, consider:

- File locations, supported formats, keys, types, defaults, constraints,
  precedence, reload behavior, and security-sensitive values.

For policy, compatibility, or support reference, consider:

- Scope, supported versions or systems, time windows, exceptions, and
  explicitly excluded promises.

Do not add parameter, request, response, error, or example sections when the
subject has none.

## Shape troubleshooting

Lead with the exact symptom a reader is likely to search for. For each entry:

1. Quote or describe the observable symptom.
2. Give the most likely supported cause.
3. Provide a diagnostic check when more than one cause is plausible.
4. Give the recovery action.
5. Show how to verify recovery.
6. State escalation or data-loss implications when relevant.

Group entries by symptom or subsystem, not by an internal implementation
taxonomy the reader does not know.

## Edit an existing page

Preserve facts, links, generated regions, frontmatter, code contracts, and
useful anchors. Keep the existing information architecture unless the user
asks for a restructure or the current structure blocks the requested outcome.
Make the smallest coherent change rather than converting every heading and
section to a preferred template.
