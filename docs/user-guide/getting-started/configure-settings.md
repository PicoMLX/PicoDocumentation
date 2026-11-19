---
title: Configure Settings
sidebar_position: 2
---

Pico AI Server keeps its configuration in the native app's **Settings** window. Settings is organized into tabs along the top of the window: **General**, **Inference**, **Models**, **Library**, **Server**, **Tools**, and **Access**. This page explains what each tab controls, then walks through the two changes most admins make first: where models are stored, and the server's network behavior.

Before you start, open Pico AI Server and keep a terminal ready so you can test with `curl` after a change.

## Open Settings

Open **Settings** from the Pico AI Server menu bar, or press `Cmd+,`. The window opens on the tab you used last.

## What each tab controls

- **General** — Startup (`Open at Login`), energy (`Prevent automatic sleep while Pico is running`), and `Request History`, which controls whether Pico records request metadata and for how long.
- **Inference** — The `Default model` used for Web Chat, Mac Cluster, and requests that omit a model; the `Default response limit` (maximum output tokens per request); and `Unload idle models after`, which frees memory when a model goes unused.
- **Models** — Browse, download, and manage language and embedding models.
- **Library** — Where models are stored, linked libraries such as LM Studio, and your Hugging Face account.
- **Server** — Start and stop the server, set the `Server name`, control network access and discovery, Web Chat, the `Port`, CORS, and Mac Cluster. Applying a change here restarts the server.
- **Tools** — Pico's `Built-in Tools` and `MCP` connections, switched with the segmented control at the top of the tab.
- **Access** — `Require API Key`, remote dashboard access, and the list of user accounts and their API keys.

## Change where models are stored

Model storage lives in the **Library** tab. You cannot move the library while the server is running.

1. Open Settings and select the **Library** tab.
2. Read the `Location` row to see the current model folder. Use `Show in Finder` to open it.
3. To move the library, first stop the server in the **Server** tab, then click `Move Library…` and choose a folder or drive. Pico Server creates a models folder in the location you choose and moves your downloaded models into it.
4. Optional: click `Use Default Location…` to switch back to the built-in library. Your current models stay where they are, and Pico Server uses the models in its default library instead.

To download private, organization-owned, or gated models you have access to, sign in under `Hugging Face` in the same tab.

## Change a network setting

The server's network settings live in the **Server** tab. Applying a change to the server name, connections, Web Chat availability, port, or CORS restarts the server, so make the change, apply it, and confirm the server still responds before you move on.

1. Open Settings and select the **Server** tab.
2. Review the controls you need:
   - `Status` and the `Start Server` / `Stop Server` button.
   - `Server name`.
   - `Allow local network connections` — when off, only apps on this Mac can connect.
   - `Discoverable on the local network` — Bonjour discovery, available only when local network connections are on.
   - `Enable Web Chat` and `Model selection`.
   - `Port`.
   - `Allow cross-origin requests (CORS)`.
3. Click `Apply and Restart Server`. When the server is stopped, the same button reads `Apply and Start Server`.

The app saves the configuration and restarts the server. The `Model selection` choice for Web Chat takes effect immediately, without a restart.

## Verify it worked

Run:

```bash
curl http://127.0.0.1:11434/v1/models
```

If you changed the port, use the new port instead. You should still get JSON back after the server restarts.

If you plan to test from another device on the same LAN, get the address to use:

```bash
curl http://127.0.0.1:11434/ip
```

## Troubleshooting

- **Symptom:** The WebUI stops working after you turn on `Allow cross-origin requests (CORS)`.
  **Likely cause:** Enabling CORS can interfere with the browser chat.
  **Fix:** Turn CORS back off unless a separate client needs it.
- **Symptom:** The server no longer answers on the old port.
  **Likely cause:** You changed `Port` and applied the change, which restarted the server.
  **Fix:** Use the new server address everywhere.
- **Symptom:** `Move Library…` is disabled.
  **Likely cause:** The server is running, and the library cannot move while it is serving models.
  **Fix:** Stop the server in the **Server** tab, then move the library.

## Next steps

- [Connect a Client](./connect-a-client.md)
- [LAN Sharing Basics](../networking/lan-sharing-basics.md)
