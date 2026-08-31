---
title: Monitor Inference Activity
sidebar_position: 1
description: Read the menu extra's Inference section to see which models are resident, whether they are batching or running single stream, and live per-request throughput.
---

Pico AI Server's menu extra shows a live **Inference** section so you can see what the engine is doing right now — which models are loaded, how requests are being scheduled, and how fast each one is generating. This is the quickest way to confirm the server is serving traffic and to spot when requests are queuing up.

Open the menu extra from the menu bar while the server is running. The Inference section updates on its own about every two seconds; you do not need to reload anything.

## When the section appears

The Inference section is shown whenever a model is **resident** (loaded in memory). If no model is loaded, there is nothing to report and the section stays empty.

When a model is resident but not currently handling any requests, the section shows a quiet line:

> Idle — no active requests

That line means the model is ready and waiting, not that anything is wrong.

## Reading a model block

Inference is grouped **by model**. Each resident model gets its own block, because scheduling is decided per model — a vision model running one request at a time can sit right next to a text model that is batching several. A block has three parts:

- **Status dot** — a small indicator that the model is resident and active.
- **Model name** — the model the block refers to.
- **Mode summary** — how requests to this model are being scheduled right now (see below).

Under the block, each in-flight request gets its own stat line.

### Mode summary: batched vs. single stream

The mode summary tells you how this model handles concurrent requests:

- **`Batched 3/32 · 2 queued`** — the model is running requests in a batch. `3/32` means three requests are generating at once out of a batch capacity of 32, and `2 queued` means two more are waiting for a free slot. The queued count only appears when requests are actually waiting; it drains as slots free up.
- **`Single stream`** — the model runs one request at a time. Additional requests wait until the current one finishes.

Not every model batches. Batching depends on the model's architecture, so some families always run single stream, and vision models in particular are served one request at a time. In the native app's **Models** list, models that support batched inference are marked with a batching badge; a model without that badge will show **Single stream** here.

### Per-request stats

For each active request, the section shows a stat line with:

- **Prompt tokens** — how many tokens were in the request's prompt.
- **Generated tokens** — how many tokens have been produced so far.
- **Mean tok/s** — the average generation speed for that request, in tokens per second.
- **Time to first token** — how long the request waited before the first output token appeared.

These numbers are per request, so with a batching model you see one line per active stream, and you can watch a slow first-token time or a low tok/s as load rises.

## What the section does not show

- **No cache hit/miss counts.** Prompt-cache reuse is not active in the engine today, so there is no truthful number to report. This is intentionally left out rather than shown as a misleading zero.
- **No per-user or per-request identity.** Streams are shown as anonymous slots on a model; the section does not attribute a request to the user or API key that made it.

## Verify it worked

1. Start the server and load a model.
2. Open the menu extra. With no traffic, the Inference section shows the model as **Idle — no active requests**.
3. Send a request — from the Web Chat, or with `curl`:

   ```bash
   curl http://127.0.0.1:11434/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{
       "model": "MODEL_NAME",
       "messages": [{ "role": "user", "content": "Write a short poem about the sea." }],
       "stream": true
     }'
   ```

   Replace `MODEL_NAME` with an installed model — list them with `GET /v1/models`.
4. While the request runs, the model block shows a mode summary and a stat line with live token counts and tok/s. Send several requests at once against a batching model and watch the active count rise (and, under enough load, the queued count appear and drain).

## Related pages

- [Install and Run Pico AI Server](../getting-started/install-and-run-pico-ai-server.md)
- [Enable Built-in Tools](../enable-built-in-tools.md) — the System Info tool reports host memory, which pairs with watching inference load.
