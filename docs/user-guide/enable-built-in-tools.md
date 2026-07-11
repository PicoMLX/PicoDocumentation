---
title: Enable Built-in Tools
sidebar_position: 3
description: Turn on Pico AI Server's built-in tools, including the system info tool, and expose them to your models and to MCP clients.
---

Pico AI Server ships with **built-in tools** that a model can call during a conversation. When a tool-capable model decides it needs one, Pico AI Server runs the tool locally and feeds the result back into the model's answer — no external service required.

Built-in tools are separate from the tools you connect through the Model Context Protocol (MCP). MCP connects Pico to *external* servers; built-in tools run *inside* Pico AI Server. You manage built-in tools in the **Tools** tab, where you enable or disable them as needed; external MCP servers are managed in the **MCP** tab.

This page shows how to enable built-in tools and uses the **System Info** tool as the worked example. You need a version of Pico AI Server that includes the **Tools** settings tab, and a model that supports tool (function) calling.

## Enable a built-in tool

1. Open **Settings** in Pico AI Server.
2. Select the **Tools** tab.
3. Turn on the individual tools you want to make available to models.

Only enabled tools are offered to the model. A tool you leave off is never advertised, so a model cannot call it.

## The System Info tool

The **System Info** tool lets a model ask about the Mac it is running on. When enabled, the model can report details such as:

- **Hardware** — Mac model identifier, chip name, architecture, CPU core counts (total, performance, and efficiency), and thermal state
- **Memory** — physical RAM, an available-memory estimate, and MLX active, cache, and peak usage
- **Operating system** — name, version, and build
- **Host app** — Pico AI Server's name, version, and build

System Info ships enabled by default. You can turn it on or off in the **Tools** tab like any other built-in tool.

### Try it now

With a tool-capable model installed and the **System Info** tool enabled, ask a question that needs host details. From the Web Chat, or over the API:

```bash
curl http://127.0.0.1:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "MODEL_NAME",
    "messages": [
      { "role": "user", "content": "What Mac and chip am I running on, and how much RAM does it have?" }
    ]
  }'
```

Replace `MODEL_NAME` with the ID of an installed tool-capable model — list them with `GET /v1/models`.

The model calls the System Info tool and answers with your machine's model, chip, and memory instead of guessing.

### Verify it worked

- The reply names your actual Mac model, chip, and RAM — not a generic or made-up machine.
- With the **System Info** tool turned **off**, the same question can no longer be answered from live host data.

## Expose your tools to MCP clients

The **MCP** tab has an **Expose enabled tools to MCP clients** toggle. Turn it on to let external MCP clients reach the tools you have enabled, in addition to your own models using them during generation. A client connects to Pico's MCP endpoint at `http://SERVER:11434/mcp` (replace `SERVER` with the address you share, and `11434` if you changed the port), so it must be able to reach that endpoint on your network.

Your enabled tools — built-in tools included — are what get exposed. Tools you leave off are never offered.

Exposing your tools and connecting to *external* MCP servers are separate features that live in the same **MCP** tab. To use tools from another server inside Pico, see [Connect External MCP Servers](./connect-external-mcp-servers.md).

## Privacy and LAN access

Some tools reveal information about your machine. The **System Info** tool, for example, participates in the LAN-access privacy warning: if you expose Pico AI Server over your local network, enabling it lets connecting clients learn details about your host.

- Enable only the tools you actually need.
- If you share Pico AI Server on a LAN, require an API key in the **Users** tab so untrusted clients cannot trigger tool calls.
- Review the privacy warning shown in the **Tools** tab before turning on tools that expose host or network information.
