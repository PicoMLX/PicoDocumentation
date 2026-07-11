---
title: Connect External MCP Servers
sidebar_position: 4
description: Add external Model Context Protocol (MCP) servers in Pico AI Server so your local models can call their tools during a conversation.
---

Pico AI Server can act as a **Model Context Protocol (MCP) client**: connect it to external MCP servers, and the tools those servers expose become available to your local models during generation. A model running in Pico can then call a remote tool mid-answer and ground its response in the result, instead of relying on its training alone.

This is the opposite direction from exposing Pico's own tools. Connecting external servers is covered here; letting other apps reach *your* enabled tools is covered in [Enable Built-in Tools](./enable-built-in-tools.md). Both live in the **MCP** settings tab.

You need a version of Pico AI Server that includes the **MCP** settings tab, and the HTTP(S) URL of an MCP server. Pico connects over the **Streamable HTTP** MCP transport (HTTP(S) endpoints only). To use a stdio-only MCP server, run a gateway that exposes it over Streamable HTTP, then point Pico at the gateway's URL rather than at the stdio server directly. A legacy SSE-only endpoint may not connect.

## Add a server

1. Open **Settings** in Pico AI Server and select the **MCP** tab.
2. Under **External MCP Servers**, click **Add Server**.
3. In the **Server** section, enter:
   - **Name** — a label for the server, such as `My Example`.
   - **Endpoint URL** — the server's HTTP(S) address, such as `https://example.com/mcp`.
4. Choose an **Authentication** method (see [Authentication](#authentication) below).
5. Optionally paste the server's usage notes into **Instructions** (see [Instructions](#instructions-optional) below).
6. Click **Save**.

A newly added server is enabled by default. Enabling a server trusts its tools, so only add servers you trust.

## Authentication

The **Authentication** picker offers three options:

- **None** — no credentials are sent.
- **Bearer Token** — paste an access token. It is sent as an `Authorization: Bearer` header and stored in the system keychain, never in the app's database.
- **OAuth** — sign in through your browser after saving. Pico registers itself with the server automatically using dynamic client registration (OAuth 2.1 with PKCE), and tokens are stored in the keychain. This requires the server to advertise a client-registration endpoint; see [Troubleshooting](#troubleshooting) if sign-in reports that it does not.

For an OAuth server, save it first, then open it again from the server list to **Sign In**. The Authentication section shows whether you are signed in and lets you **Sign Out**; signing out drops the stored tokens and registration so your next sign-in can use a different account.

## Instructions (optional)

The **Instructions** field holds free-form usage notes for the server — for example, the contents of its `SKILL.md`. Pico stores the text as-is and prepends it as a system message to guide the model whenever the server is enabled. The text is used only as guidance; scripts are never run.

Because these instructions become part of the model's system prompt, paste only notes from a server you trust, and review them first. Like any prompt content, broad or malicious instructions can steer the model's behavior and tool calls on later requests — even though the text itself is never executed.

## Enable, test, and edit servers

Each configured server appears as a row under **External MCP Servers** with a toggle to enable or disable it and a status line showing its connection state and tool count.

- **Test connections** — click the refresh button in the **External MCP Servers** header to reconnect enabled servers and update their tool counts.
- **Edit or delete** — open a server's row to change its settings, sign in or out of an OAuth server, or delete it. Deleting a server also removes its stored credentials from this device.

Only **enabled** servers are connected and have their tools offered to your models. Disable a server to stop using its tools without deleting its configuration.

## Try it now

1. Add and enable an MCP server in the **MCP** tab, then click the refresh button and confirm the row reports a non-zero tool count.
2. With a tool-capable model installed, ask a question that *requires* one of the server's tools, so the answer can only come from a tool call. From the Web Chat or over the API:

   ```bash
   curl http://127.0.0.1:11434/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{
       "model": "MODEL_NAME",
       "messages": [
         { "role": "user", "content": "YOUR_QUESTION" }
       ]
     }'
   ```

   Replace the two placeholders:
   - `MODEL_NAME` — the ID of an installed tool-capable model; list them with `GET /v1/models`.
   - `YOUR_QUESTION` — a request that only a tool from the server you connected can satisfy. For example, if you connected a documentation server such as DeepWiki, ask `Use DeepWiki to summarize the README of the facebook/react repository.`

The tools from your enabled servers are folded into the request across every generation path (OpenAI-compatible chat, Ollama-compatible, and the OpenResponses path used by the Web Chat).

## Verify it worked

- The server's row shows a connected status and a tool count greater than zero after you refresh.
- The model's answer reflects the tool's result — repository-specific detail, a live lookup, or similar — rather than a generic guess.
- Disable the server and ask again: the model can no longer use that tool.

## Privacy and trust

- Enabling a server trusts its tools; add only servers you control or trust.
- Credentials (bearer tokens and OAuth sessions) are kept in the system keychain, not in the app's database, and are removed when you delete the server.
- Server **Instructions** are treated as text only and are never executed. Still, review them before pasting — they steer the model as prompt content (see [Instructions](#instructions-optional)).
- An enabled server's tools run on behalf of **any** client that can send prompts to Pico — including clients on your LAN — using your stored credentials for that server. A prompt from any such client can make the model call the server's tools as that account. If you share Pico on a network, enable user accounts and require an API key in the **Users** tab — this turns on bearer-token enforcement, which is off by default — and enable only servers whose actions you are comfortable exposing to every connected client.

## Troubleshooting

**Refresh shows zero tools, or the server won't connect.**

- Confirm the **Endpoint URL** is the server's MCP endpoint (often ending in `/mcp`) and is reachable over HTTP(S) from this Mac.
- Make sure the server's toggle is on, then click the refresh button in the **External MCP Servers** header to reconnect and re-count tools.
- If the server needs credentials, check the **Authentication** section: a bearer token must be current, and an OAuth server must be signed in.

**OAuth sign-in fails.**

- Pico completes OAuth using dynamic client registration. If the server does not advertise a client-registration endpoint, sign-in fails with a message such as "The server doesn't advertise a client registration endpoint, and no client ID is configured," and Pico cannot connect to that server over OAuth.
- If sign-in was canceled or interrupted, reopen the server and check whether it shows **Signed in**; if not, sign in again.

**The model doesn't use the server's tools.**

- Verify the server is enabled and its row reports a tool count greater than zero.
- Use a model that supports tool (function) calling — a model without tool support never calls external tools.
- Tools from enabled servers are added on every generation path (OpenAI-compatible chat, Ollama-compatible, and OpenResponses), so confirm your request reached one of those endpoints.

## Next steps

- Turn Pico's own tools into an MCP server for other apps: [Enable Built-in Tools](./enable-built-in-tools.md).
- Share Pico safely on your network before exposing tools: [LAN Sharing Basics](./networking/lan-sharing-basics.md).
