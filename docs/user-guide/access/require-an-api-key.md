---
title: Require an API Key
sidebar_position: 1
description: Manage Pico AI Server user accounts and require an API key so only authorized clients can reach the server and its models.
---

By default, Pico AI Server accepts every request as a built-in user, so anyone who can reach the server can use it and its models. When you share the server on a LAN, turn on **Require API key** and give each person their own user account and key. This page covers the **Users** settings tab: requiring keys, adding users, and managing their keys.

Enforcement is off until you turn it on. While it is off, API keys can exist but are not checked, and every request is served as the built-in user.

## Require an API key

1. Open **Settings** in Pico AI Server.
2. Select the **Users** tab.
3. Add at least one user first (see below). You need an *enabled* user that has an API key before enforcement can be turned on.
4. In the **Authentication** section, turn on **Require API key**.
   With it on, every API request must include an enabled user's API key. With it off, keys are accepted but not required, and requests run as the built-in user.

## Add a user

1. In the **Users** tab, click **Add User**.
2. Enter a **First name** and **Email** (both required); **Last name** is optional.
3. Click **Add**.
   Pico generates an API key and shows it once in a confirmation sheet. **Copy** it there, or use **Send invite email** to send the person their server address and key. You can find the key again later in the Users tab.

## Manage a user's key

Each row in the **Users** table has an actions menu (**…**):

- **Send invite email…** — open a pre-filled email with the server address and the user's key.
- **Regenerate API key…** — issue a new key. The old key stops working immediately, so anywhere it is saved (chat clients, scripts) must be updated.
- **Disable** / **Enable** — turn a user's access off or back on without deleting them.
- **Delete…** — remove the user and revoke their key immediately.

To read or copy an existing key, use the show/hide (eye) and copy buttons in the **API key** column. Admin users are marked with a key icon next to their name.

## How clients authenticate

When **Require API key** is on, each request must carry the key in one of two headers:

```bash
# Standard bearer token
curl http://127.0.0.1:11434/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"

# X-API-Key (for Anthropic-style SDKs)
curl http://127.0.0.1:11434/v1/models \
  -H "X-API-Key: YOUR_API_KEY"
```

The browser WebUI and other static assets, `HEAD /` reachability checks, and CORS preflight (`OPTIONS`) requests are exempt, so the root chat page keeps loading. A request that is missing a key, or carries an invalid, disabled, or malformed one, gets `401 Unauthorized`.

## Verify it worked

With **Require API key** on, a request without a valid key is rejected, and a request that includes an enabled user's key succeeds:

```bash
# Rejected: no key -> 401
curl -i http://127.0.0.1:11434/v1/models

# Accepted: with an enabled user's key
curl http://127.0.0.1:11434/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Troubleshooting

- **Symptom:** You cannot disable or delete a user.
  **Cause:** While **Require API key** is on, Pico will not let you disable or delete the last enabled user that has a key — that would lock every client out.
  **Fix:** Add or enable another user with a key first, or turn off **Require API key** before removing the last one.
- **Symptom:** **Require API key** shows a warning and refuses to stay on.
  **Cause:** No enabled user has an API key.
  **Fix:** Add a user, or enable one, then turn the setting on.
- **Symptom:** A client that worked yesterday now gets `401 Unauthorized`.
  **Cause:** The key was regenerated, or the user was disabled or deleted.
  **Fix:** Issue the client a current key from an enabled user.

## Next steps

- [Enable Built-in Tools](../enable-built-in-tools.md)
- [LAN Sharing Basics](../networking/lan-sharing-basics.md)
- [Connect a Client](../getting-started/connect-a-client.md)
