---
title: Connect External Tools with MCP
sidebar_position: 2
---

<!-- Mode: Manual -->

## Understand MCP support

Pico AI Server can act as a **Model Context Protocol (MCP) client**. Connect it
to one or more external MCP servers, and the tools those servers expose become
available to your models during a conversation. When a model decides to call one
of these tools, Pico AI Server forwards the call to the MCP server and feeds the
result back into the model's response.

This works for both the Chat API and the OpenResponses API. Any client talking to
Pico AI Server benefits from the connected tools without changing its own request
format — you do not have to declare the tools in each request.

## What you will do
- Open the MCP settings tab
- Add one or more external MCP servers
- Enable the servers and tools you want models to use
- (Optional) Authenticate to a server that requires OAuth

## Before you start
- A version of Pico AI Server that includes the **MCP** settings tab
- The URL of at least one MCP server you want to connect
- A model that supports tool (function) calling

## Add an MCP server
1. Open **Settings** in Pico AI Server.
2. Select the **MCP** tab.
3. Add a server by entering its endpoint URL.
4. Enable the server. Its available tools appear once Pico AI Server connects.
5. Enable the individual tools you want to expose to models.

Only enabled servers and tools are made available to models. Everything stays off
until you turn it on, so connecting a server does not expose its tools until you
enable them.

## Authenticate with OAuth
Some MCP servers require authorization before they will list or run tools. When a
server uses OAuth, Pico AI Server opens the server's sign-in flow and completes
the handshake through its registered callback. After you approve access, the
server's tools become available like any other.

## How tools reach the model
When you send a chat or responses request, Pico AI Server injects the enabled MCP
tools into the model's tool list before generation on these endpoints:

- **Chat API** — `POST /v1/chat`, `POST /api/chat`
- **OpenResponses API** — `POST /v1/responses`

If the model calls a tool, Pico AI Server runs it against the connected MCP server
and returns the result through the normal tool-calling flow. Tools you have not
enabled are never offered to the model.

For request and response formats, see the
[Chat API](../reference/chat/chat-api.md) and
[OpenResponses API](../reference/openresponses-api.md) reference pages.

## Security
- MCP tools run with whatever access the connected MCP server grants. Only connect
  servers you trust.
- Keep servers and tools disabled until you need them, and enable the minimum
  required.
- If you also expose Pico AI Server over your local network, require an API key in
  the **Users** tab so untrusted clients on the LAN cannot trigger tool calls.
