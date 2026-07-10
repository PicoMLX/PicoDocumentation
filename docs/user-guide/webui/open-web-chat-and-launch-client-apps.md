---
title: Open Web Chat and Launch Client Apps
sidebar_position: 2
---

<!-- Mode: Manual -->

Pico AI Server gives you two launch paths: the browser-based WebUI at the root URL, and the native app's `Open Chat Client` action. Use the browser when you want the built-in chat. Use `Open Chat Client` when you want Pico to launch another app or URL instead.

## What you'll do
- Open the built-in browser chat.
- Set the default launch target.
- Confirm the native app opens the client you expect.

## Before you start
- Pico AI Server must be running.
- The current built-in WebUI address is `http://127.0.0.1:11434/`.

## Do it
1. Open the built-in browser chat:

```bash
open http://127.0.0.1:11434/
```

2. Open the native app settings.
3. In `Web Chat`, find `Default Client`.
4. Choose one of the built-in launch targets:
   - `Pico Web Chat`
   - `Bolt AI`
   - `Open WebUI`
   - `Open WebUI on Docker`
5. If none of those fit, add a custom link with `Name` and `URL`, then save it.
6. Use the menu extra and choose `Open Chat Client`.

## Verify it worked
The chosen client opens when you use `Open Chat Client`. If `Pico Web Chat` is selected, the browser should open the built-in WebUI.

## Try it now

```bash
open http://127.0.0.1:11434/
```

Then switch `Default Client` in the native app and test `Open Chat Client` again.

## Troubleshooting
- **Symptom:** `Open Chat Client` opens the wrong destination.
  **Cause:** `Default Client` still points at another saved link.
  **Fix:** Change it in the native app settings and save the new selection.
- **Symptom:** A custom link does nothing.
  **Cause:** The URL is invalid or the target app is not installed.
  **Fix:** Re-enter the URL and test it directly first.
- **Symptom:** The WebUI behaves differently between browsers.
  **Cause:** WebUI settings are stored locally in browser storage.
  **Fix:** Recheck the settings dialog in the browser you are using.

## Next steps
- [Use the WebUI](./use-the-webui.md)
- [Connect a Client](../getting-started/connect-a-client.md)
