---
title: Configure Settings
sidebar_position: 2
---

<!-- Mode: Manual -->

Use this page to set the storage location, network behaviour, and browser-chat defaults. Keep the changes small, apply them, and prove the server still responds before you move on.

## What you'll do
- Check the model library location.
- Set browser-chat defaults.
- Review the HTTP Server settings.
- Apply changes safely.

## Before you start
- Open the native Pico AI Server app.
- Keep a terminal ready so you can test `curl` after each network change.

## Do it
1. Open the native app settings.
2. In `Model Library`, check `Location`.
   Pico stores language models under `<base>/models/` and embedding models under `<base>/models/embeddings/`.
3. Use `Change…` if you want to move the whole library to another folder or drive.
   The source says Pico moves the existing model library to the new base location.
4. In `Web Chat`, set the `Default model` and `Default Client` if you want a predictable launch target.
5. In `HTTP Server`, review these fields:
   - `Server name`
   - `Serve Pico web chat`
   - `Allow local network connections`
   - `Port`
   - `Allow Cross-Origin Resource Sharing (CORS)`
   - `Enable Bonjour broadcasting`
6. Click `Apply Changes` after network or port changes.
   The current app saves the configuration and restarts the server.

## Verify it worked
Run:

```bash
curl http://127.0.0.1:11434/v1/models
```

If you changed the port, use the new port instead. You should still get JSON back after `Apply Changes`.

## Try it now

```bash
curl http://127.0.0.1:11434/ip
```

Use the returned address when you test from another device on the same LAN.

## Troubleshooting
- **Symptom:** The WebUI stops working after you turn on `Allow Cross-Origin Resource Sharing (CORS)`.
  **Cause:** The server source explicitly warns that CORS can prevent the browser chat from working.
  **Fix:** Turn CORS back off unless you need it for a separate client.
- **Symptom:** The server no longer answers on the old port.
  **Cause:** You changed `Port` and applied the change.
  **Fix:** Use the new server address everywhere.
- **Symptom:** You expect `Serve Pico web chat` to hide the root WebUI, but the browser chat still appears.
  **Cause:** TODO: the current source passes this setting into server startup, but the static file middleware is still installed unconditionally.
  **Fix:** Treat this switch as under validation and test the root URL directly before documenting policy around it.

## Next steps
- [Connect a Client](./connect-a-client.md)
- [LAN Sharing Basics](../networking/lan-sharing-basics.md)
