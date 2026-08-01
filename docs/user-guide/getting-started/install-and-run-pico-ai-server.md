---
title: Install and Run Pico AI Server
sidebar_position: 1
---

This page gets Pico AI Server running and proves the WebUI and API are alive. The goal is simple: start the server, open the browser chat, and confirm the default endpoint responds on port `11434`.

Pico AI Server is a macOS app for Apple Silicon Macs — it runs models with MLX, which requires an M-series chip, so Intel Macs are not supported. The default server port is `11434`.

## Start the server

On first launch, a short setup wizard walks you through four steps — **Welcome**, **Choose your first model**, **Choose who can connect**, and **Ready**.

1. Launch Pico AI Server and click `Set up Pico` on the Welcome screen.
2. On the model step, pick the model recommended for your Mac, choose a different one, or skip and add one later in Settings.
   If you start a download, it continues in the background while you finish setup.
3. On the access step, choose who can reach the server:
   - `This Mac only` — Pico AI Server binds to `127.0.0.1`, so only apps on this Mac can connect.
   - `Devices on my local network` — Pico AI Server binds to `0.0.0.0`, so other devices on your network can connect. Turn on the Bonjour option here if you want Pico AI Server to be discoverable automatically.

   You can change this later in Settings.
4. On the `Ready` step, click `Start server`.
   This saves your choices, starts the server, and confirms it is reachable. Navigating through the wizard never starts or stops the server — nothing runs until you click `Start server`.
5. Click `Open Chat` to open the WebUI at `http://127.0.0.1:11434/`.
   If a model is still downloading, Pico AI Server shows a download-progress page until it is ready.
6. Use the menu extra when you need quick control afterward.
   When the server is running, it shows the status, a `Start` or `Stop` button, and an IP-based server address with a copy button.

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
  **Fix:** Finish setup by clicking `Start server` on the `Ready` step, or use the menu extra to start the server, then reload the page.
- **Symptom:** During setup, the `Ready` step reports that the server didn't respond and shows a `Try again` button.
  **Cause:** Another app may be using port `11434`, or the server didn't come up in time.
  **Fix:** Quit the app that is using the port (or change the port in Settings), then click `Try again`.
- **Symptom:** Another device on your LAN cannot connect.
  **Cause:** `Allow local network connections` is off, or the network blocks device-to-device traffic.
  **Fix:** Turn the setting on and test again from the other device.
- **Symptom:** The WebUI opens, but no model is usable.
  **Cause:** No model is available yet.
  **Fix:** Open the `Models` tab in the native app and wait for a model to become available.

## Next steps

- [Configure Settings](./configure-settings.md)
- [Use the WebUI](../webui/use-the-webui.md)
