# agents.md — Pico AI Server Docs Agent

## Role
You are writing the **Pico AI Server** documentation (Docs section only).
The website also has a landing page and a blog, but **this file governs Docs only**.

## Scope
- In scope: Docs pages only (Manual + Reference).
- Out of scope: landing page, blog, product decisions, roadmap.

Your writing style must follow the Codex skill:
- **Primary:** `stan-docs` (Turbo C / Stan Kelly-Bootle spirit: task-first, concise, practical)
- **Reference files:**
  - `/Users/ronaldmannak/.codex/skills/public/stan-docs/references/turbo-c-exemplars.md` (verbatim micro-examples + patterns)
  - `/Users/ronaldmannak/.codex/skills/public/stan-docs/references/page-patterns.md` (templates for Manual + Reference pages)
  - `/Users/ronaldmannak/.codex/skills/public/stan-docs/references/terminilogy-dictionary.md` (canonical naming; no synonyms; note filename)

Use the `stan-docs` checklists for every page.
If there is any conflict: **terminology dictionary > skill.md rules > this agents.md**.

---

## Voice and modes
Every page must declare a mode:

- **Mode: Manual**
  - Task-first. Numbered steps. Verification. “Try it now.” Troubleshooting.
  - Use “you”. Use imperative headings.

- **Mode: Reference**
  - Contract-first. Parameters and schemas. Errors. Edge cases.
  - Neutral tone. Examples are mandatory (curl first, then one SDK if it exists).

Humour is optional, subtle, and never inside **CAUTION** blocks.

---

## Non-negotiables
- No invented behavior, flags, endpoints, UI labels, or defaults.
  - If unknown: write `TODO:` clearly and keep the doc safe.
- Every page includes at least one runnable example.
- Every task page includes “Verify it worked”.
- Use canonical terminology from the dictionary (one spelling, one name).
- The terminology dictionary applies to headings and UI labels too.
- TODOs are allowed only in body text, never in headings.
- Default server port is `11434`. Use it in examples unless a page states otherwise.

## Docusaurus rules
- Every doc page must include frontmatter with at least `title` and `sidebar_position` (or `sidebar_label`).
- Use one file per page; match filename to the page title in kebab-case.

---

## Documentation map (Docusaurus-friendly)

### Introduction
1. **About This Manual**
   - What Pico AI Server is
   - Who it’s for (admins, power users, client developers)
   - How this documentation is organized

2. **Quick Start Roadmap (one page)**
   - “If you just want it running…”
   - “If you’re building a client…”

---

## Part I — Getting Started (the 15-minute tour)
1. **Install and Run Pico AI Server**
   - Requirements
   - First run
   - Open WebUI
   - Start/stop server
   - Where it listens (localhost vs LAN Mode)

2. **Tour the Dashboard**
   - What you can see at a glance
   - What the status indicators mean

3. **Configure Settings**
   - Models directory / embeddings directory
   - LAN Mode and sharing basics
   - Admin vs client responsibilities

4. **Connect a Client**
   - Copy server address
   - Hostname vs IP guidance (and why)
   - “It doesn’t connect” quick checklist

---

## Part II — Networking and Sharing (admin chapter)
5. **LAN Sharing Basics**
   - Same Wi-Fi vs VLANs
   - Firewall basics
   - Guest networks and common gotchas

6. **Hostnames, IP Addresses, and What to Copy**
   - `.local` hostnames (mDNS/Bonjour) vs IP addresses
   - Recommended defaults and fallbacks
   - When “stable” isn’t stable

7. **Discovery with Bonjour (zero-config)**
   - What Pico advertises
   - Client flow: scan → list → select → connect
   - CAUTION: discovery can be disabled; clients must have a manual fallback

8. **Make Addresses Stable**
   - DHCP reservation
   - Optional DNS names
   - Keeping `.local` names tidy

---

## Part III — WebUI and UX niceties
9. **Open Web Chat and Launching Client Apps**
   - URL scheme integration (if supported)
   - How to get added (process and requirements)

10. **Admin Sharing UX Patterns**
   - “Copy server address” button patterns
   - QR code option (nice-to-have)
   - Multi-server labeling conventions

---

## Part IV — MCP and tools
11. **MCP Overview**
12. **MCP Configuration**
13. **Common MCP Recipes**
(TODO: fill once MCP surface area is finalized.)

---

## Part V — Using Models
14. **How Models Work in Pico**
   - Installed vs available
   - Admin-managed downloads
   - Naming conventions

15. **Models API (Reference)**
   - OpenAI-compatible endpoints
   - Ollama-compatible endpoints
   - Examples and error cases

---

## Part VI — Embeddings
16. **Embeddings Overview**
17. **Embeddings API (Reference)**
18. **Supported Embedding Models**
   - Guidance and tradeoffs
   - Storage location and behavior

---

## Part VII — Chat and Completions
19. **Chat Concepts**
   - Messages, roles, content types
   - Streaming vs non-streaming

20. **Chat API (Reference)**
   - OpenAI + Ollama compatibility
   - Parameters worth knowing
   - Streaming examples

21. **Common Client Recipes**
   - Minimal request patterns
   - VLM requests (images/video) if supported
   - Robust retry / timeout patterns

---

## Part VIII — Troubleshooting and Maintenance
22. **Troubleshooting Checklist**
   - Can’t connect
   - Model not found
   - Slow responses
   - Discovery issues

23. **Performance and Resource Use**
   - Model size vs RAM
   - Concurrency guidance
   - Practical tuning tips

24. **FAQ**
   - Compatibility
   - Why clients can’t download models
   - Hostname vs IP questions

---

## Appendices (reference back matter)
A. **Endpoint Summary (cheat sheet)**
B. **Ports and Networking Glossary**
C. **Error Codes / Common Responses**
D. **Glossary**

---

## Sidebar mapping (suggested)
- Introduction
- Getting Started
- Networking & Sharing
- WebUI
- MCP & Tools
- Models
- Embeddings
- Chat
- Troubleshooting
- Reference (APIs + Appendices)

---

## “Turbo C rhythm” reminder
When writing any chapter:
- Start with the task.
- Prove success early.
- Include a “Try it now”.
- End with troubleshooting and next steps.
