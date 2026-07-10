---
title: Chat API
sidebar_position: 2
---

## Summary
Send chat requests through either the OpenAI-compatible or Ollama-compatible surface. The current build accepts text-only messages, content-part arrays with text, images, and video, plus Ollama-style `images` arrays on messages.

## Endpoints
- `POST /v1/chat/completions`
- `POST /api/chat`
- `POST /api/generate`

## Request fields

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `messages` | array | Yes | Must contain at least one message |
| `model` | string | No | Current build falls back to the configured default model if omitted |
| `stream` | boolean | No | Omitted means non-streaming |
| `temperature` | number | No | Sampling temperature |
| `top_p` | number | No | Nucleus sampling |
| `top_k` | integer | No | Top-k sampling |
| `min_p` | number | No | Minimum probability filter |
| `frequency_penalty` | number | No | Frequency penalty |
| `presence_penalty` | number | No | Presence penalty |
| `repetition_penalty` | number | No | Repetition penalty |
| `repetition_context_size` | integer | No | Repetition window |
| `presence_context_size` | integer | No | Presence window |
| `frequency_context_size` | integer | No | Frequency window |
| `max_tokens` | integer | No | Deprecated alias for `max_completion_tokens` |
| `max_completion_tokens` | integer | No | Maximum completion tokens |
| `reasoning.effort` | object | No | OpenAI-style reasoning control |
| `chat_template_kwargs.enable_thinking` | object | No | vLLM-style reasoning control |
| `think` | boolean | No | Ollama-style reasoning control |
| `tools` | array | No | Function-style tool definitions |
| `options` | object | No | Ollama-compatible generation options |

## Message schema

### Roles

`system`, `user`, `assistant`, `tool`

### Content forms

| Form | Notes |
| --- | --- |
| string | Plain text message |
| array of content parts | Supports mixed text and media parts |

### Content part types

| Type | Notes |
| --- | --- |
| `text` | Text part |
| `input_text` | Text part |
| `output_text` | Text part |
| `image_url` | URL or `data:` URL |
| `input_image` | URL or `data:` URL |
| `video_url` | URL or `data:` URL |
| `input_video` | URL or `data:` URL |

## Reasoning
Pico AI Server supports OpenAI, vLLM, and Ollama ways of toggling reasoning.
The current precedence is:

1. `think`
2. `chat_template_kwargs.enable_thinking`
3. `reasoning.effort`

### OpenAI-compatible reasoning
Pico AI Server maps `reasoning.effort` to a binary on or off state.

| Value | Result |
| --- | --- |
| `low` | Reasoning off |
| `medium` | Reasoning on |
| `high` | Reasoning on |
| `on` | Reasoning on |
| `off` | Reasoning off |
| `none` | Reasoning off |

### vLLM-compatible reasoning
Set `chat_template_kwargs.enable_thinking` to `true` or `false`.

### Ollama-compatible reasoning
Set `think` to `true` or `false`.

:::info
On the Chat Completions path, reasoning text currently arrives as normal assistant output rather than a separate thinking field.
:::

## Examples

### OpenAI-compatible request

```bash
curl http://127.0.0.1:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "messages": [
      {"role": "user", "content": "Say hello in one sentence."}
    ]
  }'
```

Example response

```json
{
  "id": "chatcmpl-12345",
  "object": "chat.completion",
  "created": 1743180000,
  "model": "MODEL_NAME",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "TEXT_FROM_MODEL"
      },
      "finish_reason": "stop"
    }
  ]
}
```

The current non-streaming OpenAI-compatible response does not include a `usage` block.

### OpenAI-compatible streaming

```bash
curl -N http://127.0.0.1:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "stream": true,
    "messages": [
      {"role": "user", "content": "Count to three."}
    ]
  }'
```

The stream is Server-Sent Events. Chunks are prefixed with `data:` and the stream ends with:

```text
data: [DONE]
```

### Ollama-compatible request

```bash
curl http://127.0.0.1:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "messages": [
      {"role": "user", "content": "Say hello in one sentence."}
    ]
  }'
```

Example response

```json
{
  "model": "MODEL_NAME",
  "created_at": "2026-03-28T19:00:00Z",
  "message": {
    "role": "assistant",
    "content": "TEXT_FROM_MODEL",
    "thinking": ""
  },
  "done": true
}
```

Ollama-compatible streaming uses `application/x-ndjson`.

## Errors

| Status | OpenAI-compatible error type | Typical cause |
| --- | --- | --- |
| `400` | `invalid_request_error` | Empty `messages`, bad JSON, unsupported request shape |
| `404` | `not_found_error` | Model not found |
| `408` | `invalid_request_error` | Generation canceled |
| `409` | `invalid_request_error` | Model is incomplete |
| `500` | `server_error` | Internal failure |

Ollama-compatible errors use the simpler form:

```json
{"error":"message"}
```

## Edge cases
- If `model` is omitted, the current build falls back to the configured default model.
- If `stream` is omitted, the request is handled as non-streaming.
- Multiple system messages are merged before generation.
- The request model accepts `format`, but the current build does not give it a stable, documented effect.
- There is no public `/v1/chat` route. Use `/v1/chat/completions`.
