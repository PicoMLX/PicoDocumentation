---
title: About Pico AI Server
description: Pico AI Server runs large language models locally on your Mac and serves them through OpenAI- and Ollama-compatible APIs. Start here.
sidebar_position: 1
---

<!-- Mode: Manual -->

# About Pico AI Server

Pico AI Server runs large language models on your own Mac and serves them
through OpenAI- and Ollama-compatible APIs. Prompts and data stay on your
machine, and existing clients connect without code changes.

## What you can do

- Run chat, completion, and embedding models locally.
- Call them with OpenAI-compatible (`/v1/...`) or Ollama-compatible
  (`/api/...`) endpoints.
- Open the built-in WebUI to chat in a browser.
- Share the server with other devices on your network, or reach it remotely.

By default the server listens on port `11434`.

## Who this manual is for

- **Admins** who install Pico AI Server, download models, and manage sharing.
- **Client developers** who connect apps to the server's APIs.
- **Power users** who want a private AI server on their own hardware.

## How this documentation is organized

- **User Guide** — task-first pages: install and run the server, connect a
  client, and set up networking such as [Bonjour discovery](./networking/bonjour.md),
  [HTTPS with Caddy](./networking/https-with-caddy.md), and
  [remote access with Tailscale](./networking/remote-access-with-tailscale.md).
- **Reference** — API contracts for [chat](../reference/chat/chat-api.md),
  [models](../reference/models/models-api.md), and
  [embeddings](../reference/embeddings/embeddings-api.md), plus the
  [OpenResponses API](../reference/openresponses-api.md) and the
  [custom URL scheme](../reference/custom-url-scheme.md).

## Verify your setup

With Pico AI Server running, list the installed models:

```bash
curl http://127.0.0.1:11434/v1/models
```

A JSON response means the server is reachable. If you get a connection error,
confirm Pico AI Server is running and listening on port `11434`.

## Next steps

- New to Pico AI Server? Start with the User Guide.
- Building a client? Go straight to the [Chat API](../reference/chat/chat-api.md).
