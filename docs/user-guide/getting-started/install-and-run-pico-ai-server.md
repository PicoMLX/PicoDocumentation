---
title: Install and Run Pico AI Server
sidebar_position: 1
---

This page gets Pico AI Server running and proves the WebUI and API are alive. The goal is simple: start the server, open the browser chat, and confirm the default endpoint responds on port `11434`.

Pico AI Server is a macOS app for Apple Silicon Macs — it runs models with MLX, which requires an M-series chip, so Intel Macs are not supported. The default server port is `11434`.

## Start the server

1. Launch Pico AI Server.
2. Choose how you want to sign in.
   The setup wizard lets you create a personal account or continue without accounts, and it explains the difference between local-only and network access. If you create an account, enter your first name; a last name is optional.
   The first account you create becomes an **administrator**. You can change account roles later in **Settings**.
3. Invite other people (optional).
   During setup you can prepare invitations for several people at once. Pico creates a separate, personalized invitation for each person as an email draft; if a draft fails, you can retry it.
4. Set the server options you want.
   The onboarding flow can set `Allow local network connections`, `Broadcast Bonjour`, `Open at login`, and `Prevent sleep`.
5. Finish setup.
   The final page introduces the menu extra and summarizes the access and model you chose. Pico then opens the WebUI at `http://127.0.0.1:11434/` for you. If you created an account, the WebUI opens already signed in to it; if your browser is already signed in to a different account, that session is kept. The handoff still works while a model is finishing its download.
6. If you want LAN access, leave `Allow local network connections` on.
   With that setting on, Pico AI Server binds to `0.0.0.0`.
7. If you want local-only access, turn `Allow local network connections` off in the native app settings.
   With that setting off, Pico AI Server binds to `127.0.0.1`.
8. Use the menu extra when you need quick control.
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
  **Fix:** Use the native app or the menu extra to start the server, then reload the page.
- **Symptom:** Another device on your LAN cannot connect.
  **Cause:** `Allow local network connections` is off, or the network blocks device-to-device traffic.
  **Fix:** Turn the setting on and test again from the other device.
- **Symptom:** The WebUI opens, but no model is usable.
  **Cause:** No model is available yet.
  **Fix:** Open the `Models` tab in the native app and wait for a model to become available.
- **Symptom:** Setup reports that the server could not start.
  **Cause:** Pico AI Server could not bind its port.
  **Fix:** Use the retry option on the startup page. Before it continues, Pico verifies that this instance actually bound the port. If it keeps failing, make sure no other app — or another copy of Pico AI Server — is already using port `11434`.

## Next steps

- [Configure Settings](./configure-settings.md)
- [Use the WebUI](../webui/use-the-webui.md)
