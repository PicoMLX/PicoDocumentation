---
title: Chat API
sidebar_position: 2
---

<!-- Mode: Reference -->

## Summary
Send chat or completion requests using OpenAI-compatible or Ollama-compatible
endpoints. Pico AI Server supports message content types `text`, `image_url`,
and `video_url`.

## Endpoints
- `POST /v1/chat` (OpenAI-compatible chat)
- `POST /api/chat` (Ollama-compatible chat)
- `POST /api/generate` (Ollama-compatible completion)

TODO: Confirm whether `/v1/chat/completions` is also supported.

## Parameters
| Name | Type | Required | Default | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `model` | String | Yes | None | Model name | Must be installed |
| `messages` | Array | Yes | None | List of message objects | TODO: confirm schema |
| `stream` | Boolean | No | None | If true or null, stream tokens | TODO: confirm |
| `reasoning` | Enum | No | None | Reasoning toggle (OpenAI-style) | See Reasoning |
| `chat_template_kwargs` | Object | No | None | vLLM-style reasoning options | See Reasoning |
| `max_tokens` | Integer | No | None | Deprecated; use `max_completion_tokens` | TODO: confirm |
| `max_completion_tokens` | Integer | No | None | Max output tokens | TODO: confirm |
| `temperature` | Number | No | None | Sampling temperature | TODO: confirm range |
| `frequency_penalty` | Number | No | None | Frequency penalty | TODO: confirm range |
| `top_p` | Number | No | None | Top-p sampling | TODO: confirm range |
| `user` | String | No | None | Ignored by Pico AI Server | None |
| `format` | String | No | None | Ignored by Pico AI Server | None |
| `options` | Object | No | None | Ollama options | TODO: confirm fields |
| `think` | Boolean | No | None | Ollama-style reasoning toggle | Pico AI Server 1.1.18+ |

## Reasoning
Pico AI Server supports OpenAI, vLLM, and Ollama ways of toggling reasoning.
The `reasoning` and `chat_template_kwargs.enable_thinking` options are supported
in 1.1.14+. The `think` option is supported in 1.1.18+.

### OpenAI-compatible reasoning
Pico AI Server supports binary ON or OFF states. Requests specifying `low`
map to reasoning off. Non-standard values `on`, `off`, and `none` are accepted.

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
As of Pico AI Server 1.1.18, the `thinking` field in the response is not
supported. Reasoning output is streamed as normal output.
:::

## Example request
```bash
curl http://127.0.0.1:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  }'
```

## Example response
```json
TODO: Insert a sample response from Pico AI Server.
```

## Errors
TODO: Confirm error codes and messages.

| Code | Message | Cause | Fix |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Edge cases
- Requesting an unavailable model returns an error. TODO: confirm error code.
- Streaming responses may not include a `thinking` field. See Reasoning.
