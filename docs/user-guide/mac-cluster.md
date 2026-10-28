---
title: Mac Cluster
sidebar_position: 5
description: Combine two Macs into one Pico AI Server to run larger models and generate responses faster, with the fastest link over Thunderbolt 5 RDMA.
---

Mac Cluster lets you **use two Macs as one**. Pico AI Server runs a single model across both machines at once, which gives you two things:

- **Run larger models.** The cluster combines the memory of both Macs, so you can load a model that is too large for either Mac on its own.
- **Up to twice as fast.** Both Macs process each response, so generation can be close to twice as fast as a single Mac.

For the best results, use **two Macs with the same chip and the same amount of memory, connected by Thunderbolt 5**. A cluster also works over Ethernet or Wi‑Fi, but those links are slower.

Mac Cluster is managed in Pico AI Server's settings, in the **Cluster** tab. You turn it on separately on each Mac, then add one Mac to the other.

## Before you start

- Pico AI Server installed and running on **both** Macs, with the **same version** on each.
- A way to connect the two Macs. A **Thunderbolt** cable is strongly preferred; the cluster also runs over the same local network (Ethernet or Wi‑Fi), more slowly.
- Both Macs on the same local network if you connect them over Wi‑Fi or Ethernet, so each can discover the other.

The fastest link, **RDMA over Thunderbolt**, has extra requirements. See [Get the fastest link: RDMA over Thunderbolt](#get-the-fastest-link-rdma-over-thunderbolt) below.

## Turn on Mac Cluster and add a second Mac

Do steps 1 and 2 on **both** Macs, then add one Mac to the other from a single Mac.

1. On each Mac, open **Settings** in Pico AI Server and select the **Cluster** tab.
2. Turn on the **Mac Cluster** switch.
3. Connect the two Macs with a **Thunderbolt** cable. (To cluster over the local network instead, make sure both Macs are on the same network and skip the cable.)
4. On one Mac, find the other Mac in the Cluster tab and click **Create Cluster** next to it.

   - If the Macs are joined over a **Thunderbolt** cable, a prompt appears on the other Mac asking to join the cluster. On that Mac, click **Join**.
   - If the Macs are connected over a **shared network**, the other Mac shows a six‑digit code. Type that code on the Mac that started the request to verify the connection.

Pico pairs the Macs and prepares the model on both machines.

### Verify it worked

In the Cluster tab (and in the menu bar item), the model row shows the model's state as the cluster forms:

- **Copying** the model to the other Mac, with a progress bar, if that Mac doesn't already have the same copy.
- **Loading … on both Macs** while the model starts.
- **… runs on both Macs** with a checkmark when the cluster is ready.

Once the model runs on both Macs, send a request to Pico AI Server as usual — the cluster serves it from both machines.

## Get the fastest link: RDMA over Thunderbolt

The fastest connection between two Macs is **RDMA over Thunderbolt**. When both Macs can use it, the cluster carries inference traffic directly over the Thunderbolt link instead of a standard network connection. (When RDMA isn't available, the cluster falls back to a TCP connection over whatever link the Macs share.)

RDMA over Thunderbolt needs all of the following, on **both** Macs. The Cluster tab shows a grid with one row per requirement and one column per Mac, so you can see at a glance what is still missing:

| Requirement | What it means |
|---|---|
| **Thunderbolt 5** | Both Macs have Thunderbolt 5, joined by a Thunderbolt 5 cable. A Thunderbolt 4 cable links at a lower speed. |
| **RDMA turned on** | RDMA over Thunderbolt is enabled. This requires **macOS 26.2 or later**; earlier versions of macOS have nothing to switch on. |
| **Port has its own IP address** | The Thunderbolt port used for the link has its own IPv4 address. |

Giving the Thunderbolt port its own IP address takes two steps in **System Settings → Network** when the port is part of a Thunderbolt Bridge:

1. Open **Manage Virtual Interfaces** and remove the Thunderbolt port from **Thunderbolt Bridge**. Turning the bridge's service off is not enough — the port has to be removed from the bridge.
2. Add a network service for the Thunderbolt port and make sure it is active and has an IPv4 address.

The Cluster tab's setup checklist walks you through each of these as a step, marks the ones that still need attention, and points out the matching steps on the other Mac. When every requirement is met on both Macs and the cable is a Thunderbolt 5 link, the cluster uses RDMA automatically.

## See the cluster in the menu bar

While this Mac is in a cluster, the Pico AI Server menu bar item shows a **Mac Cluster** section with:

- The other Mac and the link type (**Thunderbolt**, **Ethernet · Slower**, or **Wi‑Fi · Slower**).
- The model's state — copying, loading, or running on both Macs.
- A **Disconnect** button to leave the cluster.

Hold **Option** while opening the menu to add technical details: the Thunderbolt port and speed, the address each Mac uses, and whether the link is **RDMA over Thunderbolt (JACCL)** or **TCP (ring)**.

## Troubleshooting

- **The other Mac isn't listed.** Make sure Pico AI Server is running on it and that **Mac Cluster** is turned on in its Cluster tab. Over a shared network, both Macs must be on the same network for discovery to work.
- **"Update Pico on both Macs to use them together."** The two Macs are running different, incompatible versions. Update Pico AI Server so both run the same version.
- **"In another cluster."** A Mac can belong to only one cluster at a time. Disconnect it from its current cluster first.
- **The link shows as Ethernet or Wi‑Fi, not Thunderbolt.** Check that the Thunderbolt cable is seated at both ends and that it carries a network connection. A Thunderbolt 4 cable, or a port left in a Thunderbolt Bridge, can keep the Macs from using the Thunderbolt link.
- **RDMA stays off.** Confirm both Macs run macOS 26.2 or later, that RDMA is turned on, and that each Thunderbolt port has its own IPv4 address. The requirements grid in the Cluster tab shows which Mac is still missing a requirement.

## Related

- [LAN Sharing Basics](./networking/lan-sharing-basics.md)
- [Bonjour Discovery](./networking/bonjour-discovery.md)
