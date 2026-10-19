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
2. Click `Add` next to it.
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

- **Direct Thunderbolt link (fastest).** When both Macs report that they can move data directly over Thunderbolt — in practice, a recent version of Pico on each and a Thunderbolt 5 connection between them — the cluster sends model data over that direct link (RDMA). This is the fastest option and the one to aim for.
- **Ethernet or Wi‑Fi.** Otherwise the cluster runs over TCP: over a network instead of a direct cable, or whenever either Mac doesn't report the direct path. It still works, just slower.

Both Macs decide from the same information, so they always pick the same link: if either can't take the direct path, the two use TCP together.

Pairing comes first, and it needs a compatible, recent version of Pico on both Macs. A Mac running a version that predates this won't pair with a newer one at all — you'll see `Update Pico on both Macs`, and the two won't cluster until both run a matching version. This is a refusal to pair, not a slower cluster.

Once both Macs commit to the direct Thunderbolt link, there's no silent retreat to the network. If that link can't be established, adding the Mac fails with the connection error rather than quietly continuing over TCP.

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
- **Symptom:** The two Macs are cabled over Thunderbolt 5, but adding the Mac fails with a connection error.
  **Cause:** The direct Thunderbolt (RDMA) link couldn't be established, and the cluster doesn't fall back to the network on its own.
  **Fix:** Reseat the Thunderbolt 5 cable, make sure both Macs run the same recent version of Pico, and add the Mac again.

:::caution
Mac Cluster works best with two Macs that have the same chip and memory. If the Macs have different memory, the cluster uses the same amount from each Mac (the smaller Mac's), and overall speed follows the slower Mac.
:::

## Next steps

- [Bonjour Discovery](./bonjour-discovery.md)
- [LAN Sharing Basics](./lan-sharing-basics.md)
