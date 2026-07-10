# Use original documentation patterns

Use these fictional examples to calibrate structure and rhythm. Never copy
their product names, commands, behavior, defaults, or output into real
documentation. Establish every real fact from the target project.

## Contents

- [Lead a README with a credible first result](#lead-a-readme-with-a-credible-first-result)
- [Make the verification command prove the claim](#make-the-verification-command-prove-the-claim)
- [Avoid a one-item numbered procedure](#avoid-a-one-item-numbered-procedure)
- [Match headings to section purpose](#match-headings-to-section-purpose)
- [Write a policy reference without fake machinery](#write-a-policy-reference-without-fake-machinery)
- [Connect a failure to recovery](#connect-a-failure-to-recovery)
- [Keep unresolved facts out of finished copy](#keep-unresolved-facts-out-of-finished-copy)

## Lead a README with a credible first result

This pattern gives the reader orientation, one supported path, and visible
proof without exposing internal planning metadata.

> # Northstar Relay
>
> Northstar Relay accepts local webhook requests and forwards them to a
> configured target.
>
> ## Start a local relay
>
> Install the command:
>
> ```shell
> brew install example/tap/northstar-relay
> ```
>
> Start a loopback listener:
>
> ```shell
> northstar-relay start --target https://example.test/hooks
> ```
>
> Look for:
>
> ```text
> Listening on http://127.0.0.1:8787
> ```

Why it works:

- The opening says what the product does.
- The first action appears early.
- The result is observable.
- The page does not add a mode marker, hidden glossary, or ceremonial
  overview.

## Make the verification command prove the claim

### Weak

> Run `curl http://127.0.0.1:8787/health`. Expect status `200`.

The default command output may not show the HTTP status.

### Stronger

> Request the health endpoint and include response headers:
>
> ```shell
> curl -i http://127.0.0.1:8787/health
> ```
>
> Look for `HTTP/1.1 200 OK` and this response body:
>
> ```json
> {"status":"ok"}
> ```

Use the exact command and output supported by the real product. The pattern
matters; these fictional values do not.

## Avoid a one-item numbered procedure

### Mechanical

> 1. Run `northstar-relay stop`.

### Natural

> Stop the relay with `northstar-relay stop`.

Use numbering when order matters across two or more actions.

## Match headings to section purpose

Use a task heading for an action:

> ## Configure a timeout

Use a noun heading for lookup or explanation:

> ## Configuration precedence

Do not force every section into an imperative phrase.

## Write a policy reference without fake machinery

A non-executable policy can be complete without commands, parameters, or
request examples:

> # Support policy
>
> ## Release channels
>
> Stable releases receive fixes for the documented support window. Preview
> releases have no guaranteed support window.
>
> ## Supported systems
>
> The support matrix lists the operating systems and architectures covered by
> this policy.
>
> ## Exceptions
>
> Security incidents may require a change without the usual notice period.

Do not add a final sentence explaining that the page has no runnable example.

## Connect a failure to recovery

### Vague

> If startup fails, check the port and try again.

### Testable

> **Symptom:** Startup reports `address already in use`.
>
> **Likely cause:** Another process is listening on the configured port.
>
> **Fix:** Stop that process or select an unused port.
>
> **Verify:** Start the relay again and confirm that it prints the listening
> address.

Use a diagnostic command only when the product or platform evidence supports
it.

## Keep unresolved facts out of finished copy

### Draft-only placeholder

> The default timeout is `TODO: confirm default`.

### Finished documentation

Omit the unsupported default. Report the missing fact to the user outside the
document, or qualify the statement if a useful supported claim remains.
