# tools/

A living, shareable database of the tools we cover at The Billion Person. Every time we feature or recommend a tool, it lands here with the facts a builder actually needs: what it does, whether it has an API, whether it has an MCP server you can plug into your AI, and where we wrote about it.

This grows over time. It is meant to become the reference: a curated shelf of tools that actually earn their place, not a hype list.

## Legend

- **GenAI**: Yes = it is fundamentally a generative-AI product. No = infrastructure that may use AI but is not generative at its core.
- **API**: public developer API. *Limited* = exists but narrow (admin/usage only, or preview), not a clean public product API.
- **MCP** (Model Context Protocol, the standard for giving an AI agent access to a tool):
  - **Official server** = the vendor ships an MCP server, so you can connect this tool directly to Claude, Cursor, ChatGPT, etc.
  - **Client** = the tool consumes MCP servers (it is the AI side), but does not expose itself as one.
  - **Server (preview)** = official server announced but still a research preview.
  - **Community only** = third-party MCP servers exist, nothing official from the vendor.

All MCP/API facts verified May 2026. Flag anything that drifts.

## The database

| Tool | What it does | Category | GenAI | API | MCP | Used by | TBP source |
|---|---|---|---|---|---|---|---|
| **Claude** (Anthropic) | LLM for chat, coding, agents. The thinking + writing layer. Reads least like AI. | LLM | Yes | Yes | Client (host) | broad dev + enterprise | [Claude wrote his blog](https://www.thebillionperson.com/p/claude-wrote-his-blog-28-days-later-3-paying-clients) |
| **ChatGPT / OpenAI** | LLM chat + developer API (Responses, Agents SDK). | LLM | Yes | Yes | Client (host) | broad | 2026-06-01 |
| **Cursor** (Anysphere) | AI-native code editor for when you want to see the code. | AI coding | Yes | Limited | Client | pro engineers, startups | 2026-06-01 |
| **Lovable** | Describe an app, get a real full-stack build. Non-coder pick. ~$200M ARR (2025). | Prompt-to-app | Yes | Limited | Server (preview) | solo / non-technical founders | 2026-06-01 |
| **Bolt** (bolt.new) | Browser prompt-to-app, instant deploy. Fast same-day MVP. | Prompt-to-app | Yes | No | Client | solo builders, hackathons | 2026-06-01 |
| **Replit** (Agent) | Cloud IDE + agent that builds, runs, and deploys from a prompt. | Prompt-to-app | Yes | Limited | Client | education, solo devs | core stack |
| **n8n** | Open-source automation with native AI agent nodes. Self-host = free. | Automation | No | Yes | Official server | technical / ops teams | 2026-06-01 |
| **Make** (make.com) | Visual no-code automation, friendlier UI, bills per operation. | Automation | No | Yes | Official server | SMBs, marketers, ops | 2026-06-01 |
| **Gemini CLI** (Google) | Open-source AI agent in the terminal. Biggest free tier in the category. | AI coding (CLI) | Yes | Yes | Client | developers, GCP users | 2026-06-01 |
| **Supabase** | Postgres backend: database, auth, storage. The backend under most no-code apps. | Backend | No | Yes | Official server | indie + startup base | 2026-06-01 |
| **Clay** (clay.com) | GTM data platform: lead enrichment, ICP scoring, outbound, via 150+ providers. | Lead-gen | No | Yes | Official server | B2B sales / RevOps | 2026-06-01 |
| **Gamma** (gamma.app) | Generate decks, docs, sites, and posts from a prompt. | AI decks | Yes | Yes | Official server | founders, marketers | 2026-06-01 |
| **Lemon Squeezy** | Merchant-of-record for selling digital products + subs (handles tax). | Payments | No | Yes | Community only | indie SaaS sellers | 2026-06-01 |
| **Stripe** | Payments infrastructure: online payments, billing, subscriptions. | Payments | No | Yes | Official server | millions of businesses | 2026-06-01 |

## How this list grows

When a tool gets featured or recommended in any TBP content (newsletter, carousel, video), add a row here. Keep the facts verified, never guess an API or MCP status, and link the published edition where we covered it. When a tool earns repeated mentions, it has earned a permanent place on the shelf.
