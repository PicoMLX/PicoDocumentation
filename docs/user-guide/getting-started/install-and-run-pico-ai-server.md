---
title: Install and Run Pico AI Server
sidebar_position: 1
---

This page gets Pico AI Server running and proves the WebUI and API are alive. The goal is simple: start the server, open the browser chat, and confirm the default endpoint responds on port `11434`.

Pico AI Server is a macOS app for Apple Silicon Macs — it runs models with MLX, which requires an M-series chip, so Intel Macs are not supported. The default server port is `11434`.

## Start the server

1. Launch Pico AI Server.
2. Complete the first-run flow.
   Onboarding walks through four steps — **Welcome**, **Model**, **Access**, and **Ready**:
   - **Model** recommends a model for this Mac based on its memory and preselects it. Continue to download the recommended model, pick a different one, or skip and add a model later in the `Models` tab. A download keeps running in the background while you finish the remaining steps.
   - **Access** asks who can connect: `This Mac only` (local-only) or `Devices on my local network` (LAN). When you allow local-network access, you can also turn on Bonjour so other devices discover Pico automatically.
   - **Ready** shows the running server's live status, the selected model, the access choice, and the server address with a copy button.

   Onboarding does not set `Open at login` or `Prevent sleep` — change those later in the native app settings.
3. Open the WebUI at `http://127.0.0.1:11434/`.
   The onboarding flow normally opens this address for you after setup. If a model is still downloading when you finish, it opens a download-progress page first.
4. If you want LAN access, choose `Devices on my local network` (or leave `Allow local network connections` on in settings).
   With that setting on, Pico AI Server binds to `0.0.0.0`.
5. If you want local-only access, choose `This Mac only` (or turn `Allow local network connections` off in the native app settings).
   With that setting off, Pico AI Server binds to `127.0.0.1`.
6. Use the menu extra when you need quick control.
   When the server is running, it shows the status, a `Start` or `Stop` button, and an IP-based server address with a copy button. It also shows a `Memory` section with an Apps / MLX / Free usage bar and a memory-pressure indicator, plus a `Models in Memory` list of loaded models.

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
