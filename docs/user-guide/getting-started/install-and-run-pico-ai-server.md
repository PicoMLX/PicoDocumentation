---
title: Install and Run Pico AI Server
sidebar_position: 1
---

<!-- Mode: Manual -->

This page gets Pico AI Server running and proves the WebUI and API are alive. The goal is simple: start the server, open the browser chat, and confirm the default endpoint responds on port `11434`.

## What you'll do
- Launch Pico AI Server.
- Finish the first-run flow.
- Open the WebUI.
- Confirm the API is listening.

## Before you start
- Pico AI Server is a macOS app.
- The default server port in the current source is `11434`.

## Do it
1. Launch Pico AI Server.
2. Complete the first-run flow.
   The onboarding flow can set `Allow local network connections`, `Broadcast Bonjour`, `Open at login`, and `Prevent sleep`.
3. Open the WebUI at `http://127.0.0.1:11434/`.
   The onboarding flow normally opens this address for you after setup.
4. If you want LAN access, leave `Allow local network connections` on.
   With that setting on, Pico AI Server binds to `0.0.0.0`.
5. If you want local-only access, turn `Allow local network connections` off in the native app settings.
   With that setting off, Pico AI Server binds to `127.0.0.1`.
6. Use the menu extra when you need quick control.
   When the server is running, it shows the status, a `Start` or `Stop` button, and an IP-based server address with a copy button.

## Verify it worked
Run:

```bash
curl http://127.0.0.1:11434/v1/models
```

If you get a JSON response, the server is up. If you also open `http://127.0.0.1:11434/`, the WebUI should load in your browser.

## Try it now

```bash
curl http://127.0.0.1:11434/hostname
```

This returns the current host name that Pico AI Server sees on the Mac.

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
