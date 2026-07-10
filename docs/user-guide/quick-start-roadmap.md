---
title: Quick Start Roadmap
sidebar_position: 2
---

<!-- Mode: Manual -->

Use this page when you want the shortest path to a working result. Pick one route, prove it works early, then come back for detail only if you need it.

## What you'll do
- Pick the fastest route for your job.
- Test the server before you spend time on fine tuning.
- Jump straight to the right chapter.

## Before you start
- Pico AI Server uses port `11434` by default.
- The browser chat lives at the root URL.

## Pick a route
1. If you just want it running on one Mac, read [Install and Run Pico AI Server](./getting-started/install-and-run-pico-ai-server.md), then open `http://127.0.0.1:11434`.
2. If you want to share it with other devices, read [Configure Settings](./getting-started/configure-settings.md), then [LAN Sharing Basics](./networking/lan-sharing-basics.md).
3. If you are building an API client, read [Connect a Client](./getting-started/connect-a-client.md), then [Models API](../reference/models/models-api.md) and [Chat API](../reference/chat/chat-api.md).
4. If you want browser chat plus external tools, read [Use the WebUI](./webui/use-the-webui.md) and then the MCP notes inside the settings dialog.

## Verify it worked
Run:

```bash
curl http://127.0.0.1:11434/v1/models
```

If you get JSON back, the server is reachable.

## Try it now

```bash
curl http://127.0.0.1:11434/ip
```

This returns the current IP address that Pico AI Server can share on the local network.

## Troubleshooting
- **Symptom:** You can use the server locally, but another device cannot connect.
  **Cause:** `Allow local network connections` is off, or the network blocks device-to-device traffic.
  **Fix:** Read [LAN Sharing Basics](./networking/lan-sharing-basics.md).
- **Symptom:** Your client connects but cannot find a model.
  **Cause:** The server has no available model yet.
  **Fix:** Check the `Models` tab in the native app.

## Next steps
- [Install and Run Pico AI Server](./getting-started/install-and-run-pico-ai-server.md)
- [Connect a Client](./getting-started/connect-a-client.md)
