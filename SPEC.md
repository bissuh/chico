# Chico: Project Spec

Living document. Source of truth for what Chico is, what's decided, where the work stands, and what's next.

Read after SOUL.md + IDENTITY.md + CLAUDE.md. Then update it when decisions change.

## TL;DR

Chico is a **portable, project-agnostic growth specialist**: the marketing, distribution, and sales brain the underdog builder cannot otherwise afford. The craft is packaged as an open-source Claude Code plugin (**turma**) that installs into any project. Chico is the character who wields it, runs the work, and sharpens the craft on real results.

Two layers:
- **turma** = the craft. A Claude Code plugin. Agnostic, installable, versioned, open source. Layer 1.
- **Chico** = the operator. The character who wields turma and sharpens it on results. Layer 2.

## 1. What Chico is

A fractional growth specialist that plugs into any project. Not tied to one brand or roster. The projects Chico serves are private (named only in the gitignored `memory/` and `clients/`); the design does not depend on any specific one. Chico is summoned into a project, works its growth, watches the numbers, and writes what worked back into the craft.

See SOUL.md (the reason) and IDENTITY.md (who).

## 2. The two-layer architecture

**Layer 1, turma (the craft).** `turma/`. A plugin bundling skills (frameworks + methods), specialist subagents, commands, and read connectors. Knows nothing about a brand until the host project provides `brand.md`. Installs into any Claude Code project via the local marketplace. Open source, so other builders can clone and use it. Gets sharper over time via the learning loop.

**Layer 2, Chico (the operator).** The character plus the runtime that wields turma. Today: local Claude Code on the Max plan. Later: an autonomous agent (Claude Agent SDK) on a capped API budget. The operator is what turns a static toolkit into a specialist who learns.

## 3. The agnostic contract: brand.md

Every specialist reads one file the host project provides: `growth/brand.md`. Voice, audience, primary conversion goal, offer, banned phrases, channels, scoreboard. Same skills, different `brand.md`, different project. Template and worked (fictional) example in `turma/templates/` and `turma/examples/`. A real filled `brand.md` is private (see section 4).

## 4. The learning loop + the privacy boundary

When a specialist runs on a real project and a result comes in, the generalizable lesson is logged (`turma/templates/learnings.template.md`), tagged by vertical, and promoted into the skill once confidence is strong.

**One boundary does three jobs at once. It is the moat, the trust line, and the git line.** Raw project data stays in the project. Only the distilled, generalized technique crosses back into turma. One client's numbers never enter another client's playbook. The repo is public and pushes to GitHub, so filled `brand.md` files, raw learnings, and keys are gitignored (`clients/`, `**/growth/brand.md`, `**/*.local.md`, `.env*`) and never pushed. Only the generic craft and the sanitized techniques are committed. Business data structurally cannot reach GitHub.

## 5. Runtime + billing

- **Now (build + prove):** local Claude Code CLI on the Max subscription. Normal interactive use, no token risk beyond what's already paid.
- **Bounded automation** (nightly consolidation, on-demand runs): also fine on Max.
- **Layer 2 (24/7 autonomous loop):** Claude Agent SDK pointed at an **Anthropic API key with a hard monthly spend cap**, not the subscription. As of 2026-06-15 Anthropic paused the change that would have given SDK usage its own credit, so today SDK usage draws from the same subscription limits. A capped API key walls the always-on loop off from the Max limits entirely. Recheck the live metering rules before switch-on.
- **Compliance:** first-party tooling only (Claude Code CLI / Agent SDK). No OpenClaw or other third-party wrappers on the subscription (blocked, ToS). The API path removes that constraint if we ever want it.

## 6. Permission tiers

- **Green** (autonomous): research, competitive teardowns, internal notes, drafts that stay internal, sharpening the craft, filling `learnings.md`.
- **Yellow** (draft, approve, then ship): anything published under a project's brand, outreach, public commitments, edits to a project's `brand.md` or a skill's canon.
- **Red** (ask first): money (spend, API budget, paid tools), committing a project to a partnership or deal, anything legal / tax / compliance, anything touching a client's live accounts, buying a domain.

## 7. The projects (consumers, not the definition)

Agnostic by design. The specific projects Chico works are recorded privately in `memory/` and `clients/`, never in this public file. The first project is a live, low-stakes one Bissuh owns, chosen because it has a real audience and real data to sharpen against. "No first company" holds for the design. The design gets proven on the first real engagement.

## 8. Roadmap

**Phase 0. Foundation (done 2026-08-22).**
- [x] Name the craft layer (turma)
- [x] Plugin skeleton + local marketplace
- [x] brand.md contract + learnings.md contract
- [x] Privacy boundary (public craft, gitignored business data)
- [x] Re-mission SOUL / IDENTITY / SPEC to canon
- [x] Rewrite CLAUDE.md + memory for the new mission
- [x] Archive TBP-specific legacy (2026-08-22: deleted, with the craft mined out first)

**Phase 1. Port the craft (done 2026-08-22).**
- [x] Move all skills into turma/skills, decoupled to read brand.md
- [x] Wire the currently-unlinked skills so the whole set is invocable
- [x] Build the operator agent + the four commands. More specialists (distribution, copy, analytics) stay queued as backlog C-002, to build when a live engagement needs the split.

**Phase 2. Prove it on the first project (next, the current bottleneck, and unassigned).**
- [ ] Pick the project. As of 2026-08-22 there is no candidate attached; the earlier one was dropped. This is the blocking step, not a formality.
- [ ] Fill that project's brand.md (private)
- [ ] Run a real growth cycle, log learnings, promote the first technique

**Phase 3. Layer 2 runtime.**
- [ ] Agent SDK loop on a capped API key
- [ ] Autonomous run + write-back, spot-checked
- Design constraints (adopted 2026-08-16, from the Precht/Nitski mining into `turma:pauta`): approvals bind to the exact artifact (text + asset + destination + publish time) and any change voids them; a global kill switch; ambiguous errors go to a review queue, never blind retries; every post-approval step is idempotent and holds no editorial authority. Nothing autonomous decides what publishes.

## 9. Open questions

1. **Which project goes first?** No candidate is attached as of 2026-08-22. Everything in Phase 2 waits on this one call, and the craft stays unproven until it lands. Chico proposes, Bissuh decides. Once picked, its `brand.md` needs his inputs (audience, voice, goal, channels) and stays private.
2. **Layer 2 budget:** what monthly API cap is Chico allowed? (Red.)
3. **Repo location:** the folder still lives under `TBP/`, a project that no longer exists. Move it to a neutral path? (Touches paths + configs.) Still open.
4. ~~**Legacy cleanup.**~~ Resolved 2026-08-22. Everything TBP-era was deleted after the reusable craft was mined into turma. See the changelog below.

## 10. Changelog

- **2026-08-22**: Repo cleanup and the end of the TBP legacy. Phases 0 and 1 closed. The repo went from 4.0 GB to under 1 MB: the TBP video estate, the root Remotion renderer, the ops scripts and their launchd jobs (both had been failing every 30 minutes since 2026-05-10 on a macOS TCC block, unnoticed), the TBP-era root docs, and the private drafts and research inbox are gone. The craft that had never been ported was pulled into turma first: the gallery renderer and batch scheduler into `ghostshelf` (now theme-driven and brand-agnostic, typechecked and render-verified), the Instagram 10-image carousel cap and the self-complete test into `carousels` (the skill had been advising slide counts that error on Instagram), the free trend-research layer and the named-slot lineup into `ghostshelf`, and two operating lessons into `cta-machine`. Plugin at 0.7.0.
- **2026-08-16**: Ops layer added to turma (`turma:pauta`, plugin 0.6.0): delegate execution, keep judgment. Five contracts (reference bank, grounding packet, owner interview, approval binding, engagement boundary); production skills now ground and gate opinion-led work. Layer 2 approval-layer constraints adopted (Phase 3 above). Source: Bernardo Precht's content-agent architecture; principle from Osvald Nitski (Mercor) on 20VC.
- **2026-07-11.** Pivot. TBP retired as a project. Chico re-missioned to portable, project-agnostic growth specialist. turma plugin (open source) + local marketplace + brand.md / learnings.md contracts built. Privacy boundary set: public craft, gitignored business data. SOUL / IDENTITY / SPEC promoted to canon. Runtime decided: Max now, Agent SDK on capped API for Layer 2. Bissuh chose to keep the repo open source so others can use and learn from turma.
