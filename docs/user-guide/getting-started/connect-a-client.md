---
title: Connect a Client
sidebar_position: 4
---

Use this page when another app needs to talk to Pico AI Server. The job is to copy the right server address, choose the correct compatibility layer, and prove the client can list models before you try chat.

Pico AI Server must be running. For another device on your LAN, `Allow local network connections` must also be on.

## Connect the client

1. Get the server address.
   The menu extra shows an IP-based server address and offers a copy button while the server is running.
2. If you need to look it up by API, use one of these helpers:

   ```bash
   curl http://127.0.0.1:11434/hostname
   curl http://127.0.0.1:11434/ip
   ```

3. Choose the base URL your client expects:
   - OpenAI-compatible client: `http://SERVER:11434/v1`
   - OpenResponses client: `http://SERVER:11434/v1`
   - Ollama-compatible client: `http://SERVER:11434`
   - Browser chat: `http://SERVER:11434/`

   Replace `SERVER` with the host name or IP address you plan to share.

4. Test the connection before you send chat:

   ```bash
   curl http://SERVER:11434/v1/models
   ```

5. If the list loads, move on to chat or responses.

## Verify it worked

Your client can reach `GET /v1/models` and receives JSON. If the list is empty, the connection still worked; it only means no model is available yet.

## Troubleshooting

- **Symptom:** The client works with `127.0.0.1` but not from another device.
  **Cause:** You are still using a local-only address.
  **Fix:** Use the LAN server address from the host Mac.
- **Symptom:** A `.local` host name works on one device but not another.
  **Cause:** Bonjour discovery or mDNS resolution is not working on that client network.
  **Fix:** Fall back to the IP-based server address.
- **Symptom:** The client reaches the server but chat requests fail with model errors.
  **Cause:** The requested model is not available.
  **Fix:** List models first and use one of the returned IDs.

## Next steps

- [Hostnames, IP Addresses, and What to Copy](../networking/hostnames-ip-addresses-and-what-to-copy.md)
- [Chat API](../../reference/chat/chat-api.md)
