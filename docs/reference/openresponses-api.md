---
title: OpenResponses API
sidebar_position: 3
---

## Summary
Pico AI Server exposes `POST /v1/responses` as its current OpenResponses entry point. Use this path when you want OpenResponses-style output objects and stream events. Keep the helper lifecycle routes out of production clients for now; they exist in the current build, but they are not ready for public documentation.

## Endpoint
- `POST /v1/responses`

## Request fields

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `input` | string or array | Yes | Empty input is rejected |
| `model` | string | No | Current build falls back to the configured default model if omitted |
| `stream` | boolean | No | `true` enables `text/event-stream` |
| `max_output_tokens` | integer | No | Maps to the server max-completion setting |
| `reasoning.effort` | string | No | `none` and `low` map to reasoning off |
| `tools` | array | No | Function tools are bridged into the Pico tool format |
| `tool_choice` | string or object | No | Defaults to `auto` when omitted |
| `temperature` | number | No | Defaults to `1` in the current non-streaming response builder |
| `top_p` | number | No | Defaults to `1` |
| `frequency_penalty` | number | No | Defaults to `0` |
| `presence_penalty` | number | No | Defaults to `0` |

## Examples

### Non-streaming request

```bash
curl http://127.0.0.1:11434/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "input": "Explain LAN Mode in one paragraph."
  }'
```

Example response excerpt

```json
{
  "status": "completed",
  "model": "MODEL_NAME",
  "output": [
    {
      "type": "message",
      "status": "completed"
    }
  ],
  "usage": {
    "input_tokens": 12,
    "output_tokens": 24,
    "total_tokens": 36
  }
}
```

### Streaming request

```bash
curl -N http://127.0.0.1:11434/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "stream": true,
    "input": [
      {
        "role": "user",
        "content": [
          {"type": "input_text", "text": "Explain Bonjour discovery in one paragraph."}
        ]
      }
    ]
  }'
```

The stream uses `text/event-stream`. The current implementation emits standard response lifecycle events such as `response.created` and `response.completed`.

## Response notes

| Item | Current behavior |
| --- | --- |
| `tool_choice` omitted | Treated as `auto` |
| `tool_choice: "none"` | Disables both explicit tools and internal tools |
| `usage` | Included in the non-streaming completed response |
| Input item parsing | The current adapter extracts text from input items for generation |

## Errors

| Status | `error.code` | Notes |
| --- | --- | --- |
| `400` | `invalid_request_error` | Invalid request shape or empty input |
| `401` | `authentication_error` | Reserved for auth failures |
| `404` | `not_found` | Not found |
| `408` | `request_timeout` | Generation canceled or timed out |
| `409` | `conflict` | Conflict state |
| `500` | `server_error` | Internal failure |

Error body shape

```json
{
  "error": {
    "message": "message",
    "type": "api_error",
    "code": "invalid_request_error"
  }
}
```

## Edge cases
- If `model` is omitted, the current build falls back to the configured default model.
- Helper routes such as `GET /v1/responses/:response_id` and `POST /v1/responses/:response_id/cancel` exist in the current build, but they are not ready for public client use.
- If you need multimodal request handling today, the Chat API is the safer surface. The current Responses adapter is text-first.
