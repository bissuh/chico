# scripts/

Shell scripts and launchd plists that make Chico run on a schedule.

## What's here

- `consolidate-memory.sh` — nightly consolidation. Invokes `claude -p` with a prompt that tells Chico to run the `consolidate-memory` skill against a target date (default: yesterday). Safe to run manually any time.
- `launchd/com.tbp.chico.consolidate-memory.plist` — macOS launchd plist that fires the script daily at 02:00.

## Installing the launchd job

```sh
# From the workspace root:
cp scripts/launchd/com.tbp.chico.consolidate-memory.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.tbp.chico.consolidate-memory.plist
launchctl list | grep tbp.chico   # verify
```

To uninstall:

```sh
launchctl unload ~/Library/LaunchAgents/com.tbp.chico.consolidate-memory.plist
rm ~/Library/LaunchAgents/com.tbp.chico.consolidate-memory.plist
```

To update the plist after editing the version in this repo: unload, copy the new version into `~/Library/LaunchAgents/`, reload.

## Testing the script manually

```sh
./scripts/consolidate-memory.sh                  # consolidates yesterday
./scripts/consolidate-memory.sh 2026-04-19       # consolidates a specific day
tail -f logs/consolidate-$(date +%Y-%m-%d).log   # watch output
```

## Known limits

- **Sleeping Mac misses the 2am slot.** launchd for user agents does not catch up missed runs. If the machine is asleep at 02:00, the job is skipped for that night. Bissuh can run the script manually the next morning to catch up. A catch-up loop (check on wake, run if last run > 24h ago) is a v0.2 nice-to-have.
- **Claude binary lives under NVM.** The script sources `~/.zprofile` and `~/.zshrc` defensively so NVM's PATH edit loads. If a node upgrade changes the claude path, nothing in this repo needs to change as long as `claude` resolves via PATH after shell config loads.
- **Logs are not rotated.** `logs/` grows over time. Clean it up manually every few months or add a logrotate step in v0.2.

## Files this skill/script writes

- `memory/YYYY-MM-DD.md` (the consolidated daily memory)
- `inbox/rule-candidates-YYYY-MM-DD.md` (only when there are candidates)
- `memory/heartbeat-state.json` (updated `last_consolidation_at`)
- `logs/consolidate-YYYY-MM-DD.log` (script + claude stdout/stderr)
- `logs/launchd-consolidate.out` and `.err` (launchd's own capture; usually empty)
