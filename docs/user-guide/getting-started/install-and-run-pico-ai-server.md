---
title: Install and Run Pico AI Server
sidebar_position: 1
---

This page gets Pico AI Server running and proves the WebUI and API are alive. The goal is simple: start the server, open the browser chat, and confirm the default endpoint responds on port `11434`.

Pico AI Server is a macOS app for Apple Silicon Macs — it runs models with MLX, which requires an M-series chip, so Intel Macs are not supported. The default server port is `11434`.

## Start the server

1. Launch Pico AI Server.
2. Complete the first-run setup wizard. It has four pages:
   - **Welcome** — a short introduction.
   - **Model** (*Choose your first model*) — pick the model to download. Models are grouped into tiers named **Fast**, **Balanced**, and **Reasoning**; Pico preselects the tier that fits your Mac's RAM and badges it **Recommended**. You can add or switch models later.
   - **Access** (*Choose who can connect*) — choose **This Mac only** or **Devices on my local network**. Choosing local-network access reveals **Make Pico discoverable automatically** (Bonjour) as a nested option.
   - **Ready** — shows the live server status, the model, the access scope, and the server address. **Open Chat** finishes setup and opens the WebUI; **Copy address** copies the server address.
3. Open the WebUI at `http://127.0.0.1:11434/`.
   The Ready page's **Open Chat** button normally opens this address for you.
4. The Access choice sets the bind address. **Devices on my local network** binds Pico AI Server to `0.0.0.0`; **This Mac only** binds it to `127.0.0.1`. You can change this later with `Allow local network connections` in the app's settings.
5. Use the menu extra when you need quick control.
   When the server is running, it shows the status, a `Start` or `Stop` button, and an IP-based server address with a copy button.

Options such as **Open at login** and **Prevent sleep** are not part of the setup wizard. Configure them in the app's **Settings** window instead.

:::caution
Choosing **Devices on my local network** binds the server to every interface, and a fresh install does **not** require an API key — so any device on the LAN can use your models and tools. Before you share on a network, turn on authentication: see [Require an API Key](../access/require-an-api-key.md).
:::

## Verify it worked

Run:

```bash
curl http://127.0.0.1:11434/v1/models
```

If you get a JSON response, the server is up. If you also open `http://127.0.0.1:11434/`, the WebUI should load in your browser.

To see the host name Pico AI Server reports for the Mac, ask the server directly:

```bash
curl http://127.0.0.1:11434/hostname
```

## Troubleshooting

- **Symptom:** The browser opens a blank page or cannot connect.
  **Cause:** The server is not running yet.
  **Fix:** Use the native app or the menu extra to start the server, then reload the page.
- **Symptom:** Another device on your LAN cannot connect.
  **Cause:** `Allow local network connections` is off, or the network blocks device-to-device traffic.
  **Fix:** Turn the setting on and test again from the other device.
- **Symptom:** The WebUI opens, but no model is usable.
  **Cause:** No model is available yet.
  **Fix:** Open the `Models` tab in the native app and wait for a model to become available.

## Next steps

- [Configure Settings](./configure-settings.md)
- [Use the WebUI](../webui/use-the-webui.md)
