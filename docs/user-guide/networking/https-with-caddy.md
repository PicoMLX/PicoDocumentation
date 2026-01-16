---
title: Add HTTPS with Caddy
sidebar_position: 9
---

Mode: Manual

## Overview
Run Pico AI Server over HTTPS on your local machine so browser tools can call
the API without mixed-content errors.

## What you will do
- Install Caddy
- Lock Pico AI Server to localhost
- Proxy HTTPS to Pico AI Server
- Trust the local certificate

## Before you start
- Pico AI Server is running
- Homebrew is installed: https://brew.sh/

## Install Caddy
1. Run:
   ```bash
   brew install caddy
   ```

## Lock Pico AI Server to localhost
1. Open Pico AI Server.
2. Go to Settings > Server. TODO: confirm the exact menu labels.
3. Disable **Enable LAN access** (LAN Mode).
4. Note the server port (default is `11434`).

## Create a Caddyfile
1. Create a file named `Caddyfile` in your working folder.
2. Paste:
   ```caddyfile
   https://localhost, https://<your-hostname>.local, https://<ip-address (192.168.x.y)> {
       reverse_proxy 127.0.0.1:11434
       tls internal
   }
   ```
3. If you changed the Pico AI Server port, update the `reverse_proxy` line.

## Trust Caddy's local certificate
1. Run:
   ```bash
   caddy trust
   ```
2. Enter your macOS password when prompted.

## Run Caddy
1. Run:
   ```bash
   caddy run
   ```

## Verify it worked
- Open `https://localhost` in your browser and confirm the certificate is valid.
- Run:
  ```bash
  curl https://localhost/v1/models
  ```
  Look for a JSON response.

> **Try it now**  
> Call the API over HTTPS:
> ```bash
> curl https://localhost/v1/models
> ```

## Troubleshooting
- **Symptom:** Browser shows a certificate warning. **Cause:** The Caddy CA is
  not trusted. **Fix:** Run `caddy trust` again.
- **Symptom:** `curl` returns connection refused. **Cause:** Caddy is not
  running. **Fix:** Run `caddy run` in the folder with your `Caddyfile`.
- **Symptom:** `curl` returns 502. **Cause:** Pico AI Server is not running or
  the port is wrong. **Fix:** Start Pico AI Server and confirm the port.
- **Symptom:** `https://127.0.0.1` fails. **Cause:** The Caddyfile only serves
  `https://localhost`. **Fix:** Use `https://localhost` or add a second site
  block for `https://127.0.0.1`.

## Next steps
- Update your client base URL to `https://localhost`.
