---
title: LAN Sharing Basics
sidebar_position: 1
---

<!-- Mode: Manual -->

LAN Mode is controlled by the `Allow local network connections` setting in the native app. When that setting is on, Pico AI Server listens on every interface. When it is off, only the local Mac can connect.

## What you'll do
- Turn LAN Mode on when you need sharing.
- Test the server from another device.
- Rule out the common network mistakes first.

## Before you start
- The default port is `11434`.
- A client on another device needs a routed path to the host Mac.

## Do it
1. Open the native app settings.
2. Turn on `Allow local network connections`.
3. Click `Apply Changes`.
4. Copy the server address from the menu extra, or query it with:

```bash
curl http://127.0.0.1:11434/ip
```

5. From another device on the same network, test:

```bash
curl http://SERVER:11434/v1/models
```

6. If that works, your LAN path is good enough for client setup.

## Verify it worked
The second device gets a JSON response from `GET /v1/models`.

## Try it now

```bash
curl http://SERVER:11434/
```

From another device, this should load the WebUI in a browser.

## Troubleshooting
- **Symptom:** The host Mac works, but another device cannot connect at all.
  **Cause:** LAN Mode is off, or the other device is not on a routed network path to the host.
  **Fix:** Turn LAN Mode on and test again on the same Wi-Fi or wired LAN first.
- **Symptom:** Devices on a guest network cannot see the server.
  **Cause:** Guest networks often block device-to-device traffic.
  **Fix:** Move both devices to the main LAN, or use a manually routed network.
- **Symptom:** Devices on different VLANs cannot connect.
  **Cause:** Inter-VLAN routing or firewall rules may block the port.
  **Fix:** Verify that TCP `11434` is allowed from the client network to the host Mac.

## Next steps
- [Hostnames, IP Addresses, and What to Copy](./hostnames-ip-addresses-and-what-to-copy.md)
- [Bonjour Discovery](./bonjour-discovery.md)
