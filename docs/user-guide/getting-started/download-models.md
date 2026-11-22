---
title: Download Models
sidebar_position: 4
---

Pico AI Server downloads models onto your Mac. The first-run flow offers a recommended set, and a Downloads window shows progress for anything you add later. The goal here is simple: install a chat model and confirm the server lists it on port `11434`.

## Download a model during setup

1. Launch Pico AI Server and continue the first-run flow to the model step.
   Setup offers a recommended chat model and a 363 MB ColBERT tool retrieval model together. Each entry shows its purpose, its size, and whether it is already installed.
2. Choose how much to download:
   - Download both to get the recommended chat model and the ColBERT retrieval model.
   - Skip to continue without downloading now.
   - Open the model browser to choose a different chat model instead.
   Only models you do not already have count toward the download total.
3. Continue. Chat becomes available as soon as its chat model finishes — you do not have to wait for every download.

ColBERT is registered as an embedding model used for tool retrieval, so it is not offered as a chat default.

## Watch and manage downloads

When a download starts — during setup or later from Settings — a compact Downloads window opens in the upper-right corner and shows each model's progress.

1. Reopen the Downloads window at any time from the `Window` menu, or from the menu extra.
2. Leave downloads running in the background. Closing the Downloads window does not stop them.
3. Expect up to two downloads at once. Setup and Settings share two download slots. Further models show `Queued` and start in order as a slot frees up.
4. Cancel a download with the cancel button on its row:
   - Canceling a `Queued` row removes it immediately.
   - Canceling an active transfer stops its network request but keeps the partial files, so a later retry can continue from them. Other downloads keep going.

## Verify it worked

After a chat model finishes downloading, confirm the server lists it:

```bash
curl http://127.0.0.1:11434/v1/models
```

The model you downloaded should appear in the JSON response. These endpoints only list installed models; they do not download anything (see [Models API](../../reference/models/models-api.md)).

## Troubleshooting

- **Symptom:** A download stays at `Queued` and does not start.
  **Cause:** Two other downloads already hold the two available slots.
  **Fix:** Wait for one to finish, or cancel it; the queued model starts when a slot frees up.
- **Symptom:** A transfer failed partway and you want to try again.
  **Cause:** The network request was canceled or interrupted.
  **Fix:** Start the download again. Pico keeps the partial files from a canceled active transfer and continues from them.
- **Symptom:** The WebUI opens, but no model is usable.
  **Cause:** No chat model has finished downloading yet.
  **Fix:** Open the Downloads window from the `Window` menu to check progress, or download a chat model from the `Models` tab in the native app.

## Next steps

- [Configure Settings](./configure-settings.md)
- [Connect a Client](./connect-a-client.md)
