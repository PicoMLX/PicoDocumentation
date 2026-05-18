---
title: Discover Servers with Bonjour
description: Discover Pico AI Server instances on the local network with Bonjour (mDNS) so clients connect without typing a host name.
sidebar_position: 7
---

<!-- Mode: Manual -->

## Understand Bonjour discovery

Pico AI Server can advertise itself on the local network using Bonjour (mDNS).
Your client can scan for these broadcasts and offer a pick list instead of asking
for a host name and port up front.

## What you will do
- Scan the local network for Pico AI Server instances
- Show a list of servers to the user
- Connect using the server's host name or IP address

## Before you start
- Pico AI Server 1.1.1 (build 29) or newer
- Bonjour discovery enabled in Pico AI Server settings

## Discover servers
1. Start a Bonjour browse for the service name `_pico._tcp`.
2. Build a list of discovered services and display the human-readable instance name.
3. When the user selects a server, read its host name, IP address, and port.
4. Store the selection and reconnect automatically on future launches.

## Verify it worked
- You can see at least one Pico AI Server instance in your list.
- You can connect without typing a host name or IP address.

> **Try it now**  
> On macOS, run this and look for Pico AI Server instances in the output:
> ```bash
> dns-sd -B _pico._tcp
> ```

## Troubleshoot discovery
- **No servers appear:** Bonjour may be disabled on the server. **Fix:** enable
  discovery in Pico AI Server settings or provide manual host entry.
- **Only one server appears on a busy LAN:** the client may be caching results.
  **Fix:** clear the cached list and rescan.
- **Connect succeeds once, then fails later:** IP addresses can change. **Fix:**
  prefer the local host name over the IP address.

## Review TXT record fields
Pico AI Server advertises the `_pico._tcp` service and includes a TXT record with
these fields:

| Field            | Type   | Meaning |
| ---              | ---    | --- |
| `IPAddress`      | String | IP address of the server |
| `Port`           | String | Server port |
| `LocalHostName`  | String | Local host name, for example `ronalds-macbook.local` |
| `ServerIdentifier` | String | Stable UUID for the server instance |

:::caution
The Pico AI Server admin can disable Bonjour discovery. If Bonjour traffic is
blocked or not routed on your network, discovery will fail. Always provide a
manual host name or IP address entry as a fallback.
:::

## Next steps
- Save the chosen server's `ServerIdentifier` so you can reconnect after IP changes.
