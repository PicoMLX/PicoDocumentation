---
title: Access Pico AI Server Remotely with Tailscale
sidebar_position: 10
---

Mode: Manual

## Overview
Use Tailscale to reach your Pico AI Server from anywhere. This makes the WebUI
and API available over your private Tailnet so you can use your personal AI
outside your home network.

## What you will do
- Install and sign in to Tailscale on the server and your client device
- Connect to Pico AI Server using the Tailscale address
- Confirm WebUI and API access

## Before you start
- Pico AI Server is running
- A Tailscale account is available for your devices

## Set up Tailscale
1. Install Tailscale on the computer running Pico AI Server.
2. Sign in to Tailscale on that computer.
3. Install Tailscale on your client device.
4. Sign in to Tailscale on your client device.

## Find the Tailscale address
1. Open Tailscale on the server.
2. Copy the server's Tailscale IP address or MagicDNS name.

## Connect from your client device
1. Open a browser on your client device.
2. Go to `http://<tailscale-ip>:11434`. TODO: confirm WebUI path if different.
3. Confirm the WebUI loads.

## Verify it worked
- WebUI loads over your Tailscale address.
- API requests succeed from your client device.

> **Try it now**  
> From your client device, run:
> ```bash
> curl http://<tailscale-ip>:11434/v1/models
> ```

## Troubleshooting
- **Symptom:** Page does not load. **Cause:** Pico AI Server is not running.
  **Fix:** Start Pico AI Server and try again.
- **Symptom:** Connection times out. **Cause:** Devices are not in the same
  Tailnet. **Fix:** Sign in to the same Tailscale account on both devices.
- **Symptom:** API calls fail. **Cause:** Wrong port or address. **Fix:** Use
  the server's Tailscale IP and port `11434`.
