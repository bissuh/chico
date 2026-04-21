# Chico backlog — build, create, automate

Everything queued up. Updated as we add items.

**Categories**
- BUILD (B): infra, scripts, integrations
- CREATE (C): content assets (lead magnets, pages, emails, bios)
- AUTOMATE (A): repeatable workflows Chico runs
- EXPERIMENT (E): test-and-learn campaigns

**Status**: `queued` | `in-progress` | `blocked` | `draft` | `done`

**Priority**: `P0` (this week) | `P1` (this month) | `P2` (later, parked)

---

## Open

### B-001 — beehiiv API integration
- Priority: P1
- Status: **done** (2026-04-21)
- Delivered:
  - `skills/beehiiv-api/SKILL.md` with read-only usage instructions
  - `scripts/beehiiv.sh` wrapper (subcommands: stats, posts, post, subscribers, segments, automations, raw)
  - `.env` (gitignored) holds API key + pub ID
  - `.env.example` checked in as template
- Not included: write operations (POST/PATCH/DELETE). Intentional. Any write path needs a separate skill with its own approval flow.

### B-002 — Post-signup survey setup
- Priority: P0
- Status: blocked on C-002
- Why: first-party data + phone capture from day one. Compounds as list grows. McGarry framework #2.
- Blocker: needs C-002 (survey copy)
- Target: 80%+ completion, 10%+ phone opt-in

### C-001 — Lazy lead magnet #1 (from Bissuh's best X long-form)
- Priority: P0
- Status: blocked on input
- Why: foundation for comment-to-get, bio CTA, post-CTAs. No other growth tactic works without at least one live magnet.
- Blocker: Bissuh names his top-performing X long-form or thread from last 90 days, or I pick one from the drafts
- Output: landing page copy + PDF layout + email-gated delivery

### C-002 — Signup survey copy (5 questions)
- Priority: P0
- Status: queued
- Why: unblocks B-002
- Notes: last question asks for phone opt-in, framed around live events (McGarry's template)

### C-003 — Welcome email v2 (WEAC refinements)
- Priority: P1
- Status: queued
- Why: current welcome email hits all five WEAC elements. Refinements only. See session notes.
- Changes:
  - Add one-line instruction on HOW to move to Primary (Gmail: drag to Primary tab. Apple Mail: mark as VIP)
  - Verify double opt-in is OFF in beehiiv settings
  - Consider moving value-prop above lead magnet link (readers who click the magnet may never scroll back)
- Target: 60%+ open, 10%+ click

### C-004 — Welcome email #2 (PMF signal ask)
- Priority: P1
- Status: queued
- Why: separate the open-ended "what problem can I solve" question from email #1's one-word reply ask. Email #1 protects deliverability. Email #2 captures insight. Both wins, no tradeoff.
- Send: 24-48h after welcome email #1

### C-005 — X / Twitter bio rewrite
- Priority: P0
- Status: draft in `outbox/`
- Why: single-CTA bio converts 50%+, linktree converts <10% (McGarry)

### C-006 — LinkedIn headline + about rewrite
- Priority: P0
- Status: draft in `outbox/`

### A-001 — Pre/Post-CTA auto-draft around Saturday newsletter
- Priority: P1
- Status: queued
- Why: saves Bissuh 30+ min/week on social prep. Turns the flywheel into muscle memory.
- Workflow:
  - Thursday night: Chico drafts Friday pre-CTA from Saturday edition-in-progress
  - Sunday morning: Chico drafts Sunday post-CTA from sent edition
  - Both drop in `outbox/` as `review-needed`
  - Bissuh approves on Friday + Sunday
- Dependency: Saturday edition drafted by Friday
- McGarry framework: MAGIC (A), ADAPT weekly rhythm

### A-002 — Weekly ADAPT content pack
- Priority: P1
- Status: queued
- Why: 5 social posts/week from every Saturday edition. Compound growth from one source.
- Workflow: Sunday night, Chico drafts Amplify + Direct + Ask + Pull + Transcribe posts. Outbox Monday morning.
- Dependency: Saturday edition sent
- McGarry framework: ADAPT

### A-003 — Warm DM flow for new followers (X + LinkedIn)
- Priority: P2
- Status: parked
- Why: MAGIC (I) — inbox DM new followers
- Blocker: not worth automating until volume > 50 new followers/week. Bissuh can do manually at current scale.

### E-001 — Comment-to-get giveaway #1 on LinkedIn
- Priority: P1
- Status: blocked on C-001
- Blocker: needs lead magnet #1 live
- Hypothesis: first run on LinkedIn gets 50+ comments, 20+ new subs in <1 week
- Setup:
  - Platform: LinkedIn (highest-value audience for TBP thesis)
  - Keyword: short and memorable (e.g., "PLAYBOOK", "MICROSAAS")
  - DM: ends with "can you let me know if the link works?" (McGarry's LinkedIn spam-dodge trick, drives 30% reply rate)
  - Cadence post-launch: once every 2-3 weeks max
- McGarry framework: MAGIC (G)

### E-002 — Deliverability detox (BSS sending progression)
- Priority: P2
- Status: parked
- Why: premature. Needs 2K+ subs and 60+ days of send data to matter. Revisit month 3+.
- McGarry framework: BSS

---

## Completed

(nothing yet)

---

## Rules for updating this file

1. New items get the next number in their category (B-003, C-007, etc.)
2. Status changes get a short inline note when relevant
3. When an item is `done`, move it to the Completed section with outcome + date
4. Parked items stay visible (don't delete — we might revisit)
5. Anything touching publishing (Yellow) stays as `draft` until Bissuh approves
