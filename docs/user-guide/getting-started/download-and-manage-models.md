---
title: Download and Manage Models
sidebar_position: 3
---

Use this page to pick a language model, download it, and confirm Pico AI Server can serve it. Pico AI Server ships with a built-in catalog, so you choose a model from the app rather than downloading files by hand. The job is simple: open the `Models` screen, download a model that fits your Mac, and prove it appears at the API.

The `Models` screen appears in two places: during the first-run onboarding flow, and any time afterward in the native app settings. Both show the same screen, so the steps below apply either way.

## Pick a model

1. Open the native app settings and select `Models` (or reach the same screen from the onboarding flow).
2. Choose a tab at the top of the screen:
   - `Recommended` — the default tab. It lists curated models whose current build fits this Mac.
   - `All Models` — the full catalog.
   - `On This Mac` — models already downloaded or partially downloaded. On iPhone and iPad this tab is named `On This Device`.
3. Read the line under the tabs to see how much room you have.
   It shows this Mac's total RAM and the free disk space, so you can judge what a model needs before you download it.
4. Download a suggested model from `Recommended`.
   Each family shows a `Suggested download` matched to your Mac. Select it and click `Download`.

The `Recommended` tab only offers a model when the catalog carries a curated recommendation for it and a current build fits this Mac. If nothing recommended fits, use `All Models` and let the guided chooser suggest a smaller format.

## Choose a specific variant

Use this when you want a particular release, size, or quantization instead of the suggested download.

1. Open `All Models` and find the family you want.
   Use `Search models or tags` to narrow the list, or click `Filters` to filter by capability, publisher region, and more.
2. Click `Choose variant…` on the family.
3. Pick the options you want on the variant page:
   - `Release` — the model release. Superseded releases are marked `(older)`.
   - `Model size` — the parameter size, when a family offers more than one.
   - `Download format` — the quantization or file format for that size.
4. Check the compatibility note before downloading.
   The page shows `N GB recommended unified memory` for a build that fits, or `Insufficient disk space` or `Exceeds available memory` when it does not.
5. Click `Download`.
   Your search and selection are preserved if you go back to the list and return.

To read more about a model before downloading, click `Model card`. It opens the model's repository on the configured hub.

## Resume or remove a download

1. Open `On This Mac` (or `On This Device`).
   A build that stopped partway shows `Partially downloaded`.
2. Click `Resume` to finish a partial download, or `Retry` on a build that shows `Failed`.
   Use `Stop` to halt a download that is in progress.
3. To delete a build, open its variant page and click `Remove download…`.

A model you linked from LM Studio appears here marked `Linked from LM Studio`. These are read-only: Pico AI Server can serve them, but you manage the files in LM Studio, so there is no `Remove download…` for them.

## Add a model Pico does not list

1. Click `Add a Model` (the `+` button) at the top of the screen.
2. Choose how to add it:
   - `Add Model from Disk…` — point Pico at a local MLX model folder.
   - `Add Model from URL…` — paste a model repository URL.

## Verify it worked

After a download finishes, the model appears under `On This Mac` and is served at the API. Confirm it with:

```bash
curl http://127.0.0.1:11434/v1/models
```

The downloaded model's ID should appear in the JSON response. If it does, any connected client can select it.

## Troubleshooting

- **Symptom:** A model you want is greyed out or shows `Exceeds available memory or storage`.
  **Cause:** The build is too large for this Mac's memory or free disk.
  **Fix:** Use `Choose variant…` and pick a smaller size or a more compressed `Download format`, or free up disk space.
- **Symptom:** The `Recommended` tab is empty.
  **Cause:** No curated build currently fits this Mac.
  **Fix:** Switch to `All Models` and download a suggested or smaller variant instead.
- **Symptom:** A download stops before it finishes.
  **Cause:** The transfer was interrupted.
  **Fix:** Open `On This Mac`, find the `Partially downloaded` build, and click `Resume`.
- **Symptom:** `curl /v1/models` does not list the model you downloaded.
  **Cause:** The download is still in progress, or the server has not refreshed.
  **Fix:** Wait for the download to finish in `On This Mac`, then run the command again.

## Next steps

- [Connect a Client](./connect-a-client.md)
- [Configure Settings](./configure-settings.md)
- [Models API](../../reference/models/models-api.md)
