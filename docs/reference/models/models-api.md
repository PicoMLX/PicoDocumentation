---
title: Models API
sidebar_position: 2
---

## Summary
Use these endpoints to list models that are already available to Pico AI Server. These routes do not download models. Model downloads are managed by the admin in the native app.

## Endpoints
- `GET /v1/models`
- `GET /api/tags`
- `GET /api/ps`
- `POST /api/show`

## `GET /v1/models`
OpenAI-compatible list of available models.

Parameters: none.

Example request

```bash
curl http://127.0.0.1:11434/v1/models
```

Example response

```json
{
  "object": "list",
  "data": [
    {
      "id": "DeepSeek-R1-Distill-Qwen-14B-8bit",
      "object": "model",
      "created": 1740592086,
      "owned_by": "Pico AI Server"
    }
  ]
}
```

Fields

| Field | Type | Notes |
| --- | --- | --- |
| `object` | string | Always `list` |
| `data[].id` | string | The display name used by Pico AI Server |
| `data[].object` | string | Always `model` |
| `data[].created` | integer | Last-modified time from the local model record |
| `data[].owned_by` | string | Always `Pico AI Server` in the current build |

## `GET /api/tags`
Ollama-compatible list of available models.

Parameters: none.

Example request

```bash
curl http://127.0.0.1:11434/api/tags
```

Example response excerpt

```json
{
  "models": [
    {
      "name": "MODEL_NAME:latest",
      "model": "MODEL_ID:latest",
      "size": 1234567890,
      "digest": "",
      "details": {
        "format": "mlx",
        "parent_model": "",
        "family": "MODEL_FAMILY",
        "parameter_size": "PARAMETER_SIZE",
        "quantization_level": "QUANTIZATION"
      }
    }
  ]
}
```

Fields

| Field | Type | Notes |
| --- | --- | --- |
| `models[].name` | string | Pico display name with `:latest` appended |
| `models[].model` | string | Internal model identifier with `:latest` appended |
| `models[].size` | integer | Stored model size |
| `models[].digest` | string | SHA if available, else empty string |
| `models[].details.format` | string | Always `mlx` in the current build |
| `models[].details.parent_model` | string | Empty string in the current build |
| `models[].details.family` | string | Model family from Pico metadata |
| `models[].details.parameter_size` | string | Parameter-size string from Pico metadata |
| `models[].details.quantization_level` | string | Quantization string from Pico metadata |

## `GET /api/ps`
Ollama-compatible process list.

Parameters: none.

Example request

```bash
curl http://127.0.0.1:11434/api/ps
```

Example response excerpt

```json
{
  "models": [
    {
      "name": "MODEL_NAME:latest",
      "model": "MODEL_ID:latest",
      "expires_at": "2026-03-28T19:00:00Z",
      "details": {
        "format": "mlx"
      }
    }
  ]
}
```

In the current build, this route reports available models with idle-expiry data. It is not a strict "loaded models only" view.

## `POST /api/show`
Ollama-compatible model metadata lookup.

Parameters

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| `model` | string | Yes | Accepts names with or without `:latest` |

Example request

```bash
curl http://127.0.0.1:11434/api/show \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME:latest"
  }'
```

Example response excerpt

```json
{
  "modelfile": "",
  "parameters": "",
  "template": "",
  "details": {
    "format": "mlx",
    "family": "llama",
    "parameter_size": "PARAMETER_SIZE",
    "quantization_level": "QUANTIZATION"
  },
  "info": {
    "llama.context_length": 4096
  },
  "capabilities": ["completion", "thinking", "tools"]
}
```

Notes

| Field | Notes |
| --- | --- |
| `details.family` | Hard-coded to `llama` in the current build |
| `info["llama.context_length"]` | Always present in the current build |
| `capabilities` | Derived from model tags such as reasoning, tools, and vision |

## Errors

| Status | Meaning | Notes |
| --- | --- | --- |
| `500` | Server could not read model metadata | Applies to all model routes when the local model store fails |

## Edge cases
- Empty arrays are valid when no models are available yet.
- `/api/show` strips `:latest` before lookup.
- A missing model on `/api/show` is intended to be a `404`, but the current controller catches the lookup error and may return `500` instead.
- Client apps can list models, but they cannot download models through these routes.
