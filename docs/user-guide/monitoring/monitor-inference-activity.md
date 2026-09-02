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
- **`Fast path 1/32`** — a batch-capable model is serving a single request on the engine's *solo fast path*, an optimized lane for a lone request. It still shows the batch capacity (`/32`) because it is the same batching engine, not a different mode: the next request joins this one and the row becomes `Batched 2/32`. A queued variant (`Fast path 1/32 · 1 queued`) can appear when a newcomer has to wait for a slot rather than joining immediately.
- **`Single stream`** — the model runs one request at a time. Additional requests wait until the current one finishes.

Fast path and single stream look similar — one active request — but they mean different things. **Fast path** is a batching model that happens to have only one request right now and will batch the next one; **Single stream** is a model that cannot batch at all, so requests always run one after another.

Not every model batches. Batching depends on the model's architecture, so some families always run single stream, and vision models in particular are served one request at a time. In the native app's **Models** list, models that support batched inference are marked with a batching badge; a model without that badge will show **Single stream** here.

### Per-request stats

For each active request, the section shows a stat line such as:

> 1200 prompt · 412 tok · 38 tok/s · 0.4 s to first token

Reading left to right:

- **Prompt tokens** (`1200 prompt`) — how many tokens were in the request's prompt.
- **Generated tokens** (`412 tok`) — how many tokens have been produced so far.
- **Mean tok/s** (`38 tok/s`) — the average generation speed for that request since its first token.
- **Time to first token** (`0.4 s to first token`) — how long the request waited before the first output token appeared, including any time queued behind other rows.

The rate and time-to-first-token fields appear only once the first token is out, so a request still in its prompt phase shows just the token counts. These numbers are per request, so with a batching model you see one line per active stream, and you can watch a slow first-token time or a low tok/s as load rises.

## What the section does not show

- **No cache hit/miss counts.** Prompt-cache reuse is not active in the engine today, so there is no truthful number to report. This is intentionally left out rather than shown as a misleading zero.
- **No per-user or per-request identity.** Streams are shown as anonymous slots on a model; the section does not attribute a request to the user or API key that made it.

## Verify it worked

1. Start the server and load a model.
2. Open the menu extra. With no traffic, the Inference section shows the model as **Idle — no active requests**.
3. Send a request that generates long enough to still be running when the section refreshes. A short prompt can finish inside the roughly two-second refresh, so ask for a long answer and raise the token cap:

   ```bash
   curl http://127.0.0.1:11434/v1/chat/completions \
     -H "Content-Type: application/json" \
     -d '{
       "model": "MODEL_NAME",
       "messages": [{ "role": "user", "content": "Write a long, detailed essay about the history of sailing." }],
       "max_completion_tokens": 2000,
       "stream": true
     }'
   ```

   Replace `MODEL_NAME` with an installed model — list them with `GET /v1/models`. While it runs, the model block shows a mode summary and a stat line with live token counts and tok/s.
4. To see batching and the queued count, send several long requests at once against a batch-capable model:

   ```bash
   for i in 1 2 3 4 5; do
     curl -s http://127.0.0.1:11434/v1/chat/completions \
       -H "Content-Type: application/json" \
       -d '{
         "model": "MODEL_NAME",
         "messages": [{ "role": "user", "content": "Write a long, detailed essay about the history of sailing." }],
         "max_completion_tokens": 2000,
         "stream": true
       }' >/dev/null &
   done
   ```

   Watch the active count rise (for example, `Batched 5/32`) and, if you launch more requests than the batch capacity, the queued count appear and then drain as slots free up.

## Troubleshooting

- **Symptom:** The Inference section does not appear at all.
  **Cause:** No model is resident — nothing is loaded in memory yet.
  **Fix:** Open the **Models** tab in the native app and select or load a model. Once it is resident, the section appears (showing **Idle — no active requests** until traffic arrives).
- **Symptom:** A model always shows **Single stream**, even when you send several requests at once.
  **Cause:** That model does not run batched — vision models and model families whose cache topology cannot batch always run one request at a time.
  **Fix:** This is expected. Check the **Models** list for the batching badge; use a batch-capable model if you need concurrent requests to share one engine.
- **Symptom:** You sent a request but never saw its stat line.
  **Cause:** The generation finished inside the roughly two-second refresh window, so it was gone before the next update.
  **Fix:** Use the longer request above (raise `max_completion_tokens` and ask for a long answer), or send several at once so at least one is always in flight when the section refreshes.

## Next steps

- [Install and Run Pico AI Server](../getting-started/install-and-run-pico-ai-server.md)
- [Enable Built-in Tools](../enable-built-in-tools.md) — the System Info tool reports host memory, which pairs with watching inference load.
