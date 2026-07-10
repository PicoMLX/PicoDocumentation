---
title: Bonjour Discovery
sidebar_position: 3
---

Bonjour discovery lets Pico clients find Pico AI Server without typing a server address first. Pico AI Server advertises the service type `_pico._tcp.` and includes the IP address, port, local host name, and a stable server identifier in the TXT record.

Two things to know before you start: `Enable Bonjour broadcasting` only works when `Allow local network connections` is on, and discovery is optional — clients still need a manual server-address path.

## Turn on discovery and browse for the server

1. Open the native app settings.
2. Turn on `Allow local network connections`.
3. Turn on `Enable Bonjour broadcasting`.
4. Click `Apply Changes`.
5. Browse for Pico AI Server from a Mac:

   ```bash
   dns-sd -B _pico._tcp
   ```

   Leave it running for a few seconds. Pico AI Server should appear if discovery is enabled and the network allows multicast DNS.

6. When you find a service, resolve it to see the details:

   ```bash
   dns-sd -L "SERVICE_NAME" _pico._tcp local
   ```

   Replace `SERVICE_NAME` with the name reported by the browse command.

7. Build your client flow around these TXT record fields:
   - `IPAddress`
   - `Port`
   - `LocalHostName`
   - `ServerIdentifier`

## Verify it worked

You can see at least one `_pico._tcp` service and resolve it to a usable server address.

## Troubleshooting

- **Symptom:** No Pico AI Server instance appears.
  **Cause:** Bonjour discovery is off, or the network blocks multicast DNS.
  **Fix:** Turn discovery on and keep a manual server-address entry in the client.
- **Symptom:** Discovery works on one network but not another.
  **Cause:** Bonjour discovery is usually local-link only.
  **Fix:** Fall back to a copied server address on networks that do not forward mDNS.
- **Symptom:** The discovered host stops working later.
  **Cause:** The IP address may have changed.
  **Fix:** Re-resolve the service, or reconnect by `ServerIdentifier` if your client stores it.

:::caution
The admin can disable Bonjour discovery. Do not make it the only connection path.
:::

## Next steps

- [Hostnames, IP Addresses, and What to Copy](./hostnames-ip-addresses-and-what-to-copy.md)
- [Connect a Client](../getting-started/connect-a-client.md)
