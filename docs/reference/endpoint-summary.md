---
title: Endpoint Summary
sidebar_position: 1
---

## Summary
Use this page as the cheat sheet for the current HTTP surface in Pico AI Server. It lists the routes registered in the current build, plus the limits that matter before you wire a client to them.

## Endpoint table

| Method | Path | Surface | Notes |
| --- | --- | --- | --- |
| `GET` | `/` | WebUI | Browser chat root URL |
| `HEAD` | `/` | Utility | Root health-style check |
| `GET` | `/hostname` | Utility | Returns the current host name |
| `GET` | `/ip` | Utility | Returns the current IP address or host name fallback |
| `GET` | `/v1/models` | OpenAI-compatible | Lists available models |
| `POST` | `/v1/chat/completions` | OpenAI-compatible | Chat Completions |
| `POST` | `/v1/responses` | OpenResponses | Public Responses entry point |
| `GET` | `/api/tags` | Ollama-compatible | Lists available models |
| `POST` | `/api/chat` | Ollama-compatible | Chat |
| `POST` | `/api/generate` | Ollama-compatible | Completion-style route using the same chat pipeline |
| `GET` | `/api/version` | Ollama-compatible | Version route |
| `GET` | `/api/ps` | Ollama-compatible | Current build reports available models with expiry times |
| `POST` | `/api/show` | Ollama-compatible | Model metadata |
| `GET` | `/props` | llama.cpp-compatible | Properties endpoint |
| `GET` | `/slots` | llama.cpp-compatible | Currently returns `501 Not Implemented` |
| `GET`, `POST` | `/mcp` | MCP | Streamable MCP endpoint |

## Not public yet

| Path | Current state |
| --- | --- |
| `/v1/embeddings` | Route is not registered in the current build |
| `/api/embed` | Route is not registered in the current build |
| `/v1/responses/:response_id*` | Helper routes exist in the current build, but are not ready for client documentation |
| `/v1/conversations/*` | Routes exist in the current build, but most handlers are placeholders |

## Example

```bash
curl http://127.0.0.1:11434/v1/models
```

If Pico AI Server is running, you get JSON back.

## Errors

| Status | Meaning | Notes |
| --- | --- | --- |
| `400` | Invalid request | Used for bad JSON, empty chat messages, and other request-shape problems |
| `404` | Not found | Used for missing models on most request paths |
| `408` | Request timeout | Used when generation is canceled |
| `409` | Conflict | Used for incomplete model states on some paths |
| `500` | Server error | Used for internal failures and some incomplete compatibility handlers |

## Edge cases
- `GET /api/chat/completions` exists, but it is an internal helper that returns an empty `200` JSON body. Do not use it as the public Chat Completions route.
- The router does not currently attach the auth middleware. Do not assume bearer-token enforcement unless your deployment adds it.
- `Serve Pico web chat` is present in settings, but the current build still serves the root WebUI unconditionally. Treat that toggle as under validation.
