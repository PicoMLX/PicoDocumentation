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

## Authentication

By default Pico AI Server serves every route without credentials. An admin can turn on `Require API key` in the native app's `Users` tab (Settings). While it is on, the router's auth middleware enforces per-user API keys:

- Requests must send `Authorization: Bearer <token>` or `X-API-Key: <token>`. The `X-API-Key` header is for Anthropic-SDK compatibility and uses the same tokens as bearer auth.
- Missing, malformed, or disabled-user tokens get `401` with an OpenAI-style body: `{"error":{"message":"Invalid or missing API key.","type":"authentication_error","code":"invalid_api_key"}}`.
- Exempt from auth even while it is on: `HEAD /`, `OPTIONS` (CORS preflight), the static WebUI assets, and `GET /api/download-status`.

## Example

```bash
curl http://127.0.0.1:11434/v1/models
```

If Pico AI Server is running, you get JSON back.

## Errors

| Status | Meaning | Notes |
| --- | --- | --- |
| `400` | Invalid request | Used for bad JSON, empty chat messages, and other request-shape problems |
| `401` | Unauthorized | Returned when `Require API key` is on and the request has no valid API key |
| `404` | Not found | Used for missing models on most request paths |
| `408` | Request timeout | Used when generation is canceled |
| `409` | Conflict | Used for incomplete model states on some paths |
| `500` | Server error | Used for internal failures and some incomplete compatibility handlers |

## Edge cases
- `GET /api/chat/completions` exists, but it is an internal helper that returns an empty `200` JSON body. Do not use it as the public Chat Completions route.
- The router attaches an auth middleware, but it enforces API keys only while `Require API key` is on in the `Users` tab. With that setting off (the default), every route is served without credentials. See [Authentication](#authentication).
- `Serve Pico web chat` is present in settings, but the current build still serves the root WebUI unconditionally. Treat that toggle as under validation.
