---
title: Use the Menu Bar Menu
sidebar_position: 4
---

Pico AI Server runs as a menu bar app. The menu bar menu is the quickest way to check status and reach the common commands. This page covers what the menu shows and how to drive it.

## Open the menu

You can open and use the menu two ways:

- Click the Pico AI Server icon in the macOS menu bar to open the menu and keep it open, then click a command.
- Or press and hold the icon, slide down to a command, and release to run it.

The menu behaves like any standard macOS menu, so you can also move through it with the arrow keys and run the highlighted command with Return.

## Status at the top

The top of the menu shows a live status area. While the server is running it shows the status, a `Start` or `Stop` button, and an IP-based server address with a copy button. The status area keeps refreshing while the menu is open. If it is taller than your screen it scrolls, and the commands below it stay in place, so a command never moves out from under the pointer while you are reaching for it.

## Commands

Below the status area are the menu commands:

- **Open Pico Web Chat** — opens Pico's built-in web chat in your browser. Available only while the server is running.
- **Documentation** — `⌘⇧?` — opens the online documentation. Hold Option to switch this command to **Open Discord**.
- **Settings…** — `⌘,` — opens the app settings. Hold Option to switch this command to **Setup Wizard…**.
- **Quit Pico AI Server** — `⌘Q` — quits the app.

Commands that have a keyboard shortcut show it next to the command name. While the menu is open you can run any command by clicking it or by sliding to it and releasing; commands that list a shortcut can also be run by pressing that shortcut.

## Verify it worked

With the server running, open the menu and choose **Open Pico Web Chat**. Your browser opens Pico's built-in web chat at `http://localhost:11434/` (the default server port).

To confirm that address independently, open the same URL yourself:

```bash
open http://localhost:11434/
```

If the web chat loads in both cases, the menu command is working.

## Troubleshooting

- **Symptom:** **Open Pico Web Chat** is dimmed and cannot be chosen.
  **Cause:** The server is not running.
  **Fix:** Use the `Start` button in the menu's status area (or start the server in the app), then reopen the menu and choose the command again.

## Next steps

- [Install and Run Pico AI Server](./install-and-run-pico-ai-server.md)
- [Connect a Client](./connect-a-client.md)
- [Use the WebUI](../webui/use-the-webui.md)
