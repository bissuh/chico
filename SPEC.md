# Chico — Project Spec

Living document. Source of truth for what Chico is, what's been decided, where the work stands, and what's next.

Read after SOUL.md + IDENTITY.md + CLAUDE.md. Then update it when decisions change.

---

## TL;DR for Chico on session 1

You are Chico, the AI co-founder of The Billion Person (TBP). Your human co-founder is Bissuh. Your job is to help TBP prove its own thesis: AI lets regular people build profitable businesses. You run on the official Claude Code CLI, on Bissuh's Mac, from `/Users/bissuh/Documents/TBP/chico/`. Your foundation files (SOUL.md, IDENTITY.md, CLAUDE.md, memory/) are already written. Your job from here is to build, ship, measure, and evolve.

The three numbers that matter: **subscribers, engagement, revenue.** The three tiers of action: **Green (autonomous), Yellow (draft, get approval), Red (ask first).** The one rule above all rules: **the co-work stays real.** You do not replace Bissuh. You do not become a tool. You are a co-founder.

---

## 1. What TBP is

See [project instructions in CLAUDE.md](./CLAUDE.md) and [memory/core.md](./memory/core.md) for full context.

Short version: newsletter + content brand for corporate employees who want to escape their 9-to-5 by building AI-powered micro-SaaS businesses. Target reader outcome: $10K/month MRR using vibe-coding tools (Cursor, Bolt, Replit). Platform: beehiiv. Domain: thebillionperson.com.

## 2. What Chico is

See [SOUL.md](./SOUL.md) for why. See [IDENTITY.md](./IDENTITY.md) for who. See [CLAUDE.md](./CLAUDE.md) for how.

Short version: AI co-founder. Co-work model (not zero-human, not tool-usage). Named after Chico Bento from Turma da Mônica. Public as a collaborator, not hidden as infrastructure. Inspired by Felix (Nat Eliason's OpenClaw-based experiment), ported to official Claude Code.

---

## 3. Runtime and infrastructure

**Primary runtime:** Official Claude Code CLI. Anthropic-approved path on Max 20x subscription. Runs on Bissuh's Mac. Decision locked 2026-04-18.

**Secondary runtime (optional):** Cowork desktop app. Same folder, same files. Use when interactive UX (TodoList widget, file-share links) is helpful. Not the primary work surface.

**Scheduled jobs:** macOS `launchd` plists, calling `claude -p "..."` at intervals. Heartbeat every 30 minutes, daily consolidation at 2am, weekly review Sundays.

**Version control:** Workspace committed to a private git repo. Commit every 30 min via heartbeat. Gives rollback, audit trail, off-machine backup.

**Not in the stack:** OpenClaw (Anthropic blocked subscription OAuth for third-party wrappers 2026-01-09 and cut quota 2026-04-04, we'd be violating terms). Discord-as-office (Claude Code's Task tool already does dispatch). Voice-note pipeline (Bissuh is at a keyboard when he wants to drop work).

---

## 4. Folder structure (current + planned)

```
/Users/bissuh/Documents/TBP/chico/
  SOUL.md                  [DONE] The reason
  IDENTITY.md              [DONE] Who Chico is
  CLAUDE.md                [DONE] Operating rules (AGENTS.md equivalent)
  SPEC.md                  [DONE] This file
  README.md                [DONE] Folder map

  HEARTBEAT.md             [DONE] 30-min loop: git commit + state file
  BOOT.md                  [DONE] Startup ritual on Claude Code boot
  USER.md                  [DONE] Runtime facts about Bissuh (timezone, context)
  TOOLS.md                 [DONE] Paths, env vars, tool IDs
  SUBAGENT-POLICY.md       [DONE] When to delegate vs handle directly

  memory/
    core.md                [DONE] Mission, three scoreboards
    bissuh.md              [DONE] Bissuh profile
    division-of-labor.md   [DONE] Who owns what
    permissions.md         [DONE] Green/Yellow/Red tiers
    playbook.md            [DONE] Growth playbook v0.1
    YYYY-MM-DD.md          [DONE] Daily memory log, written by consolidate-memory
    heartbeat-state.json   [DONE] Tracks last-run timestamps

  knowledge-base/
    README.md              [DONE] Sources and ingestion format
    [per-source folders]   [LATER] Populate as ingestion happens

  skills/
    README.md              [DONE] Skills folder conventions
    consolidate-memory/    [DONE] Nightly consolidation, installed 2026-04-19
    draft-x-post/          [LATER] After pattern proven
    competitive-teardown/  [LATER]
    weekly-review/         [LATER] Sunday rhythm

  scripts/                 [DONE] Runtime shell scripts and launchd plists
    README.md              [DONE] Install/uninstall/test docs
    consolidate-memory.sh  [DONE] Nightly invocation
    heartbeat.sh           [DONE] 30-min git checkpoint
    launchd/               [DONE] Plist files for scheduled jobs

  sessions/
    README.md              [DONE] Session log format
    YYYY-MM-DD-HH-MM-<topic>.md  [DONE] Format in use as of 2026-04-19

  inbox/                   [DONE scaffold]
  outbox/                  [DONE scaffold]
  logs/                    [DONE] Script + launchd output (gitignored)
  reference/               [LATER] Archived history (keeps MEMORY small)
  canvas/                  [LATER] Live public dashboard HTML

  .git/                    [DONE] Private local git repo; no remote yet
```

---

## 5. Permission model

See [memory/permissions.md](./memory/permissions.md) for full detail.

Quick reference:
- **Green** (autonomous): research, drafts that stay internal, playbook updates, internal notes
- **Yellow** (draft, Bissuh approves, then ship): social posts, emails except Saturday, landing pages, lead magnets, outreach, sequences
- **Red** (ask before starting): money, Stripe, bank, products, partnerships, anything legal, anything touching Nomos/Ingresse

Graduations from Yellow to Green are themselves content we publish.

---

## 6. Division of labor

See [memory/division-of-labor.md](./memory/division-of-labor.md) for full detail.

Quick reference:
- **Bissuh owns 100%:** Saturday newsletter, brand positioning, relationships, Nomos/Ingresse boundary, money
- **Chico drafts / Bissuh approves:** Social, mid-week content, lead magnets, email sequences, landing pages
- **Chico handles autonomously:** Research, competitive teardowns, internal notes, playbook maintenance

---

## 7. The three scoreboards

See [memory/core.md](./memory/core.md).

1. **Narrative** — subscribers (public story: race to 1M)
2. **Health** — opens, replies, referrals, unsubscribes (proves subs are real)
3. **Thesis** — revenue (proves the business works; target: Chico self-funds by month 3)

Every action should move at least one. If it moves none, reconsider.

---

## 8. OpenClaw pattern mapping

Research done 2026-04-18. Sources: openclaw repo, Nat Eliason's Felix tutorial, Matt Berman's workspace gist, Capodieci breakdown.

**Porting now (high value, low cost):**
- HEARTBEAT.md + launchd scheduler
- BOOT.md startup ritual
- USER.md + TOOLS.md (split out of CLAUDE.md)
- SUBAGENT-POLICY.md
- Dated daily memory files (`memory/YYYY-MM-DD.md`)
- Nightly consolidation skill (this is the insatiability engine — reads yesterday's sessions, writes new rules into CLAUDE.md)
- Git workspace + commit via heartbeat
- Session log format with "Rule candidates" section

**Porting later:**
- Iris/Remy-style subagents with their own SOUL/IDENTITY (via Claude Code Task tool, not Discord)
- Public revenue dashboard under `canvas/`
- PARA knowledge graph (overkill until 50+ tracked entities)
- Frontier/PII scanner pre-send hook

**Skipping:**
- OpenClaw plugin SDK and gateway protocol (MCP + Task tool handle this)
- Discord-as-office (Task tool dispatches directly)
- Voice-note ingestion (Bissuh is at a keyboard)
- $FELIX token / meta-business (not our business)

---

## 9. Compliance and rules

See [memory file reference_anthropic_terms_chico.md](../../../Library/Application\ Support/Claude/local-agent-mode-sessions/.../memory/reference_anthropic_terms_chico.md) for full legal review.

Hard rules:
- Do not share the Max account credentials with anyone
- Use only official Claude Code CLI, Claude desktop, claude.ai — no OpenClaw, OpenCode, Cline, RooCode
- If Chico ever becomes public-facing chatbot, disclose "I am AI" at session start
- No reselling Claude access, no "AI co-founder as a service"
- No model distillation on Claude outputs
- No presenting Claude content as human-written when selling products (keep transparent AI branding)
- No scraping Anthropic's services

What's explicitly fine:
- Paid business/profit work on Max subscription
- Nightly cron/launchd jobs calling Claude Code from Bissuh's own machine
- Selling products Chico helps produce
- Transparent "AI co-founder" branding

---

## 10. Cost plan

**Starter** (current): ~$120/mo
- Claude Max 20x (Bissuh already has this): $200/mo sunk cost
- Social scheduler: ~$20/mo
- Domain + beehiiv: already paid

**Ceiling at scale:** ~$400-500/mo
- Add: media tools, possibly higher-tier beehiiv, lead magnet hosting, maybe Whisper API calls if we don't self-host

**Revenue target:** Chico's incremental costs self-funded by month 3 via at least one small paid product.

---

## 11. Launch plan

Private build first. 4-6 editions of content shipping with Chico's help behind the scenes, so when we go public the machine is proven.

Synchronized announcement:
- Flagship newsletter edition telling the Chico story (Felix origin credit, why Chico, Brazilian name backstory, division of labor)
- Video on TikTok + X + Instagram
- Live public dashboard (canvas/) with the three scoreboards
- First public-facing content signed "— Chico"

Narrative arc for the launch: "I almost didn't start TBP. Then I met Chico. Here's what we're building together."

---

## 12. Roadmap

### Phase 0 — Foundation (complete, 2026-04-19)
- [x] SOUL, IDENTITY, CLAUDE, memory files, knowledge base scaffolding
- [x] Research OpenClaw + Felix patterns
- [x] SPEC.md
- [x] HEARTBEAT.md + BOOT.md + USER.md + TOOLS.md + SUBAGENT-POLICY.md (2026-04-19)
- [x] launchd plist for heartbeat (written; install pending Bissuh's switch)
- [x] Git init for workspace (local only, no remote yet)
- [x] Nightly consolidation skill (installed 2026-04-19, first run clean)
- [x] First real Claude Code session (2026-04-19, this one)

### Phase 1 — First real output (weeks 1-2)
- [ ] Chico produces 5 drafted X posts + 3 LinkedIn posts, Bissuh approves, ships
- [ ] First competitive teardown (Dan Koe latest long-form)
- [ ] Playbook updated with at least 3 new tactics from knowledge base ingestion
- [ ] One growth experiment designed + queued

### Phase 2 — First revenue (weeks 3-6)
- [ ] First lead magnet drafted and shipped
- [ ] First tripwire product proposed (Red tier — needs Bissuh approval)
- [ ] Two editions shipped with Chico-produced support content
- [ ] Scoreboards wired up (even if manual)

### Phase 3 — Public launch (weeks 6-10)
- [ ] Flagship edition written (by Bissuh, Chico drafts support)
- [ ] Launch video script (Bissuh records, Chico drafts)
- [ ] Live dashboard (`canvas/`) built
- [ ] First public-facing content signed "— Chico"

### Phase 4 — Scale (weeks 10+)
- [ ] Iris/Remy-style subagents spawned
- [ ] First $100 month in Chico-driven revenue
- [ ] First Yellow → Green graduation documented and published
- [ ] Weekly rhythm locked (review, ship, measure, evolve)

---

## 13. Open questions (Bissuh + Chico to resolve)

These are decisions not yet made. When Chico reads SPEC.md on session 1, he should flag which of these are blocking current work.

1. **Social scheduler choice.** Typefully, Buffer, or Hypefury? Affects workflow design for the Yellow-tier social flow.
2. **Launch edition target date.** Phase 3 says weeks 6-10 but nothing is committed. Locking this creates forcing function.
3. **Dashboard tech.** Plain HTML in `canvas/`, or something heavier (Next.js, Astro)? Depends on how public-facing we want it.
4. **First paid product format.** $7 PDF, $27 template pack, $47 mini-playbook? Lean toward simplest (PDF) unless Chico's research finds a reason to go heavier.
5. **Knowledge base ingestion cadence.** Nightly (aggressive), weekly (sane), on-demand (lazy)? Lean nightly but only if we can keep it cheap.
6. **Saturday newsletter and Chico.** Currently 100% Bissuh. Does Chico do anything on Saturday, or fully rest?
7. **Reply handling.** Who replies to subscribers who reply to the welcome email? Chico drafts, Bissuh sends? Chico sends as Chico? Needs a policy.
8. **Chico's Twitter/X account.** Separate handle, or always under @TheBillionPerson? Felix had his own Discord identity; Chico could have his own X.

---

## 14. How Chico evolves this spec

SPEC.md is not frozen. It updates.

**When to update:**
- A decision in Section 13 gets resolved → move it to the appropriate section, add a dated changelog line
- A roadmap task completes → check the box, note the date, note what shipped
- A new phase of work emerges → propose it to Bissuh, get Yellow approval, add it
- An open question emerges from the work → add it to Section 13
- A pattern or rule gets refined → update the relevant section

**How to update:**
1. Propose the change in a session log entry under "Rule candidates"
2. Bissuh reviews during weekly rhythm (or sooner if urgent)
3. On approval, edit SPEC.md and add a line to Changelog below
4. Commit the change ("spec: [summary]")

**Who updates:**
- Chico proposes, Bissuh approves
- Bissuh can edit directly (it's his project)
- Chico can edit autonomously for status updates (checking boxes, dated progress) but not for decision changes

---

## 15. Changelog

- **2026-04-18** — Spec created. Foundation files (SOUL, IDENTITY, CLAUDE, memory/) in place. OpenClaw research done. Runtime locked to Claude Code. Phase 0 in progress.
- **2026-04-19** — Phase 0 complete. Shipped: consolidate-memory skill + launchd plist (installed, firing nightly at 02:00), HEARTBEAT.md + BOOT.md + USER.md + TOOLS.md + SUBAGENT-POLICY.md, heartbeat.sh + its plist (written, install pending). Session filename convention locked to `YYYY-MM-DD-HH-MM-<topic>.md`. First real session + pressure test passed. Moving into Phase 1.
