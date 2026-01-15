---
title: Custom URL Scheme
sidebar_position: 2
---

Mode: Manual

## Overview
Pico AI Server can launch a chat app from WebUI using a custom URL scheme.
This lets users jump from WebUI to their preferred client without copying the
server address.

## What you will do
- Set a custom URL scheme in WebUI
- Open your chat app from the "Open Web Chat" menu

## Before you start
- Your chat app supports a custom URL scheme (for example, `yourapp://`)
- WebUI is accessible from your browser

## Set the URL scheme
1. Open WebUI.
2. Go to Settings.
3. Find the chat app URL scheme field. TODO: confirm the field label.
4. Enter your scheme, for example `yourapp://`.
5. Save the setting.

## Verify it worked
- The "Open Web Chat" menu item opens your chat app. TODO: confirm menu label.

> **Try it now**  
> On macOS, replace `yourapp` with your scheme and run:
> ```bash
> open "yourapp://"
> ```

## Troubleshoot launch issues
- **Symptom:** The app does not open. **Cause:** The URL scheme is not registered.
  **Fix:** Confirm your app registers the scheme and try again.
- **Symptom:** The wrong app opens. **Cause:** Another app registered the same
  scheme. **Fix:** Change your scheme to a unique value.
- **Symptom:** The menu item does nothing. **Cause:** The scheme field is empty
  or invalid. **Fix:** Re-enter the scheme in WebUI settings.

## Next steps
- If you are a chat app developer and want your app listed, contact the Pico
  team. TODO: confirm the current request channel.
