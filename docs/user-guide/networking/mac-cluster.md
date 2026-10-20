---
title: Mac Cluster
sidebar_position: 4
---

Mac Cluster joins two Macs running Pico AI Server so they act as one. The two Macs share a single model — so a model too large for one Mac can fit — and both Macs work on every response together, up to twice as fast. You turn it on in `Settings` → `Cluster`.

Mac Cluster works best with two Macs that have the same chip and memory, connected by a Thunderbolt 5 cable. Ethernet and Wi‑Fi also work, but are slower.

Two things to know before you start:

- Mac Cluster finds other Macs over the same Bonjour advertisement that clients use, so each Mac must have its server running with `Allow local network connections` and `Enable Bonjour broadcasting` turned on.
- The Mac you add *from* becomes the cluster's server (the host); the Mac you add lends its memory and chip (the member). Clients keep connecting to the host at port `11434`, exactly as before.

## Prepare both Macs

1. Install and run Pico AI Server on both Macs.
2. On each Mac, open the native app settings, turn on `Allow local network connections`, turn on `Enable Bonjour broadcasting` (under `Advanced` in `General`), and click `Apply Changes`.
3. On the Mac that will host, choose a default model in `Models`. The host runs its default model on both Macs.
4. Download that same model on both Macs. The cluster can only run a model that is present on both.
5. For the fastest link, connect the two Macs with a Thunderbolt 5 cable. Ethernet and Wi‑Fi also work.

## Turn on Mac Cluster

1. On each Mac, open `Settings` → `Cluster`.
2. Turn on the `Mac Cluster` switch.

When it is on, `This Mac` shows this Mac's model, chip, and memory, and the other Macs running Pico appear under `Nearby Macs`.

## Add the other Mac

Do this on the Mac you want to be the host.

1. Open `Settings` → `Cluster`. The other Mac appears under `Nearby Macs`.
2. Click `Add` next to it. The row reads `Connecting…` while Pico reaches the other Mac, then `Waiting for an answer on that Mac…` once the request gets there. If Pico can't reach the Mac within ten seconds, the row returns to `Add` so you can try again — it never hangs.
3. Confirm the pairing on the other Mac:
   - Over a direct Thunderbolt cable, the other Mac shows a prompt that reads `"<name>" wants to add this Mac to its cluster`. Click `Join` on that Mac.
   - Over Ethernet or Wi‑Fi, the other Mac shows a six‑digit code. Type that code on the host Mac. This confirms you are adding the Mac in front of you. After three wrong codes, the request is declined and you start over.
4. Once the Mac joins, the host loads its default model on both Macs. The model row reads `Loading … on both Macs…`, then `… runs on both Macs`.

## Verify it worked

On both Macs, `Settings` → `Cluster` shows `In This Cluster` with both Macs, the link between them (for example, `Thunderbolt`), and a model row that reads `<model> runs on both Macs`. The host also shows how much memory the pair has for models.

You can confirm the shared model answers from the host. On the host Mac:

```bash
curl http://127.0.0.1:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "YOUR_DEFAULT_MODEL_ID",
    "messages": [{"role": "user", "content": "Say hello from the cluster."}]
  }'
```

Replace `YOUR_DEFAULT_MODEL_ID` with the host's default model ID. A normal chat completion comes back; the work behind it is now split across both Macs.

To confirm a Mac is advertising itself for clustering, browse and resolve the Pico service from another Mac:

```bash
dns-sd -L "SERVICE_NAME" _pico._tcp local
```

Replace `SERVICE_NAME` with the name reported by `dns-sd -B _pico._tcp`. While Mac Cluster is on, the TXT record carries extra keys — `Cluster`, `ClusterVersion`, `ClusterPort`, `Chip`, and `MemoryGB` — alongside the usual discovery fields.

## How the two Macs connect

You don't choose how the Macs talk to each other, and the app doesn't show it: Pico picks the fastest link the two Macs share and uses it on its own. The `In This Cluster` panel reports the physical connection (for example, `Thunderbolt`), not the transport underneath it.

- **Direct Thunderbolt link (fastest).** When both Macs report that they can move data directly over Thunderbolt, the cluster sends model data over that direct link (RDMA). This is the fastest option and the one to aim for. It takes a recent version of Pico on each Mac, macOS 26.2 or later on both, a Thunderbolt 5 cable between them, and RDMA turned on — see [Get the fastest link](#get-the-fastest-link) below.
- **Ethernet or Wi‑Fi.** Otherwise the cluster runs over TCP: over a network instead of a direct cable, or whenever either Mac doesn't report the direct path. It still works, just slower.

Both Macs decide from the same information, so they always pick the same link. If either can't take the direct path, they pair over TCP instead. If both can but the direct link fails to start, pairing stops with a connection error rather than retrying over TCP.

Pairing comes first, and the two Macs must run compatible versions of Pico — ones new enough to speak the same cluster protocol. A Mac too old to pair with a newer one shows `Update Pico on both Macs to use them together`; update the older Mac and add it again.

### Get the fastest link

The `Thunderbolt` section in `Settings` → `Cluster` tells you whether this Mac is ready for the direct RDMA link and, when it isn't, names the one thing to do next. When a step needs a change outside Pico, the section shows a button that opens the right macOS settings for you.

For the direct link, both Macs need all of the following. The section walks you through them roughly in this order:

- A Thunderbolt 5 cable connecting the two Macs.
- macOS 26.2 or later (RDMA is not available on earlier macOS).
- RDMA turned on.
- A Thunderbolt network set up so the connection has an IPv4 address. Without one, Pico keeps the pair on TCP.

The section also reflects the other Mac: if that Mac still needs macOS updated or RDMA turned on, it says so, and it shows `waiting for the other Mac` until that Mac is ready. When everything is in place, it reports that the pair is ready for the direct link, and a cluster you form then runs over RDMA.

## Staying awake

While a Mac is in a cluster — as host or member — Pico keeps it from falling asleep on its own, so the shared model stays loaded and a long response isn't cut off partway. In `General` settings, `Prevent automatic sleep while Pico is running` shows as on and dimmed for as long as the cluster lasts, with the note `This Mac stays awake while it's in a cluster.` Your saved choice isn't changed: when you leave the cluster, or quit Pico, the Mac's normal sleep behavior returns.

This covers idle sleep only. Choosing `Sleep` from the Apple menu, or closing a laptop's lid, still puts the Mac to sleep.

## Leave or remove the cluster

- On the host, click `Remove "<member>"` to end the cluster.
- On the member, click `Leave Cluster`.

Pico forms a cluster only once per launch. After you leave or remove a cluster, quit and reopen Pico on both Macs before clustering again. If you try without relaunching, you see `Pico has already run a cluster since it was opened. Quit and reopen Pico on both Macs to cluster again.`

## Troubleshooting

- **Symptom:** `Other Macs can't find this Mac`.
  **Cause:** This Mac's server is not advertised.
  **Fix:** Start the server, turn on `Allow local network connections`, turn on `Enable Bonjour broadcasting`, and click `Apply Changes`.
- **Symptom:** The other Mac does not appear under `Nearby Macs`.
  **Cause:** Mac Cluster is off on that Mac, or there is no shared network path.
  **Fix:** Turn on Mac Cluster on that Mac, and connect the two Macs with Thunderbolt or put them on the same LAN.
- **Symptom:** The other Mac shows `In another cluster`.
  **Cause:** That Mac is already hosting or is a member of another cluster.
  **Fix:** Leave that cluster first, then add the Mac again.
- **Symptom:** The row reads `Couldn't reach "<name>". Is Pico open on that Mac?`.
  **Cause:** Pico could not connect to the other Mac within ten seconds — usually because Pico isn't running there, or that Mac's address changed.
  **Fix:** Make sure Pico is open on the other Mac, then click `Add` again to retry with its current address.
- **Symptom:** The code is rejected.
  **Cause:** The digits do not match the ones shown on the added Mac.
  **Fix:** Re‑read the code on that Mac and type it again. After three wrong tries the request is declined.
- **Symptom:** The model will not load on both Macs.
  **Cause:** The host has no default model, or the model is not downloaded on both Macs.
  **Fix:** Set a default model on the host and download the same model on both Macs.
- **Symptom:** `Update Pico on both Macs to use them together`.
  **Cause:** The two Macs run different, incompatible Pico versions.
  **Fix:** Update Pico to the same version on both Macs.
- **Symptom:** `Thunderbolt cable disconnected` or `Connection lost`.
  **Cause:** The link between the Macs dropped.
  **Fix:** Reconnect the Thunderbolt cable, or bring the other Mac back onto the network. The cluster is restored when the other Mac is reachable again.
- **Symptom:** The pair runs over TCP even with a Thunderbolt 5 cable between the Macs.
  **Cause:** One of the direct-link requirements isn't met on one of the Macs — macOS older than 26.2, RDMA off, or no IPv4 address on the Thunderbolt network.
  **Fix:** Open the `Thunderbolt` section in `Settings` → `Cluster` on each Mac and follow the step it names. See [Get the fastest link](#get-the-fastest-link).

:::caution
Mac Cluster works best with two Macs that have the same chip and memory. If the Macs have different memory, the cluster uses the same amount from each Mac (the smaller Mac's), and overall speed follows the slower Mac.
:::

## Next steps

- [Bonjour Discovery](./bonjour-discovery.md)
- [LAN Sharing Basics](./lan-sharing-basics.md)
