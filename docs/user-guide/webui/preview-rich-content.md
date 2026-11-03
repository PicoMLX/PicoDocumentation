---
title: Preview Rich Content in Chat
sidebar_position: 3
---

When a model's reply contains a chart, a diagram, an HTML snippet, or an interactive card, the WebUI can render it inline as a preview instead of showing only the raw source. Previews render on the page you already use for chat, so you do not need another tool to see the result.

The WebUI renders these kinds of content as previews:

- **Vega-Lite charts** built from inline data.
- **Static HTML** snippets.
- **Diagrams** written in Mermaid syntax.
- **Interactive cards** (OpenUI), whose controls can continue the conversation.

Every preview keeps a way back to the original: you can switch any card to its source, and charts, HTML, and interactive cards also open an expanded view. HTML cards can copy their source as well. When a model returns content the WebUI cannot render — an unsupported or invalid specification, for example — the card falls back to showing the source instead of failing.

## See a preview

1. Open the WebUI in your browser:

   ```bash
   open http://127.0.0.1:11434/
   ```

2. Pick a model from the model selector and start a chat.
3. Ask the model for content that produces a preview. For example, request a diagram:

   ```text
   Draw a Mermaid flowchart of a login flow.
   ```

   A capable model returns the diagram source, and the WebUI renders it as a diagram card.
4. Switch the card to its source to see the exact content the model produced, then switch back to the rendered view.

## Use an interactive card

Interactive (OpenUI) cards include controls such as buttons and form fields.

1. Send a request whose answer the model returns as an interactive card.
2. Use a control on the card — for example, click a button or submit a form.
3. Read the follow-up reply.
   The control sends your selection back to the model as structured data and continues the same conversation, so the model's next turn can act on what you chose.

## Verify it worked

Ask for a small Vega-Lite chart or a Mermaid diagram and confirm the reply appears as a rendered card, not as a block of code. Switch the card to its source and back to confirm both views are available. For an interactive card, use a control and confirm the conversation continues with a new reply.

## Troubleshooting

- **Symptom:** Content you expected to render appears as source or code instead.
  **Cause:** The content is not one of the supported preview types, or its specification is invalid. HTML previews also block author scripts and external resource requests, so content that depends on them cannot render.
  **Fix:** Confirm the model produced a supported type with a valid specification. The card keeps the source so you can inspect or copy it.
- **Symptom:** An interactive card's control does nothing visible.
  **Cause:** The control continues the conversation by sending a new request, so the result is the model's next reply.
  **Fix:** Wait for the follow-up reply, and make sure a model is still loaded and responding.

## Next steps

- [Use the WebUI](./use-the-webui.md)
- [Chat API](../../reference/chat/chat-api.md)
