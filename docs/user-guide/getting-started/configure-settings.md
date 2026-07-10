---
title: Configure Settings
sidebar_position: 2
---

Use this page to set the storage location, network behavior, and browser-chat defaults. Keep the changes small, apply them, and prove the server still responds before you move on.

Before you start, open the native Pico AI Server app and keep a terminal ready so you can test with `curl` after each network change.

## Change the settings

1. Open the native app settings.
2. In `Model Library`, check `Location`.
   Pico stores language models under `<base>/models/` and embedding models under `<base>/models/embeddings/`.
3. Use `Change…` if you want to move the whole library to another folder or drive.
   Pico moves the existing model library to the new base location.
4. In `Web Chat`, set the `Default model` and `Default Client` if you want a predictable launch target.
5. In `HTTP Server`, review these fields:
   - `Server name`
   - `Serve Pico web chat`
   - `Allow local network connections`
   - `Port`
   - `Allow Cross-Origin Resource Sharing (CORS)`
   - `Enable Bonjour broadcasting`
6. Click `Apply Changes` after network or port changes.
   The app saves the configuration and restarts the server.

## Verify it worked

Run:

```bash
curl http://127.0.0.1:11434/v1/models
```

If you changed the port, use the new port instead. You should still get JSON back after `Apply Changes`.

If you plan to test from another device on the same LAN, get the address to use:

```bash
curl http://127.0.0.1:11434/ip
```

## Troubleshooting

- **Symptom:** The WebUI stops working after you turn on `Allow Cross-Origin Resource Sharing (CORS)`.
  **Cause:** CORS can prevent the browser chat from working; the settings UI warns about this.
  **Fix:** Turn CORS back off unless you need it for a separate client.
- **Symptom:** The server no longer answers on the old port.
  **Cause:** You changed `Port` and applied the change.
  **Fix:** Use the new server address everywhere.
- **Symptom:** You turn off `Serve Pico web chat`, but the browser chat still appears at the root URL.
  **Cause:** In the current build, the root WebUI is still served regardless of this setting.
  **Fix:** Treat the toggle as under validation and test the root URL directly before you rely on it.

## Next steps

- [Connect a Client](./connect-a-client.md)
- [LAN Sharing Basics](../networking/lan-sharing-basics.md)
