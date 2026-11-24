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
| `GET`, `POST` | `/v1/conversations` | Conversations | List or create stored chats (user accounts only) |
| `GET`, `POST`, `DELETE` | `/v1/conversations/{id}` | Conversations | Retrieve, update, or delete a chat |
| `GET`, `POST` | `/v1/conversations/{id}/items` | Conversations | List or add items |
| `GET`, `POST`, `DELETE` | `/v1/conversations/{id}/items/{item_id}` | Conversations | Retrieve, edit, or delete an item |
| `GET`, `POST` | `/v1/conversation_groups` | Conversations | List or create sidebar groups |
| `POST`, `DELETE` | `/v1/conversation_groups/{id}` | Conversations | Rename or delete a group |
| `GET` | `/v1/conversation_events` | Conversations | Server-Sent change notices |
| `GET`, `POST` | `/mcp` | MCP | Streamable MCP endpoint |

## Not public yet

| Path | Current state |
| --- | --- |
| `/v1/embeddings` | Route is not registered in the current build |
| `/api/embed` | Route is not registered in the current build |
| `/v1/responses/:response_id*` | Helper routes exist in the current build, but are not ready for client documentation |

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

## Authentication
The current build attaches auth middleware that keys off the `Require an Invitation` (user accounts) setting:

- **User accounts off (default):** requests pass through with no token.
- **User accounts on:** routes under `/v1/` and `/api/` require a valid `Authorization: Bearer <api-key>` or `X-API-Key: <api-key>` header, and a missing or invalid token answers `401`. Static web-UI files, `HEAD /`, `OPTIONS` preflight, and the cluster's model-file routes stay exempt. An `/v1/` or `/api/` path still needs a token even when it ends in a static extension such as `.json`.

## Edge cases
- `GET /api/chat/completions` exists, but it is an internal helper that returns an empty `200` JSON body. Do not use it as the public Chat Completions route.
- `Serve Pico web chat` is present in settings, but the current build still serves the root WebUI unconditionally. Treat that toggle as under validation.
