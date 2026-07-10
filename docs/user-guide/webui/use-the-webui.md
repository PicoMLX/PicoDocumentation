---
title: Use the WebUI
sidebar_position: 1
---

The WebUI is the browser chat served from the root URL. It gives you a chat landing screen, a conversation sidebar, file attachments, a model selector, and a local settings dialog for day-to-day use.

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
6. Attach files when needed.
   Text files and PDFs are accepted. Images need a vision-capable model. Audio needs an audio-capable model.
7. Open the settings dialog when you want local chat behavior changes.
   The current sections are `General`, `Display`, `Sampling`, `Penalties`, `Import/Export`, `MCP`, and `Developer`.

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

## Next steps

- [Open Web Chat and Launch Client Apps](./open-web-chat-and-launch-client-apps.md)
- [Chat API](../../reference/chat/chat-api.md)
