---
title: Mac Cluster
sidebar_position: 4
---

A Mac Cluster links two Macs so they run larger models faster than one Mac could alone. One Mac is the **host** (the main Mac) and the other is a **member** (a worker). While a Mac is a member, the host answers every request sent to the member, so a client can connect to either Mac and reach the same models.

Two things to know before you start: clustering needs a Thunderbolt cable between the two Macs, and a member's own user accounts and API keys stop working until it leaves the cluster — the host checks every sign-in against its own accounts.

## Set up a cluster

You can start clustering from the setup wizard's `Enable Clustering` step, or at any time from the native app settings.

1. Connect the two Macs with a Thunderbolt cable. For best performance, use Thunderbolt 5 when both Macs support it, and use Macs with the same chip and memory.
2. On both Macs, open the native app settings and turn on the `Mac Cluster` toggle (`Run larger models faster with two Macs`).
3. On the host, select the other Mac and click `Create Cluster`.
4. Verify the pairing code. One Mac shows a code; enter the same code on the other Mac to confirm you are pairing the right machines.
5. On the member, accept the invitation. The member is told what joining means — that the host will answer every request sent to this Mac, and, when user accounts are on, that this Mac's accounts and API keys will not work until it leaves the cluster — then click `Join`.

On a Thunderbolt 5 Mac, clustering requires RDMA, which transfers data directly between Macs over Thunderbolt 5. If RDMA is off, the app points you to the setting to turn it on. A Mac without Thunderbolt 5 can still join a cluster without RDMA, but transfers may be slower.

## How a cluster answers requests

A member forwards every request it receives to the host, unchanged, and streams the host's reply straight back:

- The member passes your request to the host exactly as received, including the `Authorization` and `X-API-Key` headers. The host checks the sign-in against its own accounts and answers. Authenticate with the **host's** API key, not the member's.
- Streamed responses stay streamed. Server-sent event tokens arrive through the member as the host generates them.
- A member keeps advertising itself over Bonjour, so clients that discover it still reach the host through it.

If the host cannot be reached, the member returns an error that names the host, in the shape of the request's API — OpenAI by default, or Ollama for `/api/` paths:

- **503** — the host could not be found over Bonjour.
- **502** — the host was found but did not answer (within about 5 seconds).

To restore a member's own accounts, API keys, and models, leave the cluster from its `Mac Cluster` settings.

## Verify it worked

From a client, send a request to the **member's** address and confirm the host answers it. For example, list the models the host serves:

```bash
curl http://MEMBER_ADDRESS:11434/v1/models
```

Replace `MEMBER_ADDRESS` with the member Mac's host name or IP address. The response lists the host's models, not the member's. A chat request sent to the member is likewise answered by the host:

```bash
curl http://MEMBER_ADDRESS:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer HOST_API_KEY" \
  -d '{
    "model": "MODEL_ID",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

## Troubleshooting

- **Symptom:** A request to a member returns `503`.
  **Cause:** The member cannot find the host over Bonjour.
  **Fix:** Confirm the host is running and that both Macs are on a network that allows Bonjour (multicast DNS), then retry.
- **Symptom:** A request to a member returns `502`.
  **Cause:** The host was found but did not answer in time.
  **Fix:** Confirm the host is running and reachable, then retry.
- **Symptom:** A client's API key or account suddenly stops working against one Mac.
  **Cause:** That Mac joined a cluster, so the host's accounts now apply.
  **Fix:** Use the host's API key, or have the admin remove that Mac from the cluster to restore its own accounts and keys.

:::caution
A member's own accounts and API keys do not work while it is in a cluster. The host's accounts apply to every request the member forwards.
:::

## Next steps

- [Bonjour Discovery](./bonjour-discovery.md)
- [Connect a Client](../getting-started/connect-a-client.md)
