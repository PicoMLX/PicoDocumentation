---
title: Enable Built-in Tools
sidebar_position: 3
description: Turn on Pico AI Server's built-in tools, including the system info tool, and expose them to your models and to MCP clients.
---

<!-- Mode: Manual -->

## Understand built-in tools

Pico AI Server ships with **built-in tools** that a model can call during a
conversation. When a tool-capable model decides it needs one, Pico AI Server runs
the tool locally and feeds the result back into the model's answer — no external
service required.

Built-in tools are separate from the tools you connect through the Model Context
Protocol (MCP). MCP connects Pico to *external* servers; built-in tools run
*inside* Pico AI Server. Both are turned on in Pico's settings, and both are off
until you enable them.

This page shows how to enable built-in tools and uses the **System Info** tool as
the worked example.

## What you will do
- Open the **Tools** settings tab
- Enable the built-in tools you want models to use
- Ask a model a question that makes it call a tool
- (Optional) Expose your enabled tools to MCP clients

## Before you start
- A version of Pico AI Server that includes the **Tools** settings tab
- A model that supports tool (function) calling

## Enable a built-in tool
1. Open **Settings** in Pico AI Server.
2. Select the **Tools** tab.
3. Turn on the individual tools you want to make available to models.

Only enabled tools are offered to the model. A tool you leave off is never
advertised, so a model cannot call it.

## The System Info tool

The **System Info** tool lets a model ask about the Mac it is running on. When
enabled, the model can report details such as:

- **Hardware** — Mac model identifier, chip name, architecture, CPU core counts
  (total, performance, and efficiency), and thermal state
- **Memory** — physical RAM, an available-memory estimate, and MLX active, cache,
  and peak usage
- **Operating system** — name, version, and build
- **Host app** — Pico AI Server's name, version, and build

System Info is on by default, alongside the other harmless local utilities. You can
turn it off in the **Tools** tab like any other tool.

### Try it now
With a tool-capable model installed and the **System Info** tool enabled, ask a
question that needs host details. From the Web Chat, or over the API:

```bash
curl http://127.0.0.1:11434/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "your-model-name",
    "messages": [
      { "role": "user", "content": "What Mac and chip am I running on, and how much RAM does it have?" }
    ]
  }'
```

The model calls the System Info tool and answers with your machine's model, chip,
and memory instead of guessing.

### Verify it worked
- The reply names your actual Mac model, chip, and RAM — not a generic or made-up
  machine.
- With the **System Info** tool turned **off**, the same question can no longer be
  answered from live host data.

## Expose your tools to MCP clients

The **Tools** tab also has an **Expose enabled tools to MCP clients** toggle. Turn
it on to let external MCP clients reach the tools you have enabled, in addition to
your own models using them during generation.

Your enabled tools — built-in tools included — are what get exposed. Tools you
leave off are never offered.

## Privacy and LAN access

Some tools reveal information about your machine. The **System Info** tool, for
example, participates in the LAN-access privacy warning: if you expose Pico AI
Server over your local network, enabling it lets connecting clients learn details
about your host.

- Enable only the tools you actually need.
- If you share Pico AI Server on a LAN, require an API key in the **Users** tab so
  untrusted clients cannot trigger tool calls.
- Review the privacy warning shown in the **Tools** tab before turning on tools
  that expose host or network information.
