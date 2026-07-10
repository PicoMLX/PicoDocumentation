---
title: Hostnames, IP Addresses, and What to Copy
sidebar_position: 2
---

Use this page when you need a stable server address for another person or another app. Pico AI Server exposes helper endpoints for both host name and IP address, and the menu extra copies an IP-based server address by default.

Pico AI Server must be running. If you are sharing to another device, LAN Mode must be on.

## Choose an address to share

1. Query the current host name:

   ```bash
   curl http://127.0.0.1:11434/hostname
   ```

2. Query the current IP address:

   ```bash
   curl http://127.0.0.1:11434/ip
   ```

3. Compare both values, then decide which one to share:
   - Prefer a host name when your clients resolve local names reliably.
   - Prefer the IP-based server address when you need the least surprising copy-and-paste result. The menu extra copy button uses an IP-based address.
4. When you share the address, include the scheme and port, for example `http://192.168.x.y:11434`.

## Verify it worked

Use the address you chose from another device:

```bash
curl http://SERVER:11434/v1/models
```

Replace `SERVER` with the address you shared. If it returns JSON, the chosen server address is good enough for client setup.

## Troubleshooting

- **Symptom:** The host name changes or does not resolve.
  **Cause:** Local name resolution depends on Bonjour discovery and the client network.
  **Fix:** Share the IP-based server address instead.
- **Symptom:** The IP address changes after a router restart.
  **Cause:** DHCP assigned a new address.
  **Fix:** Update the shared server address, or make the address stable in your network infrastructure.
- **Symptom:** The copied server address works inside your home, but not elsewhere.
  **Cause:** The address is only valid on that LAN.
  **Fix:** Treat it as a LAN address, not a public internet address.

## Next steps

- [Bonjour Discovery](./bonjour-discovery.md)
- [Connect a Client](../getting-started/connect-a-client.md)
