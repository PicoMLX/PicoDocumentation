---
title: Set Up a Mac Cluster
sidebar_position: 1
---

Mac Cluster connects two Apple silicon Macs so they run a model together. Use it to run a model that is too large for one Mac's memory, or to share the work across both machines. This page walks through turning the feature on, connecting the two Macs, and reading the setup checklist until the cluster is ready.

A cluster is always **two Macs**: the one you set it up on and one other Mac on the same network. Both Macs run Pico AI Server, and both must be on the **same build** of the app.

## Before you start

You need:

- **Two Apple silicon Macs**, each running Pico AI Server.
- **The same version of Pico AI Server on both Macs.** If the versions differ, the setup checklist shows `Update Pico on both Macs to use them together`.
- **A Thunderbolt cable between the two Macs.** This is the recommended connection. For best performance, use **Thunderbolt 5** when both Macs support it. A cluster can also form over a shared network (Ethernet or Wi‑Fi), but those links are slower.
- For the fastest link, **macOS 26.2 or later** on both Macs, which adds RDMA over Thunderbolt. On older macOS there is nothing to switch on, and you can still create the cluster without RDMA.

The Cluster tab shows a small requirements grid with one column for **This Mac** and one for the other Mac, so you can confirm each item is met on both:

| Requirement | What it means |
| --- | --- |
| Thunderbolt 5 | The connected port is Thunderbolt 5. |
| RDMA turned on | RDMA over Thunderbolt is available and enabled (macOS 26.2+). |
| Port has its own IP address | The connected Thunderbolt port has its own IP address (it is not held by Thunderbolt Bridge). |

The grid's **Cable** row reads `Port N · X Gb/s` when a cable is connected, or `Not connected` when it is not.

## Turn on Mac Cluster

1. Open Pico AI Server settings and select the **Cluster** tab.
2. Turn on the **Mac Cluster** switch (labeled *Run larger models with two Macs*).
   When the switch is off, the tab explains: *Connect two Macs with a Thunderbolt cable. For best performance, use Thunderbolt 5 when both Macs support it.*
3. Turn on **Mac Cluster** on the other Mac too, the same way.

With the switch on, the tab shows a 3D view of the two Macs and a **setup checklist** below them. The checklist is titled **Set up your cluster** and changes to **Cluster ready** once every step is complete. Work down the checklist — each row shows the one thing to do next, with a button when there is an action to take.

## Connect the two Macs

1. **Connect the Thunderbolt cable.**
   The 3D view turns to face the port to use and shows where the cable goes. On a MacBook it points to the correct left or right side; on a Mac Studio it highlights an eligible front port. Insert the cable into the highlighted port on each Mac.
2. **Find the other Mac.**
   Once both Macs run Pico with Mac Cluster on, each one appears to the other. If only one other Mac is found, its name is shown directly. If several are found, choose the one you want under the Mac picker.
3. **Create the cluster.**
   Select **Create Cluster**. If RDMA is not available yet, you can instead select **Create Without RDMA** to proceed over the slower link.
4. **Confirm the pairing on the other Mac.**
   - **Over Thunderbolt**, the other Mac shows a prompt: *"…" wants to add this Mac to its cluster.* Choose **Join** on that Mac. (Joining shares that Mac's memory and processing power with the cluster.)
   - **Over a shared network**, the other Mac displays a six‑digit code. Enter that code on the Mac that started the cluster to verify the connection.

When pairing succeeds, the checklist advances through the remaining steps on its own.

## Finish RDMA setup (fastest link)

For the fastest link, each Mac's Thunderbolt port needs RDMA turned on and its own IP address. The checklist guides these steps and provides buttons such as **Open Network Settings** where a change is needed:

- **Turn on RDMA** on each Mac (macOS 26.2+). On older macOS the checklist shows **Update macOS** instead, and this step does not block creating the cluster.
- **Remove the port from Thunderbolt Bridge.** If the connected port is held by Thunderbolt Bridge, it cannot get its own IP address. In **Network settings → Manage Virtual Interfaces**, remove the port from the bridge. Turning the bridge's service off is not enough.
- **Give the port a network service with an IP address.** The checklist reports when the port still has no address of its own and points you to Network settings.

When every step is complete, the checklist reads **Cluster ready** and the chosen model loads across both Macs.

## Performance considerations

Below the checklist, the Cluster tab lists **Performance considerations** — a plain list of things that affect speed without blocking setup. For example, a slower‑than‑expected link (a Thunderbolt 4 cable between two Thunderbolt 5 Macs), or another Mac with less memory or a different chip than this one. These are advisories: the cluster still works, but it may run slower.

## Reconnect and recover

- **Disconnect:** While a cluster is active, use **Disconnect** on either Mac to leave it. Pico releases the connection cleanly so you can create a cluster again without reopening the app.
- **Try again:** If preparing the cluster fails, the checklist keeps the specific reason and offers **Try Again** once both Macs report they are ready. Retrying still starts a fresh join.
- **Reopen both Macs:** Clearing a connection cannot interrupt a link or collective that is already stuck. If cleanup cannot finish safely, the checklist offers **Show Instructions**, which tells you to *quit Pico Server on both Macs, then reopen it and create the cluster again.*

Run the same, current build of Pico AI Server on both Macs for the most reliable setup and recovery.

## Troubleshooting

- **`Turn on Mac Cluster on that Mac to add it`** — The other Mac runs Pico but has Mac Cluster switched off. Turn the switch on there.
- **`Couldn't reach "…". Is Pico open on that Mac?`** — Pico is not reachable on the other Mac. Make sure Pico AI Server is open and running on it.
- **`Update Pico on both Macs to use them together`** — The two Macs run different, incompatible versions. Install the same build on both.
- **Cable shows `Not connected` or carries no network** — Check that the cable is seated in the highlighted Thunderbolt port on both Macs. A cable plugged into a MacBook's charger port, not a Mac, is not a cluster link.
- **Link slower than expected** — If both Macs have Thunderbolt 5 but the link is slow, the cable is most likely Thunderbolt 4; swap in a Thunderbolt 5 cable. If a non‑Thunderbolt‑5 port is in use while a faster one is free, move the cable to the Thunderbolt 5 port.
