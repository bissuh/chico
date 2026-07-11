# Backlog — turma + Chico

Everything queued. Categories: BUILD (B), CRAFT (C, new or sharpened skills), RUN (R, real growth engagements), RUNTIME (RT, Layer 2).

Status: queued | in-progress | blocked | done

---

## Open

### RT-001: Layer 2 runtime (Agent SDK loop on capped API)
- Status: designed (see `RUNTIME.md`), not activated
- Why: make Chico an always-on agent that gets summoned across projects and writes learnings back
- Blocker: Bissuh sets a monthly API spend cap (Red). Recheck the Agent SDK metering (the 2026-06-15 pause) before switch-on.

### R-001: First real engagement, Sementes
- Status: in-progress (brand.md written, Chico summonable via `/turma:chico`)
- Run the first growth cycle: audit, highest-leverage move, ship, log the learning. Proves the whole system on real data. The first technique promoted back to turma comes from here.

### B-001: Connector analytics depth
- Status: queued
- `youtube-connector` is public-data only (OAuth unlocks retention and traffic). `beehiiv-connector` is read-only. Add per-project analytics as connectors when a real engagement needs them (Sementes uses Supabase + Search Console).

### C-001: Extract general growth frameworks into turma skills
- Status: queued
- The retired TBP playbook (git history) holds durable, agnostic doctrine not yet in a skill: the Acquire/Activate/Retain/Monetize/Refer loop, the hook hierarchy, welcome-flow and retention discipline. Turn the portable parts into turma skills (e.g. `growth-loop`, `hook-craft`).

### C-002: Build out the specialist agents
- Status: queued
- Beyond the `chico` operator agent: a distribution specialist, a copy specialist, a growth-analytics specialist that `chico` delegates to. Build when a real engagement needs the split.

### B-002: Repo relocation
- Status: queued
- The repo still lives under `TBP/`. Move to a neutral path once the pivot settles (touches paths and local configs).

### B-003: Triage remaining TBP legacy
- Status: queued
- `remotion/` (root): the TBP content renderer. Decide keep-as-turma-asset vs archive. (cta-machine has its own Remotion already.)
- `outbox/`, `knowledge-base/`, `playbooks/` contents (gitignored): TBP drafts and research. Archive or mine for reusable material.
- `scripts/` (pulse.sh, week-1-evaluation.sh): TBP-specific ops. Remove or repoint.
- Root ops docs (`BOOT.md`, `HEARTBEAT.md`, `SUBAGENT-POLICY.md`, `USER.md`, `TOOLS.md`): TBP-era, mostly mechanically valid. Repoint or archive (the boot ritual now lives in `CLAUDE.md`).

---

## Completed

- **Pivot from TBP to turma/Chico (2026-07-11):** canon re-missioned (SOUL/IDENTITY/SPEC/CLAUDE), turma plugin built (9 decoupled skills + chico agent + `/turma:chico` command + connectors + runnable tooling), privacy boundary set (public craft, gitignored business data), legacy TBP growth skills retired, memory + README rewritten.

---

## Rules

1. New items get the next number in their category.
2. Status changes get a short inline note.
3. When done, move to Completed with outcome + date.
4. Anything publishing under a brand stays draft until the owner approves (Yellow). Money and pushing the public repo are Red.
