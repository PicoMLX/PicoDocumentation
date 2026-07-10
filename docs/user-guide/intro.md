---
title: About This Manual
sidebar_position: 1
---

Pico AI Server is a local AI server for macOS. It serves the WebUI at the root URL, exposes OpenAI-compatible and Ollama-compatible endpoints, adds an OpenResponses endpoint, and can share the service on your local network.

This manual is for three groups: the admin who runs Pico AI Server, the person who uses the WebUI, and the developer who connects a client. Start with the task you want to finish today, not at page one.

## Check that the server is reachable

Most pages in this manual assume Pico AI Server is running on the host Mac. Confirm that first:

```bash
curl http://127.0.0.1:11434/v1/models
```

If Pico AI Server is running, you get JSON back. On a clean installation the `data` array may be empty — that still counts as reachable. If the connection is refused, read [Install and Run Pico AI Server](./getting-started/install-and-run-pico-ai-server.md).

Unless a page says otherwise, examples use `http://127.0.0.1:11434` and run on the Mac that hosts Pico AI Server.

## How this manual is organized

- **Getting Started** installs the app, walks through settings, and connects a first client.
- **Networking & Sharing** covers LAN Mode, server addresses, and Bonjour discovery.
- **WebUI** covers the built-in browser chat and client-launch options.
- **Reference** documents the HTTP API surface, endpoint by endpoint.

## Where to go next

- Want the shortest path to a working result? Read the [Quick Start Roadmap](./quick-start-roadmap.md).
- Only need the endpoint list? Open the [Endpoint Summary](../reference/endpoint-summary.md).
