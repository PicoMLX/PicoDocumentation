---
title: Conversations API
sidebar_position: 4
---

## Summary
The Conversations API stores chats on the server so that a client — including the web chat bundled with Pico AI Server — can save, list, branch, and reopen conversations. It follows OpenAI's [Conversations API](https://platform.openai.com/docs/api-reference/conversations) and adds Pico fields for the web UI's chats, sidebar groups, and a change-notice stream.

Chats are stored per account, so these routes work **only when user accounts are enabled** (`Require an Invitation`, under Settings). With user accounts off, every route answers `501 Not Implemented`.

## Endpoints

| Method | Path | Notes |
| --- | --- | --- |
| `GET` | `/v1/conversations` | List the caller's chats, most recently modified first |
| `POST` | `/v1/conversations` | Create a chat, optionally forking another |
| `GET` | `/v1/conversations/{conversation_id}` | Retrieve a chat |
| `POST` | `/v1/conversations/{conversation_id}` | Partial update |
| `DELETE` | `/v1/conversations/{conversation_id}` | Delete a chat and its items |
| `GET` | `/v1/conversations/{conversation_id}/items` | List items on every branch |
| `POST` | `/v1/conversations/{conversation_id}/items` | Add items (all or none) |
| `GET` | `/v1/conversations/{conversation_id}/items/{item_id}` | Retrieve one item |
| `POST` | `/v1/conversations/{conversation_id}/items/{item_id}` | Partial item edit |
| `DELETE` | `/v1/conversations/{conversation_id}/items/{item_id}` | Delete one item |
| `GET` | `/v1/conversation_groups` | List the caller's sidebar groups, newest first |
| `POST` | `/v1/conversation_groups` | Create a group |
| `POST` | `/v1/conversation_groups/{group_id}` | Rename a group |
| `DELETE` | `/v1/conversation_groups/{group_id}` | Delete a group (its chats stay, ungrouped) |
| `GET` | `/v1/conversation_events` | Stream change notices (Server-Sent Events) |

## Authentication

Because the API runs only when user accounts are enabled, every request needs a token. Send the account's API key as either header:

```text
Authorization: Bearer <api-key>
X-API-Key: <api-key>
```

- The authenticated account owns everything a request creates and is the only account whose chats it can see. Another account's record answers `404`, like a missing one.
- A missing or invalid token answers `401`.
- A token that belongs to an account that can't own chats (for example an agent's) answers `403`.

## Identifiers and timestamps

- **IDs are made by the client.** Each `id` — for a conversation, item, or group — must be a lowercase UUID version 4. The server rejects any other form with `400 invalid_id`.
- `created_at` is in Unix **seconds**. Every other time field ends in `_ms` and is in **milliseconds** since the Unix epoch. Incoming `_ms` values must be from `0` through `253402300799999` (the end of the year 9999).

## Optimistic concurrency

Update, rename, and item-edit requests accept an optional `if_version`. When it does not match the record's current `version`, the request is refused with `409 stale_version`, and the error body carries `current`: the record as it stands now.

A conversation's `version` moves only when its name changes; its `last_modified_ms` moves when items are added.

## Objects

### Conversation

```json
{
  "id": "0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d",
  "object": "conversation",
  "created_at": 1743180000,
  "last_modified_ms": 1743180000000,
  "version": 1,
  "name": "My chat",
  "metadata": {},
  "current_item_id": null,
  "pinned": false,
  "group_id": null,
  "forked_from_conversation_id": null,
  "settings": {}
}
```

- `current_item_id` is the owner's last-used branch, the default when the chat is reopened.
- `settings` holds the web UI's per-chat settings and is opaque to the server.
- `metadata` is a flat map of strings.
- Nullable fields (`current_item_id`, `group_id`, `forked_from_conversation_id`) are always present, as `null` when unset.

### Conversation item (message)

```json
{
  "id": "1c2d3e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f",
  "type": "message",
  "role": "user",
  "status": "completed",
  "content": [{ "type": "input_text", "text": "Hello" }],
  "message_type": "text",
  "parent_id": null,
  "children_ids": [],
  "timestamp_ms": 1743180000000,
  "version": 1
}
```

- `content` is exactly one text part: `input_text` for user, system, and tool items; `output_text` for assistant items.
- `children_ids` is derived by the server. Sending it is an error.
- Items form a tree through `parent_id`; the first item (the root) has none.
- Assistant items may also carry `model`, `reasoning_content`, `tool_calls`, and `timings`; tool items may carry `tool_call_id`. These are stored as sent.

### Conversation group

```json
{
  "id": "2d3e4f5a-6b7c-4d8e-9f0a-1b2c3d4e5f6a",
  "object": "conversation_group",
  "name": "Work",
  "created_at_ms": 1743180000000,
  "updated_at_ms": 1743180000000,
  "version": 1
}
```

### List envelope

List routes answer with OpenAI's list envelope. Lists come back whole, so `has_more` is always `false`.

```json
{ "object": "list", "data": [], "first_id": null, "last_id": null, "has_more": false }
```

## Conversations

### Create a conversation

Required: `id` (a lowercase UUID v4) and `name`. Optional: `pinned`, `group_id`, `settings`, `metadata`, and `fork_from` to copy items from another chat.

```bash
curl http://127.0.0.1:11434/v1/conversations \
  -H "Authorization: Bearer $PICO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d",
    "name": "My chat"
  }'
```

To fork another chat, send `fork_from` with the source `conversation_id`, the `item_id` to copy down to, and an optional `include_attachments` (default `false`):

```json
{
  "id": "3e4f5a6b-7c8d-4e9f-a0b1-2c3d4e5f6a7b",
  "name": "Forked chat",
  "fork_from": {
    "conversation_id": "0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d",
    "item_id": "1c2d3e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f",
    "include_attachments": false
  }
}
```

### Update a conversation

A partial update: an omitted field stays, and `null` clears it. `settings` is patched per key, where a `null` value removes that key. Accepts `name`, `pinned`, `group_id`, `current_item_id`, `settings`, `metadata`, and `if_version`.

```bash
curl http://127.0.0.1:11434/v1/conversations/0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d \
  -H "Authorization: Bearer $PICO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "name": "Renamed chat", "pinned": true }'
```

### Delete a conversation

Deletes the chat and its items for good. The `forks` query parameter decides what happens to its forks: `keep` (the default) hands each direct fork the deleted chat's own fork origin; `delete` removes the forks too. The answer lists every conversation that was removed in `deleted_ids`.

```bash
curl -X DELETE "http://127.0.0.1:11434/v1/conversations/0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d?forks=keep" \
  -H "Authorization: Bearer $PICO_API_KEY"
```

## Items

### List items

Returns every item on every branch, earliest first. The first release has no other listing, so the `branches=all` query parameter is required.

```bash
curl "http://127.0.0.1:11434/v1/conversations/0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d/items?branches=all" \
  -H "Authorization: Bearer $PICO_API_KEY"
```

### Add items

All items land, or none do. Each item needs `id`, `role`, `message_type`, `content` (one `input_text` or `output_text` part), and `timestamp_ms`; `parent_id` is required for every item except the root.

```bash
curl http://127.0.0.1:11434/v1/conversations/0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d/items \
  -H "Authorization: Bearer $PICO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "items": [
      {
        "id": "1c2d3e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f",
        "role": "user",
        "message_type": "text",
        "content": [{ "type": "input_text", "text": "Hello" }],
        "timestamp_ms": 1743180000000
      }
    ]
  }'
```

### Edit an item

A partial edit. A new `parent_id` moves the item. An item's `id`, `role`, and `message_type` can't change; `content` and `timestamp_ms` can't be cleared.

### Delete an item

Without `cascade=true`, an item that has children is refused with `409 has_children`. The answer is the conversation (whose `current_item_id` may have moved) with `deleted_ids`.

```bash
curl -X DELETE "http://127.0.0.1:11434/v1/conversations/0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d/items/1c2d3e4f-5a6b-4c7d-8e9f-0a1b2c3d4e5f?cascade=true" \
  -H "Authorization: Bearer $PICO_API_KEY"
```

## Groups

Groups organize chats in the sidebar. Create one with a client-made `id` and a `name`; rename it by posting a new `name` to its path; delete it to ungroup its chats (the chats stay).

```bash
curl http://127.0.0.1:11434/v1/conversation_groups \
  -H "Authorization: Bearer $PICO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "id": "2d3e4f5a-6b7c-4d8e-9f0a-1b2c3d4e5f6a",
    "name": "Work"
  }'
```

## Change events

`GET /v1/conversation_events` streams the caller's change notices as Server-Sent Events until the client hangs up or the server stops. A notice names *what* changed, never the data, so a client reloads what it shows whenever a stream opens — nothing is replayed. A keep-alive comment comes first and then every 15 seconds.

```bash
curl -N http://127.0.0.1:11434/v1/conversation_events \
  -H "Authorization: Bearer $PICO_API_KEY"
```

Each record's `event:` is one of `conversation.changed`, `conversation.deleted`, `group.changed`, or `group.deleted`, and its `data:` is one line of JSON:

```text
event: conversation.changed
data: {"origin_client_id":"window-1","conversation_id":"0b9f3c2a-1d4e-4a6b-8c7d-2e1f0a9b8c7d","last_modified_ms":1743180000000,"version":2}
```

Every route that saves a change publishes to the account's open streams. To let a client skip the notices its own writes cause, send a window identifier in the `X-Pico-Client-Id` request header on write requests; the matching notice echoes it as `origin_client_id` (otherwise `null`).

## Errors

Errors use OpenAI's envelope, `{"error": {"message", "type", "param", "code"}}`. A `stale_version` error also carries a top-level `current` with the record as it stands now.

| Status | `code` | Meaning |
| --- | --- | --- |
| `400` | `invalid_request` | Bad request shape or body |
| `400` | `invalid_id` | An `id` is not a lowercase UUID v4 |
| `400` | `unsupported_parameter` | Listing items without `branches=all` |
| `400` | `invalid_parent` | An item's `parent_id` is not a valid parent |
| `401` | `invalid_api_key` | Missing or invalid token |
| `403` | `permission_denied` | The account can't own chats (not a person) |
| `404` | `not_found` | No such record for this account |
| `409` | `id_exists` | The `id` is already in use |
| `409` | `stale_version` | `if_version` did not match |
| `409` | `has_children` | Deleting an item with children without `cascade=true` |
| `501` | — | User accounts are off, so conversations aren't stored |

## Edge cases
- These routes are off unless user accounts are enabled; otherwise they answer `501`.
- Clients mint every `id`. There is no server-assigned ID to read back.
- `children_ids` is server-derived; sending it in an item is rejected.
- List responses always report `has_more: false`; the whole list is returned.
