---
title: Performance Dashboard
sidebar_position: 1
description: Open Pico AI Server's performance dashboard to watch live inference throughput, concurrency, context size, and memory, review request history, and control what is recorded.
---

Pico AI Server includes a **performance dashboard** that shows how the server is handling requests — both live and over time. It reports measured inference throughput, how many requests are running at once, context sizes, and MLX memory and GPU usage, and it keeps a history of completed requests so you can see trends.

The dashboard reads from telemetry the server records about each request. It records *how* requests ran — model, token counts, timing, and outcome — but **not** the prompt or response text. You can turn recording off, choose how long details are kept, and clear the history at any time.

## Open the dashboard

The dashboard is available while the server is running. From the Pico AI Server **menu bar** item:

- **Open Dashboard…** opens the dashboard in a native window.
- **Open Dashboard in Browser** opens the web dashboard at `http://127.0.0.1:11434/dashboard/` in your default browser. If you changed the server port, the URL uses that port instead.

Both surfaces show the same readings and the same metric calculations; use whichever you prefer. The browser version is also what a remote administrator sees when remote access is enabled (see [Remote access](#remote-access)).

## What the dashboard shows

The dashboard is organized into three pages:

- **Overview** — live charts, including generation and prompt‑processing throughput, request concurrency, total and largest logical context, and MLX memory and GPU usage. Peaks and live ranges are calculated on the server so every surface agrees.
- **History** — aggregated usage over a period, so you can compare models and spot trends.
- **Activity** — a table of recent requests with their timing and outcome.

You can narrow what you see with filters for the time **period**, **model**, **API format**, and **outcome**, or set a custom **From**/**To** range.

## What is recorded

Open **Settings → Dashboard** to control recording and access.

- **Record request history** (on by default) records models, token counts, timing, and outcomes. **Prompt and response text are not recorded.** Turn this off to stop recording new requests.
- **Keep request details** sets how long per‑request details are kept — **7**, **30**, or **90 days**. Shortening the retention removes older request details. Hourly usage totals are kept for one year regardless of this setting.
- **Clear Recorded History…** removes the recorded history.

## Verify it worked

A request only shows up if it is being recorded, so first confirm **Record request history** is on in **Settings → Dashboard**.

With the dashboard open, send one request to the server so there is something to display. From a terminal, replace `MODEL_NAME` with a model you have installed:

```bash
curl http://127.0.0.1:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

Then open the **Activity** page: the request you just sent appears as a new row with its model, timing, and a completed outcome. The **Overview** charts register its generation and prompt-processing throughput, and **History** folds it into the totals for the current period.

## Remote access

By default, the dashboard is only reachable from the Mac running Pico AI Server. A browser request is treated as the local owner only when it comes from the loopback address with a matching local origin; forwarded or proxy headers never grant local access.

To let an administrator open the dashboard from another device, turn on **Allow remote dashboard access** in **Settings → Dashboard**. Remote access is opt‑in and additionally requires:

- an **administrator API key**, and
- the server's **network access** to be enabled (see [LAN sharing basics](../networking/lan-sharing-basics.md)).

Remote access is deliberately independent of the inference API's authentication: enabling it exposes the dashboard and its exports, not your models. Dashboard responses are sent with no‑store caching and a self‑only content security policy.

## Export data

From the browser dashboard, the server can export request data as **JSONL** or **CSV** for your own analysis. Exports honor the same filters as the dashboard and are subject to the same access rules — a remote export requires an enabled administrator.

:::note Developer reference
The dashboard is backed by a small read‑only HTTP surface under `/api/dashboard/` (for example `snapshot`, `history`, `requests`, `activity`, and `export`). These endpoints serve the dashboard UI and share its access policy; they are not part of the inference API and are not intended as a stable integration point.
:::
