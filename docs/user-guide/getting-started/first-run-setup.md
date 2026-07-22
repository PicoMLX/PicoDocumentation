---
title: First-Run Setup
sidebar_position: 2
---

The first time you launch Pico AI Server, a setup wizard walks you through four pages — **Welcome**, **Model**, **Access**, and **Ready**. By the end you have chosen who can reach the server and the server is running; if you picked a model, it is downloading or already ready (you can also skip that step and add a model later). This page explains each page so you know what every choice does.

You can change every choice later in the app's Settings window, so pick sensible defaults now and move on.

## Walk through the wizard

1. Launch Pico AI Server.
2. On the **Welcome** page, review the summary and continue.
   This page introduces Pico AI Server and links to the privacy policy and terms.
3. On the **Model** page ("Choose your first model"), pick a model (or skip it), then continue.
   - Pico shows a short list of options — such as **Fast**, **Balanced**, and **Reasoning** — sized for your Mac's memory.
   - One selectable option is preselected and marked **Recommended** for this Mac; the page subtitle names it (for example, "Balanced is recommended for this Mac. You can add or switch models later.").
   - Each selectable option shows its model name and total download size. An option that isn't available yet is labeled **Coming soon**, and one that needs more memory than your Mac has shows its RAM requirement instead — neither can be selected.
   - For a selectable option, the continue button reflects your choice: **Download _tier_ · _size_** for a model that is not on disk yet, or **Use _tier_** for one you already have.
   - You can continue without choosing. If no model is available yet, Pico asks you to confirm, and you can download one later in Settings.
4. On the **Access** page ("Choose who can connect"), pick one option, then continue.
   - **This Mac only** — the most private choice. Only apps on this Mac can connect. Pico binds to `127.0.0.1`.
   - **Devices on my local network** — any device on your network can use Pico. Pico binds to `0.0.0.0`.
   - When you choose local-network access, a **Make Pico discoverable automatically** toggle appears. Turn it on to advertise the server over Bonjour so Pico clients and other Pico servers can find it without typing an address.
5. On the **Ready** page, review the live server details, then select **Open Chat**.
   - The page shows the real server state: a status dot, the model you chose (when you picked one), the access scope you chose, and the server address.
   - Select the copy button next to **Address** to copy the server address.
   - **Open Chat** finishes setup, applies your choices, and opens the browser chat. If a model download is still in progress, Pico opens a page that tracks the download instead.

After you finish, Pico stays in the menu bar. Use its icon to open chat, view memory, or change settings.

## Verify it worked

When the Ready page reports the server is running, confirm the API answers:

```bash
curl http://127.0.0.1:11434/v1/models
```

If you get a JSON response, the server is up. If you chose **Devices on my local network**, also ask the server for the address to share with other devices:

```bash
curl http://127.0.0.1:11434/ip
```

## Troubleshooting

- **Symptom:** The Model page lists fewer options than you expected.
  **Cause:** The available tiers depend on your Mac's memory; an 8 GB Mac is offered only the smallest tier.
  **Fix:** Choose an available tier now, then add larger models later from the `Models` tab in Settings.
- **Symptom:** A download fails during or after setup.
  **Cause:** A network interruption or an unreachable model repository.
  **Fix:** Pico shows a **Download Failed** alert. Dismiss it and start the download again from the `Models` tab in Settings.
- **Symptom:** The Ready page shows the server address, but another device cannot connect.
  **Cause:** You chose **This Mac only**, so the server is not exposed on the LAN.
  **Fix:** Reopen setup or open Settings and switch to **Devices on my local network**, then test again. See [LAN Sharing Basics](../networking/lan-sharing-basics.md).

## Next steps

- [Configure Settings](./configure-settings.md)
- [Connect a Client](./connect-a-client.md)
