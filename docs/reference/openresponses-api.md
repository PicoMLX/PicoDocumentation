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
| `tools` | array | No | Function tools are bridged into the Pico tool format. One `mcp` entry can opt into Pico's own tools — see [Pico tools over MCP](#pico-tools-over-mcp) |
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

## Pico tools over MCP

A Responses client can let the model use Pico AI Server's own tools — the built-in tools and any connected MCP servers' tools — by opting in. Without the opt-in, a Responses request is offered only tools that need no approval, and no tool items appear in the output.

### Opt in

Add one `mcp` entry to `tools` whose `server_label` is `pico`:

```json
{
  "type": "mcp",
  "server_label": "pico",
  "server_url": "http://127.0.0.1:11434/mcp",
  "require_approval": "always"
}
```

- `server_label` must be `pico`. The host in `server_url` is ignored. An `mcp` entry for any other server, or a second `pico` entry, is rejected with `400`.
- `allowed_tools` restricts which Pico tools the model may use. It is a list of tool names, or an object `{"tool_names": ["TOOL_NAME"], "read_only": true}`. Omit it to allow every Pico tool; send `[]` to allow none.
- `require_approval` controls which calls pause for your approval:

  | Value | Effect |
  | --- | --- |
  | omitted or `"always"` | Every call to a Pico tool pauses for approval |
  | `"never"` | No call pauses |
  | `{"never": {"tool_names": ["TOOL_NAME"]}}` | The named tools run without asking; the rest pause |
  | `{"always": {"tool_names": ["TOOL_NAME"]}}` | Only the named tools pause; the rest run |
  | `{..., "read_only": true}` | Matches tools from a trusted source that mark themselves read-only |

### Example

This streams a request that lets the model call Pico's tools without pausing for approval:

```bash
curl -N http://127.0.0.1:11434/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "stream": true,
    "input": "What Mac and chip am I running on?",
    "tools": [
      {
        "type": "mcp",
        "server_label": "pico",
        "server_url": "http://127.0.0.1:11434/mcp",
        "require_approval": "never"
      }
    ]
  }'
```

### Output items

With the opt-in, Pico reports what it does as Responses output items, each with matching stream events:

- `mcp_list_tools` — the tools Pico offers, each with `name`, `description`, `input_schema`, and, for trusted sources, `annotations`.
- `mcp_call` — one per tool Pico runs, with `name`, `arguments`, and `output` or `error`, and a `status` of `completed` or `failed`.
- `mcp_approval_request` — emitted for each Pico call waiting for your approval. The turn then ends with `status: "completed"`.

A client's own function tools are still reported as `function_call` items.

### Approve and resume

When a turn ends with `mcp_approval_request` items, send the conversation history back to continue it. For each request, add an `mcp_approval_response`:

```json
{ "type": "mcp_approval_response", "approval_request_id": "mcpr_…", "approve": true }
```

Add a `function_call_output` for each of your own `function_call` items from the same turn. Pico rechecks permission, runs each approved call, and reports it as an `mcp_call` carrying its `approval_request_id`. A declined call is not run; the model is told the user declined it.

A call you approve runs once. If you send its approval again while it is still running, Pico returns `409`; once it has finished, Pico returns the stored result instead of running the tool a second time.

### Errors specific to the opt-in

| Status | Cause |
| --- | --- |
| `400` | An `mcp` opt-in for a server other than `pico`, a second `pico` entry, an approval sent without the opt-in, an unanswered approval request, or an approval that refers to an earlier turn |
| `409` | An approval re-sent while its call is still running |

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
