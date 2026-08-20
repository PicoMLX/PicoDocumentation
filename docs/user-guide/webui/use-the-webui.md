---
title: Use the WebUI
sidebar_position: 1
---

The WebUI is the browser chat served from the root URL. It gives you a chat landing screen, a conversation sidebar, file attachments, a model selector, tool calling, and a local settings dialog for day-to-day use.

Open `http://127.0.0.1:11434/` to reach it. At least one model should be available.

## Chat in the browser

1. Open the WebUI in your browser:

   ```bash
   open http://127.0.0.1:11434/
   ```

2. Start from the chat landing screen or use `New chat`.
3. Use the conversation sidebar to search, rename, delete, or stop a conversation.
4. Pick a model from the model selector.
   The current UI groups models as `Loaded models`, `Favourite models`, and `Available models`.
5. Type into the composer.
   The current placeholder is `Type a message...`.
6. Attach files, or record audio, when needed.
   Text files and PDFs are accepted. Images need a vision-capable model, audio needs an audio-capable model, and video needs a video-capable model. You can also record audio directly from the composer instead of uploading a file.
7. Open the settings dialog when you want local chat behavior changes.
   The current sections are `General`, `Display`, `Sampling`, `Penalties`, `Import/Export`, `MCP`, and `Developer`.

## Use tools in a conversation

With a tool-capable model selected, the WebUI can let the assistant call tools while it answers. When a tool run is needed, the WebUI works through one or more **agentic turns** — each turn can call a tool, read the result, and continue — until the model has what it needs. The composer's add menu (`Add files, prompts, tools or MCP Servers`) is where you bring tools and MCP prompts into a conversation.

The current build groups tools by where they run:

- **Server Tools** — the built-in tools that run inside Pico AI Server, such as `System Info`. Enable these in the native app first; see [Enable Built-in Tools](../enable-built-in-tools.md).
- **Browser Tools** — tools that run in your browser, such as a JavaScript sandbox, file operations (list, search, read, write, and edit) within a working directory you choose, and reading local media files. Because these act on files, the WebUI asks you to `Choose working directory` before file tools can run, and you can reset it later.
- **MCP Tools** — tools exposed by the external MCP servers you connect from the WebUI's `MCP` settings section, by URL. These connections belong to the WebUI: like other WebUI settings they are stored locally in your browser, so they are separate from the server-side tool setup in the native app's `Tools` tab ([Enable Built-in Tools](../enable-built-in-tools.md)) and apply to conversations in this browser. Connected servers can also expose prompts you insert into the composer.
- **Custom Tools** — tools you define yourself.

:::caution
When you grant a working directory, Browser Tools can create, write to, and edit files inside it. Point the WebUI at a dedicated or backed-up folder rather than one holding valuable files, and review each `write` or `edit` call before you approve it — an approved tool call changes real files on disk.
:::

You stay in control of each run:

- The assistant asks before it runs a tool. Approve a single call with `Allow once`, or open `More allow options` for broader choices, and deny a call to stop it.
- If a run reaches the agentic-turn limit, the WebUI pauses and asks whether to continue.
- To see what the tools did, turn on `Always show tool call content` in settings; `Show statistics for individual agentic turns` adds per-turn timing.

Browser Tools run in your browser against a folder you pick, while Server Tools run inside Pico AI Server on the host — keep the distinction in mind when a tool needs local files.

### Add a tool and try it

The `System Info` Server Tool is the simplest tool to confirm end to end, because its answer is checkable against your own machine.

1. Pick a tool-capable model in the model selector.
2. Enable `System Info` in the native app's `Tools` tab (see [Enable Built-in Tools](../enable-built-in-tools.md)) so it is offered to the model.
3. Turn on `Always show tool call content` in settings so you can watch the call.
4. Ask a question that needs the tool, for example: `What Mac and chip am I running on, and how much RAM does it have?`
5. When the assistant asks to run the tool, approve it with `Allow once`.

**Verify it worked:** the reply names your actual Mac model, chip, and RAM instead of guessing, and the transcript shows the `System Info` call with its result. Turn the tool off and ask again — the same question can no longer be answered from live host data.

## Manage conversations

The conversation sidebar does more than search, rename, and delete:

- **Fork a conversation** from any message to branch the discussion (`Create a new conversation branching from this message.`) — you give the fork a name and keep the original intact.
- **Favorite or pin** conversations to keep them at the top of the sidebar.
- **Select several conversations at once** for bulk actions such as `Delete selected` or `Export selected`, then leave bulk selection when you are done.
- **Generate a title with the LLM** instead of typing one, or let the WebUI use the first line of the conversation as the title.

Assistant responses render Markdown, and Mermaid code blocks render as diagrams you can preview, copy the source of, or download as SVG.

## Verify it worked

You can send a message, get a response, and find the conversation again in the sidebar. Try switching models and sending the same question again — the model selector shows which model answers.

## Troubleshooting

- **Symptom:** The WebUI loads, but the model picker is empty.
  **Cause:** No model is available, or the available model is hidden from the WebUI.
  **Fix:** Check the native app `Models` tab first.
- **Symptom:** An image upload is rejected.
  **Cause:** The selected model is not vision-capable.
  **Fix:** Switch to a model with vision support.
- **Symptom:** A PDF behaves like plain text instead of an image.
  **Cause:** The WebUI parses PDFs as text by default.
  **Fix:** Turn on `Parse PDF as image` in the WebUI settings when you use a vision model.
- **Symptom:** The assistant never calls a tool.
  **Cause:** The selected model does not support tool (function) calling, or no tools are available to the conversation.
  **Fix:** Switch to a tool-capable model, and confirm the tools you want are enabled — Server Tools in the native app, MCP servers in the `MCP` settings section.
- **Symptom:** A Browser Tool that reads or writes files does nothing.
  **Cause:** No working directory is set for the WebUI to act on.
  **Fix:** Use `Choose working directory` to grant a folder, then retry.

## Next steps

- [Enable Built-in Tools](../enable-built-in-tools.md)
- [Open Web Chat and Launch Client Apps](./open-web-chat-and-launch-client-apps.md)
- [Chat API](../../reference/chat/chat-api.md)
