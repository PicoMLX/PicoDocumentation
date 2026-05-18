---
title: Embeddings API
description: Create text embeddings with Pico AI Server using OpenAI- and Ollama-compatible endpoints and supported embedding models.
sidebar_position: 2
---

<!-- Mode: Reference -->

## Summary
Create embeddings using OpenAI-compatible or Ollama-compatible endpoints.

:::info
The embeddings API is available from Pico AI Server 1.1.12 and newer.
:::

## Supported embedding models
Embedding models are downloaded on demand and loaded into memory as needed.
Pre-downloading and persistent caching are not supported.

Default storage location: `<base-directory>/Embeddings` as set in WebUI.
TODO: Confirm how to read or change the base directory.

| Name | Architecture |
| --- | --- |
| `all-MiniLM-L6-v2` | BERT |
| `msmarco-bert-base-dot-v5` | BERT |
| `LaBSE` | BERT |
| `gte-base` | BERT |
| `bert-base-uncased` | BERT |
| `mxbai-embed-large-v1` | BERT |
| `roberta-base` | RoBERTa |
| `xlm-roberta-base` | XLM-RoBERTa |
| `multilingual-e5-large` | XLM-RoBERTa |
| `multilingual-e5-small` | XLM-RoBERTa |
| `paraphrase-multilingual-mpnet-base-v2` | XLM-RoBERTa |
| `xlm-roberta-base-multilingual-en-ar-fr-de-es-tr-it` | XLM-RoBERTa |
| `clip-vit-base-patch16` | CLIP |
| `clip-vit-base-patch32` | CLIP |
| `clip-vit-large-patch14` | CLIP |
| `glove-twitter-25` | Word2Vec |
| `glove-twitter-50` | Word2Vec |
| `glove-twitter-100` | Word2Vec |
| `glove-twitter-200` | Word2Vec |
| `potion-base-2M` | Model2Vec |
| `potion-base-4M` | Model2Vec |
| `potion-base-8M` | Model2Vec |
| `potion-retrieval-32M` | Model2Vec |
| `potion-base-32M` | Model2Vec |
| `M2V_base_output` | Model2Vec |
| `M2V_base_output` | Static |
| `static-similarity-mrl-multilingual-v1` | Static |

## `POST /v1/embeddings`
OpenAI-compatible embeddings endpoint.

Parameters
| Name | Type | Required | Default | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `model` | String | Yes | None | Embedding model name | Must be installed |
| `input` | String or Array | Yes | None | Input text(s) to embed | TODO: confirm size limits |
| `encoding_format` | String | No | None | Ignored by Pico AI Server | None |
| `user` | String | No | None | Ignored by Pico AI Server | None |

Example request
```bash
curl http://127.0.0.1:11434/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "all-MiniLM-L6-v2",
    "input": "hello world"
  }'
```

Example response
```json
{
  "object": "list",
  "model": "all-MiniLM-L6-v2",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [TODO]
    }
  ]
}
```

## `POST /api/embed`
Ollama-compatible embeddings endpoint.

Parameters
| Name | Type | Required | Default | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `model` | String | Yes | None | Embedding model name | Must be installed |
| `input` | String or Array | Yes | None | Input text(s) to embed | TODO: confirm size limits |

Example request
```bash
curl http://127.0.0.1:11434/api/embed \
  -H "Content-Type: application/json" \
  -d '{
    "model": "all-MiniLM-L6-v2",
    "input": "hello world"
  }'
```

Example response
```json
{
  "model": "all-MiniLM-L6-v2",
  "embeddings": [[TODO]],
  "total_duration": null,
  "load_duration": null,
  "prompt_eval_count": null
}
```

## Errors
TODO: Confirm error codes and messages.

| Code | Message | Cause | Fix |
| --- | --- | --- | --- |
| TODO | TODO | TODO | TODO |

## Edge cases
- Requesting a model that is not installed returns an error. TODO: confirm error code.
- Large input arrays may exceed limits. TODO: confirm limits and behavior.
