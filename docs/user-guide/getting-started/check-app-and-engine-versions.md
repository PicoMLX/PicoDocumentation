---
title: Check App and Engine Versions
sidebar_position: 4
description: Open the About window in Pico AI Server to read the app version and the exact engine package versions, and include them when you report a problem.
---

Pico AI Server runs models through a stack of engine packages. When you report a
bug, confirm which build you are on, or check that an update actually applied,
the **About** window shows both the app version and the exact version of each
engine package the app was built with.

## Open the About window

1. In the macOS menu bar, open the **Pico Server** menu (the app menu, next to the
   Apple menu).
2. Choose **About Pico Server**.

The window opens with the app name and its version at the top, for example
`Version 1.2.3 (456)` — the release version followed by the build number in
parentheses.

## Read the engine versions

Below the app version, the **Engine Versions** section lists the packages that
make up the inference stack:

| Entry | What it is |
| --- | --- |
| **EngineRouter** | The engine routing layer that dispatches requests to a model's engine |
| **PicoCore** | The shared on-device model engine |
| **MLX core** | The native MLX library, reported by MLX itself |
| **mlx-swift** | The Swift bindings for MLX |
| **mlx-swift-lm** | The Swift language-model layer on top of MLX |

Each engine entry (except **MLX core**, which reports its own version string) is
shown as the package's build provenance:

- A release tag followed by a short commit revision in parentheses, such as
  `0.4.0 (1a2b3c4d)`.
- Just the short commit revision when the build is not from a tagged release.
- The label followed by **(modified)** when the app was built against locally
  changed sources rather than an exact published commit.
- **Version unavailable** when the build provenance could not be read.

## Verify it worked

You have read the version information correctly when:

- The **Engine Versions** section lists all five entries — EngineRouter,
  PicoCore, MLX core, mlx-swift, and mlx-swift-lm — and each shows a value
  (a version or a revision) rather than being blank.
- The `Version …` line at the top of the window matches the build you
  installed.

You can also confirm the app version and build without opening the window, by
asking the server's version endpoint. Run this on the Mac running Pico AI
Server:

```bash
curl http://127.0.0.1:11434/api/version
```

From another device, replace `127.0.0.1` with the server's LAN address — see
[Connect a Client](./connect-a-client.md) — which requires **Allow local network
connections** to be on.

A running server replies with JSON:

```json
{
  "name": "Pico AI Server",
  "bundleIdentifier": "com.starlingprotocol.PicoServer",
  "version": "1.2.3",
  "build": "456"
}
```

The `version` and `build` fields match the `Version 1.2.3 (456)` line at the top
of the About window. The endpoint reports only the app version — the per-engine
versions in the **Engine Versions** section are shown only in the About window.
If the number you get back here or in the window does not match the release you
just installed, the update did not take effect.

## Why this matters

Include these versions when you file a bug report or ask for help — the engine
versions pin down exactly which inference stack produced the behavior you are
seeing, which the app version alone does not. They are also the quickest way to
confirm that a specific MLX or PicoCore build is the one actually running after
an update.

## Next steps

- [Configure Settings](./configure-settings.md)
- [Connect a Client](./connect-a-client.md)
