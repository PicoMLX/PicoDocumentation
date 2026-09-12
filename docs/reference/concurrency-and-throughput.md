---
title: Concurrency and Throughput
sidebar_position: 4
description: How Pico AI Server handles simultaneous requests from multiple clients, including automatic batching, queuing behavior, and shared vision-model residency.
---

## Summary
Pico AI Server is a multi-user server: several clients can call it at the same time. This page describes how the server handles simultaneous requests so you can set client timeouts and expectations correctly. It applies to the chat, completion, and responses endpoints.

## Concurrent requests
You can send multiple requests at once. When they target a compatible model, Pico AI Server serves them together in a single batched decoding pass instead of running them strictly one after another. Batching is automatic: there is no setting to turn it on, and no per-request field controls it.

Requests that cannot share a batch — for example, a model family that does not support batched decoding — fall back to a single-stream path and are served one at a time for that model.

### Try it now

Send three requests in parallel and confirm each one returns its own HTTP status:

```bash
for i in 1 2 3; do
  curl -sS -o /dev/null -w "request $i: HTTP %{http_code}\n" \
    http://127.0.0.1:11434/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
      "model": "MODEL_NAME",
      "messages": [{"role": "user", "content": "Say hello in one sentence."}]
    }' &
done
wait
```

Replace `MODEL_NAME` with an installed model — list them with `GET /v1/models`. Each request runs concurrently and prints its own status line (the order varies):

```text
request 1: HTTP 200
request 2: HTTP 200
request 3: HTTP 200
```

A non-`200` code, or a `curl` error in place of a status line, marks a request that did not succeed. `-sS` keeps error messages visible while hiding the progress meter, and `-o /dev/null` discards the response body so only the status lines remain.

## Queuing and backpressure
When more work arrives than the server can decode at once, extra requests wait in a queue and start as capacity frees up. The server does not shed load with a rate-limit response: there is no `429 Too Many Requests` and no `503 Service Unavailable` on the busy path. A saturated server shows up as higher latency, not as an error.

Design clients accordingly:

- Use a generous request timeout. A queued request can wait behind others before it starts producing tokens.
- Prefer streaming for long generations, so you receive tokens as soon as your request begins decoding. The streaming format differs by endpoint: see the [Chat API](./chat/chat-api.md) page for Chat Completions and Ollama, or the [OpenResponses API](./openresponses-api.md) page for `/v1/responses`.
- Do not treat a slow response as a failure to retry right away. An aggressive retry adds more work to the same queue.

Cancellation is the one load-related response you will see: if you cancel a non-streaming generation, the server returns `408 Request Timeout`.

## Vision models and memory
When you use a vision-capable model, Pico AI Server serves both text-only and image requests from a single resident copy of that model. It does not load a separate text model alongside it, which keeps memory use lower on a shared server.

A request that carries an image or video still needs a vision-capable model. If the selected model cannot act as one, the request fails rather than silently answering without the media. See the [Chat API](./chat/chat-api.md) page for the media content-part forms.

## Edge cases
- Batching and queuing are engine behaviors, not request parameters. No field in a request enables, disables, or reserves a batch slot.
- Concurrency is shared across all clients. One client sending many parallel requests competes with every other client for the same decoding capacity.
- The current build reports live request and memory activity in the app's menu-bar panel, not through the HTTP API. No endpoint returns queue depth or the number of active streams.

## Troubleshooting

- **Symptom:** Parallel requests take far longer than the same request sent on its own, or appear to hang.
  **Likely cause:** The server is at capacity and is queuing your requests; each starts only as earlier work finishes. This is backpressure, not a failure — no error is returned.
  **Fix:** Raise the client timeout, send fewer requests at once, or stream so you receive tokens as soon as your request begins decoding.
  **Verify:** Send a single request in isolation. If it returns promptly, the earlier delay was queuing rather than a server problem.

## Next steps

- [Chat API](./chat/chat-api.md) — request fields, streaming, and media content-part forms.
- [OpenResponses API](./openresponses-api.md) — the `/v1/responses` contract, including its streaming lifecycle events.
- [Endpoint Summary](./endpoint-summary.md) — the full HTTP surface and status codes.
