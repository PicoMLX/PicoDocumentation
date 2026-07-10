# Calibrate the teaching voice

Use an original, modern voice. Draw on the pedagogical strengths of classic
hands-on programming manuals without imitating a named author or copying
period prose.

## Contents

- [Teach through action and consequence](#teach-through-action-and-consequence)
- [Establish recovery early](#establish-recovery-early)
- [Reveal detail progressively](#reveal-detail-progressively)
- [Build a mental model](#build-a-mental-model)
- [Anticipate the next question](#anticipate-the-next-question)
- [Vary the cadence](#vary-the-cadence)
- [Sound confident without overselling](#sound-confident-without-overselling)
- [Use restrained humor](#use-restrained-humor)
- [Preserve American English](#preserve-american-english)
- [Understand the inspiration](#understand-the-inspiration)

## Teach through action and consequence

Use this rhythm when it helps:

1. Give a concrete action.
2. Describe the visible result.
3. Explain what changed.
4. Connect that explanation to the reader's next decision.

Do not separate an action from its result with several paragraphs of
background.

### Less useful

> The configuration system provides several mechanisms through which values
> may be supplied.

### More useful

> Set `ACORN_PORT` to change the listening port. The service reads the
> variable at startup, after the configuration file and before command-line
> options.

The revision gives the reader an action, effect, timing, and precedence.

## Establish recovery early

Tell readers how to stop, undo, retry, or return to a known state before an
experiment becomes costly. Include cleanup when a tutorial creates resources.
Put rollback instructions beside a risky change rather than in a remote
appendix.

## Reveal detail progressively

Start with the smallest complete path. Introduce extra options after the
reader has a working baseline. Explain advanced behavior at the moment it
becomes relevant.

Avoid both extremes:

- Do not bury the first action beneath architecture and history.
- Do not give unexplained commands that leave the reader unable to adapt.

## Build a mental model

Explain the artifacts and state transitions the reader can observe. After a
build, for example, identify which files were created and which tool created
them. After a request, explain which component accepted it and what happens
next.

Use concrete relationships before abstract terminology. Define the formal
term once the reader has something to attach it to.

## Anticipate the next question

Answer the question raised naturally by the preceding result:

- Where did the file go?
- Which value wins when two settings exist?
- Does the change survive a restart?
- How do I stop it?
- What happens at the limit?
- How do I know the retry succeeded?

Do not invent an answer merely because the question is predictable. Inspect
the product evidence or report the gap.

## Vary the cadence

Prefer clear sentences, but do not turn every sentence into a clipped command.
Mix concise actions with fuller explanations. Keep each paragraph focused on
one topic, usually in two to five sentences.

Let the browser wrap prose naturally. Do not use hard line breaks to enforce
the visual width of a paragraph in the rendered page.

## Sound confident without overselling

- Prefer specific claims over adjectives.
- Replace "powerful," "seamless," and "easy" with observable behavior.
- Use contractions when they sound natural.
- Acknowledge limits plainly.
- Celebrate a meaningful success sparingly and only after it occurs.
- Never imply that a confused reader failed a test of intelligence.

## Use restrained humor

Keep humor off unless the requested or established product voice supports it.
When a light aside genuinely helps:

- Limit it to one per page.
- Aim it at literal or predictable machine behavior.
- Keep it short enough to remove without changing the instructions.
- Avoid idioms that complicate translation.

Never use humor in a warning, error explanation, security procedure,
incident response, or troubleshooting entry.

## Preserve American English

Write prose in American English unless the user explicitly requests another
locale. Preserve exact product names, UI text, identifiers, commands, and
quotations even when they use another spelling.

## Understand the inspiration

The useful source characteristics are progressive examples, immediate
feedback, recovery paths, artifact inspection, conversational transitions,
and explanations attached to actions. The source prose also contains dated
assumptions, long digressions, OCR errors in available scans, and humor that
does not suit modern global documentation.

Use the characteristics, not the wording:

- [Stan Kelly-Bootle, `Mastering Turbo C`](https://bitsavers.org/pdf/borland/turbo_c/Kelly-Bootle_Mastering_Turbo_C_2ed_1989.pdf)
- [Borland, `Turbo C User's Guide`](https://bitsavers.org/pdf/borland/turbo_c/Turbo_C_Users_Guide_1987.pdf)
- [Borland, `Turbo C Reference Guide`](https://bitsavers.org/pdf/borland/turbo_c/Turbo_C_Reference_Guide_1987.pdf)
