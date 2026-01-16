---
title: Models API
sidebar_position: 2
---

<!-- Mode: Reference -->

## Summary
List models that are already installed on Pico AI Server. Client apps cannot
download models directly. The admin downloads models in WebUI.

## Endpoints
- `GET /v1/models` (OpenAI-compatible)
- `GET /api/tags` (Ollama-compatible)
- `GET /api/ps` (Ollama-compatible, stub)
- `GET /api/show` (Ollama-compatible)

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
      "object": "model",
      "id": "DeepSeek-R1-Distill-Qwen-14B-8bit",
      "created": 1740592086,
      "owned_by": "Pico AI Server"
    }
  ]
}
```

Response fields
| Name     | Type    | Required | Default | Description | Constraints |
| ---      | ---     | ---      | ---     | ---         | --- |
| `object` | String  | Yes      | `list`  | Always `list` | Fixed value |
| `data`   | Array   | Yes      | None    | List of model objects | None |

Model object
| Name       | Type   | Required | Default | Description | Constraints |
| ---        | ---    | ---      | ---     | ---         | --- |
| `id`       | String | Yes      | None    | Model name | Hugging Face repo name |
| `created`  | Number | Yes      | None    | Last modified time (Unix timestamp) | TODO: confirm |
| `object`   | String | Yes      | `model` | Always `model` | Fixed value |
| `owned_by` | String | Yes      | `Pico AI Server` | Owner | Fixed value |

:::note
The model name is the repository name on Hugging Face. For example, if
the model URL is `https://huggingface.co/mlx-community/DeepSeek-R1-Distill-Llama-8B-3bit`,
the model name is `DeepSeek-R1-Distill-Llama-8B-3bit`.
:::

## `GET /api/tags`
Ollama-compatible list of available models.

Parameters: none.

Example request
```bash
curl http://127.0.0.1:11434/api/tags
```

Response fields
| Name     | Type  | Required | Default | Description | Constraints |
| ---      | ---   | ---      | ---     | ---         | --- |
| `models` | Array | Yes      | None    | List of model objects | None |

Model object
| Name          | Type   | Required | Default | Description | Constraints |
| ---           | ---    | ---      | ---     | ---         | --- |
| `name`        | String | Yes      | None    | Model name | None |
| `size`        | Number | Yes      | None    | Model size in bytes | TODO: confirm |
| `modified_at` | String | Yes      | None    | ISO 8601 timestamp | TODO: confirm |
| `digest`      | String | Yes      | None    | SHA digest | TODO: confirm |
| `model`       | String | Yes      | None    | Hugging Face repo name | None |
| `details`     | Object | Yes      | None    | Model details | None |

Details object
| Name                 | Type   | Required | Default | Description | Constraints |
| ---                  | ---    | ---      | ---     | ---         | --- |
| `format`             | String | Yes      | None    | Model format | TODO: confirm |
| `parent_model`       | String | Yes      | None    | Parent model name | TODO: confirm |
| `family`             | String | Yes      | None    | Model family | None |
| `quantization_level` | String | Yes      | None    | Quantization | None |
| `parameter_size`     | String | Yes      | None    | Parameter size | None |

## `GET /api/ps`
Ollama-compatible stub.

Parameters: none.

Example request
```bash
curl http://127.0.0.1:11434/api/ps
```

Example response
```json
{
  "parameters": "",
  "template": "Unknown",
  "license": "Unknown",
  "modelfile": "Unknown"
}
```

## `GET /api/show`
Ollama-compatible endpoint for model information.

Parameters: none.

Example request
```bash
curl http://127.0.0.1:11434/api/show
```

TODO: Confirm the response body for `/api/show`. Older docs conflict.

## Errors
TODO: Confirm error codes and messages.

| Code | Message | Cause | Fix |
| ---  | ---     | ---   | --- |
| TODO | TODO    | TODO  | TODO |

## Edge cases
- Empty list when no models are installed.
- TODO: Confirm response when model metadata is missing.
