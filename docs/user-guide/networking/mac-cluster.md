---
title: Mac Cluster
sidebar_position: 4
---

Mac Cluster joins two Macs running Pico AI Server so they act as one. The two Macs share a single model — so a model too large for one Mac can fit — and both Macs work on every response together, up to twice as fast. You turn it on in `Settings` → `Cluster`.

Mac Cluster works best with two Macs that have the same chip and memory, joined by a Thunderbolt 5 cable. You create a cluster over a direct Thunderbolt cable between the two Macs.

Two things to know before you start:

- Mac Cluster finds other Macs over the same Bonjour advertisement that clients use, so each Mac must have its server running with `Allow local network connections` and `Enable Bonjour broadcasting` turned on.
- The Mac you create the cluster *from* becomes the cluster's server (the host); the Mac that joins lends its memory and chip (the member). Clients keep connecting to the host at port `11434`, exactly as before.

## Prepare both Macs

1. Install and run Pico AI Server on both Macs.
2. On each Mac, open the native app settings, turn on `Allow local network connections`, turn on `Enable Bonjour broadcasting` (under `Advanced` in `General`), and click `Apply Changes`.
3. On the Mac that will host, choose a default model in `Models`. The host runs its default model on both Macs.
4. On the host, download the model the cluster will run. You don't have to download it on the member: if the model is missing there, the host copies its own copy to the member over the cluster link when the cluster starts (see [Share the model across both Macs](#share-the-model-across-both-macs)). If the member already holds that model as a *different* download, the cluster won't run it until both Macs have the same copy.
5. Connect the two Macs with a Thunderbolt cable. For the fastest link, use Thunderbolt 5 ports on both Macs and a Thunderbolt 5 cable.

## Turn on Mac Cluster

1. On each Mac, open `Settings` → `Cluster`.
2. Turn on the `Mac Cluster` switch.

When it is on, the pane shows a single card. The card draws the two Macs and the link between them, above a title that names the one thing to do next and, below it, at most one button. Each Mac is labeled with its chip and memory, such as `M5 Max · 128 GB`; under `This Mac`, a second line shows this Mac's own Pico name — the name the other Mac sees it by — so you can tell two Macs' settings apart. The line between the Macs carries the link's symbol in its middle: Thunderbolt's bolt, marked `5` for a Thunderbolt 5 link (80 Gb/s or faster, or one ready for RDMA) and `4` for a slower one, or the Wi‑Fi or Ethernet symbol when the Macs pair over the network instead. The symbol takes the line's color, and the link's name — for example `Thunderbolt · 40 Gb/s` — sits just below the line. Before the two Macs are linked, the line is plain.

Until the other Mac is ready, the card's title tells you what to do next — for example `Open Pico on Your Other Mac`, `Turn On Mac Cluster on "<name>"`, `Connect Your Other Mac`, `Waiting for "<name>"`, or `Other Macs Can't Find This Mac` — each with a line under it that explains the step.

## Create the cluster

Do this on the Mac you want to be the host.

1. Connect the two Macs with a Thunderbolt cable, and turn on `Mac Cluster` on both.
2. When the other Mac is ready, the card reads `Ready to Create a Cluster`, with a line such as `Together: 256 GB for models, over Thunderbolt 5 with RDMA.` Click `Create Cluster`. If Pico finds more than one Mac, the card reads `Choose the Mac to create a cluster with.` and lists each Mac with its own `Create Cluster` button.
3. While Pico reaches the other Mac, the card reads `Connecting to "<name>"…` with the line `Accept the request on that Mac.` and a `Cancel` button. If Pico can't reach the Mac within ten seconds, the card returns to its ready state and shows `Couldn't reach "<name>". Is Pico open on that Mac?` — it never hangs.
4. On the other Mac, confirm the request. A prompt reads `"<name>" wants to add this Mac to its cluster`; click `Join`. (Click `Don't Join` to decline.)
5. Once the Mac joins, the host loads its default model on both Macs. The model row reads `Loading <model> on both Macs…`, then `<model> runs on both Macs`. If the member doesn't have the model, the host copies it over the cluster link first — the row reads `Copying <model> to "<member>"… 45%` on the host and `Copying <model> from "<host>"… 45%` on the member, with a progress bar — and loading continues once the copy finishes. See [Share the model across both Macs](#share-the-model-across-both-macs).

## Share the model across both Macs

Both Macs run the same model: the host runs its default model, and the member runs the host's copy of it. You only download the model on the host.

- **A missing model is copied for you.** When the member doesn't have the model, the host serves its own copy over the cluster link and the member downloads it automatically, using the same download machinery as any other model — so you see the usual progress and the member's free-disk check. The model row shows `Copying <model> to "<member>"… 45%` on the host and `Copying <model> from "<host>"… 45%` on the member, with a progress bar, then loading continues.
- **If the copy can't finish,** the start fails and the model row shows the reason — for example `Copying "<model>" from "<host>" failed: The model needs 40 GB, but only 12 GB is free on this Mac.` Clear the problem it names and create the cluster again. A copy isn't resumed across attempts: a new cluster starts it over.
- **Both copies must match.** When both Macs already have the model, Pico checks that the two copies match before running them together — it compares each Mac's `config.json` and weight files by name and size. If they differ, the member won't run the model and reports `"<member>" has a different copy of "<model>": its configuration or weight files don't match. Download it again on one of the Macs.` This is a structural check: a match means the two copies can run together, not that their weights are byte-for-byte identical. A copy Pico can't read fails the same way. Automatic copy only fills in a model the member is *missing* — it won't replace a different copy that's already there.

## Verify it worked

When the cluster is up, the card on both Macs shows the two Macs with the link between them (for example, `Thunderbolt`), a model row that reads `<model> runs on both Macs`, and a `Disconnect` button. The card's title reads how much memory the pair has for models, such as `256 GB for Models`. On the member, the card adds the line `This Mac lends its memory and chip to "<host>".`

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

You don't choose how the Macs talk to each other, and the app doesn't show it: Pico picks the fastest link the two Macs share and uses it on its own. The card reports the physical connection (for example, `Thunderbolt`), not the transport underneath it.

- **Direct Thunderbolt link (fastest).** When both Macs report that they can move data directly over Thunderbolt, the cluster sends model data over that direct link (RDMA). This is the fastest option and the one to aim for. It takes a recent version of Pico on each Mac, Thunderbolt 5 ports on both Macs joined by a Thunderbolt 5 cable, macOS 26.2 or later on both, and RDMA turned on — see [Set up RDMA](#set-up-rdma) below.
- **TCP over the cable.** Otherwise the cluster runs over plain TCP across the same Thunderbolt cable — whenever either Mac doesn't report the direct path. It still works, just slower.

Both Macs decide from the same information, so they always pick the same link. If either can't take the direct path, they pair over TCP instead. If both can but the direct link fails to start, pairing stops with a connection error rather than retrying over TCP.

Pairing comes first, and the two Macs must run compatible versions of Pico — ones new enough to speak the same cluster protocol. A Mac too old to pair with a newer one shows the card title `Update Pico`, with the line `"<name>" runs another version of Pico. Update Pico on both Macs.`; update the older Mac and create the cluster again.

### Set up RDMA

Pico checks each Mac against the direct-link requirements on its own and keeps the card on the next thing to fix until both Macs qualify. You don't open a separate screen for it.

For the direct link, both Macs need all of the following:

- **Thunderbolt 5 on both Macs:** each Mac needs Thunderbolt 5 ports, connected by a Thunderbolt 5 cable. A Mac with only Thunderbolt 4 ports can't take the direct link, even with a Thunderbolt 5 cable.
- **macOS 26.2 or later** (RDMA over Thunderbolt is not available on earlier macOS).
- **RDMA turned on,** then a restart. On macOS 27 or later, turn it on in `Privacy & Security` → `Developer Tools`. On earlier macOS, start up in macOS Recovery, choose `Utilities` → `Terminal`, enter `rdma_ctl enable`, and restart.
- **An IPv4 address on the Thunderbolt port.** The port the cable is in needs its own active network service, set to configure IPv4 using DHCP. Without one, Pico keeps the pair on TCP.

Both Macs must qualify: if the other Mac still needs macOS updated or RDMA turned on, the card waits on it. When everything is in place, the card reads `Ready to Create a Cluster` with the line `…over Thunderbolt 5 with RDMA.`, and a cluster you create then runs over RDMA. If you'd rather not wait, the card offers `Create Cluster Without RDMA` to form the cluster over TCP now.

## Work through setup from the card

You set up a cluster from the card alone: it always surfaces just the single next step, so you fix one thing at a time and the card moves on once it's done. It walks you through connecting the other Mac — opening Pico there, connecting the Thunderbolt cable, and creating the cluster — and, when RDMA applies, through the [RDMA requirements](#set-up-rdma) above. The card's title names the step, and the line under it explains what to do.

## See the cluster in the menu bar

While a Mac is in a cluster, the Pico menu bar icon carries a small link badge — like the chain link Personal Hotspot adds to the Wi‑Fi icon. If the two Macs can't reach each other, the link is slashed.

Open the menu bar item, and while this Mac is hosting or is a member it shows a `Mac Cluster` section between the server status and `Memory`:

- the other Mac's name and the link to it — for example `Thunderbolt 5 · RDMA` or `Thunderbolt · 80 Gb/s`, or `Disconnected` in orange when the link has dropped;
- the same title and detail as the Cluster settings card, such as `256 GB for Models` and `This Mac lends its memory and chip to "<host>".`;
- the model row — the same `<model> runs on both Macs` (or copy progress) you see in settings;
- a `Disconnect` button in the section header.

Hold Option while opening the menu to see the connection details: the Thunderbolt port, interface, and speed; both Macs' addresses; and whether the model's two halves talk over `RDMA over Thunderbolt (JACCL)` or `TCP (ring)`.

## Staying awake

While a Mac is in a cluster — as host or member — Pico keeps it from falling asleep on its own, so the shared model stays loaded and a long response isn't cut off partway. In `General` settings, `Prevent automatic sleep while Pico is running` shows as on and dimmed for as long as the cluster lasts, with the note `This Mac stays awake while it's in a cluster.` Your saved choice isn't changed: when you leave the cluster, or quit Pico, the Mac's normal sleep behavior returns.

This covers idle sleep only. Choosing `Sleep` from the Apple menu, or closing a laptop's lid, still puts the Mac to sleep.

## Leave the cluster

Click `Disconnect` on either Mac — the host or the member — to end the cluster.

Pico forms a cluster only once per launch. After you disconnect, quit and reopen Pico on both Macs before clustering again. If you try without relaunching, you see `Pico has already run a cluster since it was opened. Quit and reopen Pico on both Macs to cluster again.`

## Troubleshooting

- **Symptom:** The card reads `Other Macs Can't Find This Mac`.
  **Cause:** This Mac's server is not advertised.
  **Fix:** Start the server, turn on `Allow local network connections`, turn on `Enable Bonjour broadcasting`, and click `Apply Changes`.
- **Symptom:** The card reads `Open Pico on Your Other Mac` or `Turn On Mac Cluster on "<name>"`.
  **Cause:** Pico isn't open on the other Mac, or Mac Cluster is off there.
  **Fix:** Open Pico on the other Mac and turn on `Mac Cluster` in `Settings` → `Cluster`.
- **Symptom:** The card reads `"<name>" Is in Another Cluster`.
  **Cause:** That Mac is already hosting or is a member of another cluster.
  **Fix:** Disconnect that Mac from its cluster first, then create the cluster again.
- **Symptom:** The card reads `Couldn't reach "<name>". Is Pico open on that Mac?`.
  **Cause:** Pico could not connect to the other Mac within ten seconds — usually because Pico isn't running there, or that Mac's address changed.
  **Fix:** Make sure Pico is open on the other Mac, then click `Create Cluster` again to retry with its current address.
- **Symptom:** The model will not load on both Macs.
  **Cause:** The host has no default model, or its copy of the model can't be read to share it.
  **Fix:** Set a default model on the host and confirm it's downloaded there. The member doesn't need its own copy — the host copies the model over the cluster link when the cluster starts.
- **Symptom:** The member reports `"<name>" has a different copy of "<model>": its configuration or weight files don't match. Download it again on one of the Macs.`
  **Cause:** Both Macs have the model, but the downloads differ. Pico compares each copy's `config.json` and weight files before running and won't run two copies that don't match. (Automatic copy only fills in a model the member is *missing*; it won't replace a copy already there.)
  **Fix:** Download the model again on one of the Macs so both hold the same copy, then create the cluster again.
- **Symptom:** The model row reads `Copying "<model>" from "<host>" failed: …` with a reason.
  **Cause:** The member couldn't download the host's copy over the cluster link — most often too little free disk space, though the message names the actual problem.
  **Fix:** Clear the problem the message names (for example, free up disk space on the member), then create the cluster again.
- **Symptom:** The card reads `Waiting for "<name>"` with `Pico there hasn't been found over the cable yet.`
  **Cause:** You just connected the Thunderbolt cable. The two Macs have found each other over Wi‑Fi or Ethernet, but Pico hasn't been seen over the new cable yet.
  **Fix:** Wait a few seconds — Pico keeps checking and the card moves on once it finds the other Mac over the cable. After about half a minute it falls back to asking you to open Pico on the other Mac.
- **Symptom:** The card reads `Update Pico`.
  **Cause:** The two Macs run different, incompatible Pico versions.
  **Fix:** Update Pico to the same version on both Macs.
- **Symptom:** The card shows `Disconnected`.
  **Cause:** The Thunderbolt link between the Macs dropped.
  **Fix:** Reconnect the Thunderbolt cable. The cluster is restored when the other Mac is reachable again.
- **Symptom:** The pair runs over TCP even with a Thunderbolt 5 cable between the Macs.
  **Cause:** One of the direct-link requirements isn't met on one of the Macs — a Mac with only Thunderbolt 4 ports, macOS older than 26.2, RDMA off, or no IPv4 address on the Thunderbolt port.
  **Fix:** Work through the RDMA requirements on each Mac. See [Set up RDMA](#set-up-rdma).
- **Symptom:** The card reads `Thunderbolt Network Isn't Working`.
  **Cause:** macOS could not add the Thunderbolt port to its network bridge, so the cable has no working network even though it's plugged in.
  **Fix:** Restart that Mac. A restart usually lets macOS add the port back to the bridge.
- **Symptom:** The two Macs find each other, but the card says the Thunderbolt Bridge is off and asks you to turn it on.
  **Cause:** The Thunderbolt port is in a network bridge whose service is turned off. The Macs can still see each other over the bridge's IPv6 link-local address, but a shared model needs IPv4, so the cluster can't run that way.
  **Fix:** Turn the Thunderbolt Bridge on in `Network` settings. Note that turning the bridge *off* is not what RDMA needs — RDMA needs the port to have its own IP address instead, which is the separate step under [Set up RDMA](#set-up-rdma).

## Read the cluster logs

When a cluster won't form or a link drops, Mac Cluster records what it did to the app's log file at `Documents/logs/<date>.log` in the Pico AI Server container (one file per day). Each line reads `<timestamp> <level>: [<label>] <message>`, where the label names the component that logged it — for example `[PicoCore]`. Cluster messages carry the `Mac Cluster:` marker, so you can search the file for `Mac Cluster:` to find them; they note the Thunderbolt readings as they change, the Macs found and their links, which backend was chosen (RDMA or TCP), and membership changes. Quote the relevant lines when you report a clustering problem.

:::caution
Mac Cluster works best with two Macs that have the same chip and memory. If the Macs have different memory, the cluster uses the same amount from each Mac (the smaller Mac's), and overall speed follows the slower Mac.
:::

## Next steps

- [Bonjour Discovery](./bonjour-discovery.md)
- [LAN Sharing Basics](./lan-sharing-basics.md)
