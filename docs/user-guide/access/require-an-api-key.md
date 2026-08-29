---
title: Require an API Key
sidebar_position: 1
description: Manage Pico AI Server user accounts and require an API key so only authorized clients can reach the server and its models.
---

By default, Pico AI Server accepts every request as a built-in user, so anyone who can reach the server can use it and its models. When you share the server on a LAN, turn on **Require API key** and give each person their own user account and key. This page covers the **Users** settings tab: requiring keys, adding users, and managing their keys.

Enforcement is off until you turn it on. While it is off, API keys can exist but are not checked, and every request is served as the built-in user.

:::caution
Requiring a key controls **who** can use the server; it does not encrypt traffic. Pico AI Server serves plain `http://`, so a key travels over the network unencrypted, and an untrusted device on the same LAN could capture and replay it. Turn on LAN access only on a network you trust, and regenerate any key you believe was exposed.
:::

## Require an API key

1. Open **Settings** in Pico AI Server.
2. Select the **Users** tab.
3. Add at least one user first (see below). You need an *enabled* user that has an API key before enforcement can be turned on.
4. In the **Authentication** section, turn on **Require API key**.
   With it on, every API request must include an enabled user's API key. With it off, any key on a request is ignored and every request runs as the built-in user.

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

:::caution
An API key is a credential: it authorizes every request made on the user's behalf until you regenerate it. **Send invite email** puts the key in an ordinary email, so anyone who receives or forwards that message can use it. Share keys only through a trusted channel, and **regenerate** a user's key immediately if you suspect it was exposed.
:::

## How clients authenticate

When **Require API key** is on, each request must carry an enabled user's key in one of two headers — `Authorization: Bearer <key>` or `X-API-Key: <key>` (the `X-API-Key` form is for Anthropic-style SDKs). A request that is missing a key, or carries an invalid, disabled, or malformed one, gets `401 Unauthorized`.

Only the static WebUI shell is exempt: the root page, other static assets, `HEAD /` reachability checks, and CORS preflight (`OPTIONS`) requests load without a key, so the chat page still opens. The model and chat API requests that page makes are **not** exempt — they need a key like any other client, so configure the WebUI with a key when enforcement is on, or its requests get `401`.

## Try it now

Replace `YOUR_API_KEY` with a real key from the **Users** tab — copy it from the **API key** column, or from the sheet shown when you add or regenerate a user. Then send an authenticated request:

```bash
curl http://127.0.0.1:11434/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

You get the model list back as JSON.

## Verify it worked

With **Require API key** on, a request without a valid key is rejected, and the same request with an enabled user's key succeeds:

```bash
# Rejected: no key -> 401
curl -i http://127.0.0.1:11434/v1/models

# Accepted: with an enabled user's key (replace YOUR_API_KEY)
curl http://127.0.0.1:11434/v1/models \
  -H "Authorization: Bearer YOUR_API_KEY"
```

## Troubleshooting

- **Symptom:** You cannot disable or delete a user, and the message is about the last enabled key holder.
  **Cause:** While **Require API key** is on, Pico will not let you disable or delete the last enabled user that has a key — that would lock every client out.
  **Fix:** Add or enable another user with a key first, or turn off **Require API key** before removing the last one.
- **Symptom:** You cannot disable or delete a user, and the message says it is the last admin.
  **Cause:** This is a separate guard from the key requirement. Pico keeps at least one enabled administrator (admins are marked with a key icon), so it can block the change even when another enabled non-admin user still has a key.
  **Fix:** Make sure another enabled administrator account remains before you disable or delete this one.
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
