---
title: Tour the Menu Bar
sidebar_position: 2
---

Pico AI Server lives in the macOS menu bar. Clicking its icon opens a panel that is the fastest way to check the server, watch memory, see which models are loaded, and reach settings. This page walks through each section so you can read the panel at a glance.

Pico AI Server must be installed and its icon visible in the menu bar. If you just finished the setup wizard, the icon is already there.

## Open the menu bar panel

1. Click the Pico icon in the macOS menu bar.
2. Read the sections from top to bottom:
   - **Server status** — a colored dot and a label (`Server Running`, `Server Stopped`, `Starting…`, or `Server Error`), with a `Start` or `Stop` button. While the server runs, the panel also shows the LAN server address with a copy button.
   - **Memory** — a segmented bar that splits memory into `Apps`, `MLX` (memory used by loaded models), and `Free`. Click the `GB` / `%` control in the section header to switch the legend between gigabytes and percentages; Pico remembers your choice. A `Pressure` row reads `Stable`, `Elevated`, or `High`.
   - **Models in Memory** — each model currently held in memory, with its state (`Loading`, `Active`, or `Idle`). Idle models show a trash button to remove them from memory, and `Clear All` unloads every idle model at once. When nothing is loaded, this reads `No models loaded`.
   - **Downloads** — appears only while a model is downloading, showing a per-model progress bar.
3. Use the actions at the bottom of the panel:
   - `Open Pico Web Chat` opens the browser chat (available only while the server runs).
   - `Documentation` opens Pico's documentation, and `Settings…` (⌘,) opens the native settings window.
   - Hold `Option` to reveal `Setup Wizard…` in place of `Settings…`, and `Open Discord` in place of `Documentation`.
   - `Quit Pico AI Server` (⌘Q) quits the app.

## Verify it worked

The status dot matches the server. With the server running, the dot is green and the API answers:

```bash
curl http://127.0.0.1:11434/v1/models
```

Send a chat request to load a model, then reopen the panel: the model appears under `Models in Memory`, and the `MLX` share of the memory bar grows.

## Troubleshooting

- **Symptom:** The `Open Pico Web Chat` action is greyed out.
  **Cause:** The server is not running.
  **Fix:** Press `Start` in the `Server status` section, then try again.
- **Symptom:** `Models in Memory` says `No models loaded` even though a model is installed.
  **Cause:** Installed models load on first use; nothing is held in memory until a request arrives.
  **Fix:** Send a chat request, then reopen the panel.
- **Symptom:** The memory legend shows percentages when you want gigabytes (or the reverse).
  **Cause:** The `GB` / `%` toggle is set to the other unit.
  **Fix:** Click `GB` / `%` in the `Memory` header to switch it back.

## Next steps

- [Configure Settings](./configure-settings.md)
- [Use the WebUI](../webui/use-the-webui.md)
