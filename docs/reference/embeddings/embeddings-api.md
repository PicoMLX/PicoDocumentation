---
title: Embeddings API
sidebar_position: 2
---

<!-- Mode: Reference -->

## Summary
Pico AI Server has embedding code and embedding settings in source, but the public HTTP embeddings routes are not registered in the current server build. Treat this page as the current-state reference, not as a promise that `/v1/embeddings` or `/api/embed` are live today.

## Supported embedding models
These models appear in the current `EmbeddingsConfiguration.models` list:

| Model ID |
| --- |
| `sentence-transformers/all-MiniLM-L6-v2` |
| `sentence-transformers/msmarco-bert-base-dot-v5` |
| `sentence-transformers/paraphrase-multilingual-mpnet-base-v2` |
| `thenlper/gte-base` |
| `tomaarsen/xlm-roberta-base-multilingual-en-ar-fr-de-es-tr-it` |

Current defaults in source

| Setting | Value |
| --- | --- |
| Default embeddings model | `sentence-transformers/msmarco-bert-base-dot-v5` |
| Batch size | `32` |
| Parse format | `automatic` |
| Splitter | `semantic` |
| Chunk size | `512` |
| Chunk overlap | `96` |
| Threshold | `0.7` |
| Max results | `30` |

## Storage

| Item | Current path shape |
| --- | --- |
| Base library | User-configurable model-library base directory |
| Language models | `<base>/models/` |
| Embedding models | `<base>/models/embeddings/` |

## Example

Use this negative check to confirm the current build does not expose the public OpenAI-compatible embeddings route:

```bash
curl -i http://127.0.0.1:11434/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "sentence-transformers/msmarco-bert-base-dot-v5",
    "input": "hello world"
  }'
```

Expect a not-found style result, because the current router does not register this path.

## Errors

| Current state | Meaning |
| --- | --- |
| Route not available | `/v1/embeddings` and `/api/embed` are commented out in the current router |

## Edge cases
- PicoCore does include an embedding service, so this is an availability issue in the HTTP surface, not an absence of embedding code.
- The native app also includes embedding settings, but the embeddings tab is not enabled in the current settings UI.
- TODO: document the public request and response schema when the server registers `/v1/embeddings` or `/api/embed`.
