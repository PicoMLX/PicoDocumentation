---
title: Custom URL Scheme
sidebar_position: 10
---

Mode: Reference

## Summary
Register your chat app's custom URL scheme so Pico AI Server can launch it from
the **Open Chat Client** menu item.

## Where this appears
The **Open Chat Client** menu item lives in Pico AI Server. It defaults to the
included Pico WebUI. Admins can switch it to a custom URL scheme to open a
different chat client.

## Custom URL scheme format
Use your app's registered URL scheme, for example:
- `boltai://`
- `my-chatapp://`

## Default behavior
If no custom scheme is set, **Open Chat Client** opens the Pico WebUI at the
local server address (for example `http://127.0.0.1:11434`).

## Examples
Example values for the custom scheme field:
- `boltai://`
- `my-chatapp://`

Example behavior:
- `boltai://` opens Bolt AI.
- `my-chatapp://` opens your app.

## Errors
No errors are returned to the app. Failures happen on the user's device.

## Edge cases
- If the scheme is unregistered, the OS does nothing.
- If two apps register the same scheme, the OS opens one of them.
