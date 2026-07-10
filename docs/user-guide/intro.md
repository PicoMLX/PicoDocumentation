---
title: About This Manual
sidebar_position: 1
---

<!-- Mode: Manual -->

Pico AI Server is a local AI server for macOS. It serves the WebUI at the root URL, exposes OpenAI-compatible and Ollama-compatible endpoints, adds an OpenResponses endpoint, and can share the service on your local network.

This manual is for three groups: the admin who runs Pico AI Server, the person who uses the WebUI, and the developer who connects a client. Start with the task you want to finish today.

## What you'll do
- Pick the right starting page.
- Check that Pico AI Server is reachable.
- Jump to the correct API reference.

## Before you start
- Use `http://127.0.0.1:11434` unless a page says otherwise.
- Run the examples on the Mac that hosts Pico AI Server unless the page says to test from another device.

## Pick your path
1. If you want browser chat on one Mac, read [Install and Run Pico AI Server](./getting-started/install-and-run-pico-ai-server.md).
2. If you want to share Pico AI Server on your LAN, read [Configure Settings](./getting-started/configure-settings.md) and [LAN Sharing Basics](./networking/lan-sharing-basics.md).
3. If you are building a client, read [Connect a Client](./getting-started/connect-a-client.md) and then the Reference section.
4. If you only need the endpoint list, open [Endpoint Summary](../reference/endpoint-summary.md).

## Verify it worked
Run:

```bash
curl http://127.0.0.1:11434/v1/models
```

If Pico AI Server is running, you get JSON back. On a clean installation the `data` array may be empty.

## Try it now

```bash
open http://127.0.0.1:11434
```

This should open the WebUI in your browser.

## Troubleshooting
- **Symptom:** `curl` says the connection was refused.
  **Cause:** Pico AI Server is not running.
  **Fix:** Read [Install and Run Pico AI Server](./getting-started/install-and-run-pico-ai-server.md).
- **Symptom:** The browser opens, but you cannot use a model yet.
  **Cause:** No model is available.
  **Fix:** Open the native app and check the `Models` tab.

## Next steps
- [Quick Start Roadmap](./quick-start-roadmap.md)
- [Endpoint Summary](../reference/endpoint-summary.md)
