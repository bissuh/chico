# Chico: Layer 2 Runtime (design)

> Status: designed, not activated. Activation needs a monthly API budget cap from Bissuh (Red) and a recheck of the Agent SDK metering rules. Until then, Chico runs interactively via Claude Code (Layer 2 off).

## What Layer 2 is

Today Chico runs interactively: Bissuh opens Claude Code, summons Chico (`/turma:chico`), Chico works, the session ends. Layer 2 makes Chico an **autonomous, summonable agent**: a process that can be pointed at a project, run a growth cycle on its own, respect the permission tiers, and write sanitized learnings back to turma so the craft compounds without a human in the loop for every step.

The craft (turma) does not change. Layer 2 is just a different way of running the operator that wields it.

## The runtime: Claude Agent SDK

First-party. The same engine under Claude Code, run headless on a server, in a loop, with MCP connectors and subagents. Chosen because:

- It reuses the exact turma plugin, skill, and agent architecture. One mental model, not two.
- It is ToS-safe, unlike third-party wrappers (OpenClaw and the like) which are blocked on the subscription.
- It supports the long-running and summoned patterns Layer 2 needs.

## Billing: a capped API key, not the subscription

As of 2026-06-15 Anthropic paused the change that would have given Agent SDK usage its own credit, so today SDK usage draws from the same limits as interactive Claude Code. An always-on loop on the Max subscription would compete with, and could exhaust, interactive use.

So Layer 2 runs on an **Anthropic API key with a hard monthly spend cap**, separate from the Max subscription. A capped budget cannot touch the interactive limits. Bissuh sets the ceiling. When it is hit, the loop stops. Recheck the live metering before switch-on (the pause may have lifted, possibly in our favor).

## Architecture sketch

```
summon(project):
  read the project's brand.md + reachable analytics (connectors)
  plan the growth cycle (growth-audit)
  for each move:
    Green work: do it (research, drafts to outbox, internal analysis)
    Yellow work: draft to outbox, stop, notify the owner
    Red work:  stop, ask the owner
  capture the sanitized, generalized technique -> learnings -> promote to turma
  report
```

The loop is bounded by the permission tiers, not just by tokens. Yellow and Red are hard stops that hand back to a human. The autonomy is in the Green work and the orchestration, not in publishing or spending.

## Boundaries in the runtime

- **Permission tiers hold.** The agent drafts under Yellow (to `outbox/`), never publishes. It stops on Red. It spends nothing beyond the capped budget it was given.
- **Privacy holds.** Raw project data stays in the project. Only sanitized techniques cross back to turma. Nothing private is committed to the public repo.
- **First-party only.** Agent SDK, no third-party harnesses on the subscription.

## Activation checklist

1. Bissuh decides the monthly API spend cap (Red).
2. Recheck the current Agent SDK metering rules.
3. Provision an Anthropic API key with the cap set.
4. Stand up the loop (Agent SDK, headless), pointed at one project first to dogfood.
5. Spot-check the first autonomous cycles before widening.
