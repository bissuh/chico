# TOOLS.md — paths, binaries, accounts

Operational reference. When Chico needs to know *where* something lives on this machine or *which* account we use for what, this is the lookup.

Update this file when a tool changes, when an account is swapped, or when a new dependency enters the stack.

## Workspace

- **Chico workspace root**: `/Users/bissuh/Documents/TBP/chico/`
- **TBP materials root** (outside Chico scope but read-only referenced): `/Users/bissuh/Documents/TBP/`
- **TBP Writing Manual**: `/Users/bissuh/Documents/TBP/TBP-WRITING-MANUAL.md` — source of truth for voice
- **Newsletter format guide**: `/Users/bissuh/Documents/TBP/newsletter-format-guide.md`
- **Existing published articles**: `/Users/bissuh/Documents/TBP/Articles/`

## Binaries

- **claude CLI**: resolved via shell PATH. Current install is Homebrew (`/opt/homebrew/bin/claude`), with an NVM copy also on disk (`/Users/bissuh/.nvm/versions/node/v22.22.2/bin/claude`). Scripts source `~/.zprofile` and `~/.zshrc` to pick up whichever comes first on PATH.
- **git**: system default
- **zsh**: `/bin/zsh` (used by scripts and launchd plists)

## Scheduling

- **Launchd agent directory**: `~/Library/LaunchAgents/`
- **Installed jobs** (check with `launchctl list | grep tbp.chico`):
  - `com.tbp.chico.consolidate-memory` — fires daily at 02:00, runs `scripts/consolidate-memory.sh`
  - `com.tbp.chico.heartbeat` — fires every 30 min, runs `scripts/heartbeat.sh` (once installed)

## Accounts and external services

Track what exists; never store credentials here.

- **Domain**: `thebillionperson.com` — registrar tracked in Bissuh's password manager
- **Newsletter platform**: beehiiv — dashboard: beehiiv.com (account is Bissuh's; Chico has no login)
- **Email**: Bissuh owns the sending identity; all subscriber email goes through beehiiv
- **Anthropic / Claude Max 20x subscription**: Bissuh's personal account, $200/mo. Never shared.
- **GitHub / git remote**: TBD — workspace git is local-only as of 2026-04-19 (no remote configured). Adding a remote is Red-tier (account setup).

## Tools not yet chosen (open questions)

These are placeholders. When a decision is made, update this file and mark the SPEC §13 question resolved.

- **Social scheduler**: undecided (Typefully / Buffer / Hypefury). SPEC §13 Q1.
- **Lead magnet hosting**: undecided
- **Dashboard (canvas/)**: undecided (plain HTML vs Next.js/Astro). SPEC §13 Q3.
- **First paid product format**: undecided. SPEC §13 Q4.

## Environment variables

None required in v0.1. If any are added (for an API key, a scheduler token, etc.), document them here and never commit them.

## Logs

- **Script logs**: `logs/<script-name>-YYYY-MM-DD.log` (gitignored)
- **Launchd stdout/stderr**: `logs/launchd-<job>.out` / `.err` (gitignored)

## State files

- `memory/heartbeat-state.json` — last-run timestamps for scheduled jobs. Read before deciding whether to run a catch-up pass. Written by the script that just ran.
