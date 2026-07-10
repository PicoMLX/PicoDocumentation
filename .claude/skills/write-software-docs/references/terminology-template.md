# Build an internal terminology dictionary

Read this file only when the project lacks a usable glossary and inconsistent
names would materially harm the documentation. Keep the resulting dictionary
internal unless the user requests a published glossary or style guide.

## Extract names from evidence

Check these sources in order:

1. User instructions and product naming guidance.
2. Public UI labels, command names, API schemas, and source identifiers.
3. Existing documentation and release artifacts.
4. Marketing copy only for official product capitalization, not technical
   behavior.

Record conflicts instead of silently normalizing them. Preserve exact strings
that readers must type or locate.

## Capture only useful distinctions

Use a compact working template:

```text
Product name:
Command or CLI name:
Service or daemon name:
Web interface name:
Configuration file:
Configuration directory:
Primary resource nouns:
Primary task verbs:
Authentication terms:
Address or URL terminology:
Important UI labels:
Deprecated terms:
```

Delete fields that do not apply. Add a term only when choosing the wrong name
would confuse a reader, break a command, or make related pages inconsistent.

## Separate prose from exact text

- Use American English for descriptive prose.
- Preserve exact product names, UI labels, commands, identifiers, file names,
  and API fields.
- Do not replace an exact technical term merely to satisfy a general language
  preference.
- Define an acronym at first use unless the intended audience reliably knows
  it.
- Use one term for one concept. Avoid casual synonyms after choosing the
  canonical term.

## Use safe example values

Prefer reserved or clearly fictional values:

- Domain: `example.com` or `api.example.com`
- IPv4 documentation address: `192.0.2.10`
- IPv6 documentation address: `2001:db8::10`
- Loopback address: `127.0.0.1`
- Generic identifier: `example-id`

Use a real default port, path, host name, or account name only when product
evidence confirms it. Do not use incomplete addresses such as
`192.168.x.y` in a command advertised as copyable.

## Resolve conflicts deliberately

When source code, UI text, and existing documentation disagree:

1. Determine which version each source describes.
2. Prefer current public behavior for current-version documentation.
3. Preserve an established public spelling when changing it would break
   compatibility or recognition.
4. Report a material source conflict to the user.
5. Avoid broad terminology cleanup outside the requested scope.

Do not emit unresolved placeholders into finished documentation.
