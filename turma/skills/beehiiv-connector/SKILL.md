---
name: beehiiv-connector
description: Read a beehiiv publication's state (subscribers, posts, stats, segments) via the v2 REST API, read-only. Invoke when asked "how did last week's send do," "what's our subscriber count," "which post drove the most clicks," or any other read query about the project's beehiiv state. Also invoke at the top of a weekly review or when a decision depends on real numbers rather than memory. Reads the host publication's credentials from the project's own .env; never writes.
---

# beehiiv-connector

Direct read access to a project's beehiiv publication. Thin wrapper around the v2 REST API via `scripts/beehiiv.sh`.

**Before you start:** read the project's `brand.md`. Section 8 says whether beehiiv is the connected analytics source. Section 9 names the scoreboard numbers that actually matter for this project, and that is what you report against. The wrapper travels with this connector and reads `BEEHIIV_API_KEY` and `BEEHIIV_PUBLICATION_ID` from the host project's `.env` (gitignored). No publication is hardcoded in the skill.

## When to invoke

- Any question about the project's current subscriber count, growth, open rate, click rate, or unsubscribe trend
- Before running a weekly review or producing a health-of-the-business summary
- When proposing an experiment and you need a baseline number to compare against
- When the answer to "is this idea working?" depends on real data, not memory

## When NOT to invoke

- Writing or scheduling a post -> out of scope. Writes go through the beehiiv UI with the project owner's approval (Yellow tier).
- Pulling full subscriber dumps for export -> confirm with the project owner first, this is a lot of data and PII.
- Anything under Red tier (billing, paid plans, plan changes).

## How to use

The wrapper lives at `scripts/beehiiv.sh` and ships with this connector. Point it at the host project by setting `BEEHIIV_API_KEY` and `BEEHIIV_PUBLICATION_ID` in the project's `.env` (gitignored); the wrapper reads them at call time. Set those two vars in the project before the first call.

### Core commands

```bash
# Publication-level stats (subs, average open/click rate, total sent)
./scripts/beehiiv.sh stats

# Most recent posts with stats inline
./scripts/beehiiv.sh posts 10

# Full detail + stats for one post (opens, clicks, top URLs, unsubs, spam)
./scripts/beehiiv.sh post <post_id>

# Most recent subscribers with engagement stats and referrals
./scripts/beehiiv.sh subscribers 25

# One subscriber's detail
./scripts/beehiiv.sh sub <subscription_id>

# Segments (starts empty until any are created)
./scripts/beehiiv.sh segments

# Automations (welcome sequences, etc)
./scripts/beehiiv.sh automations

# Escape hatch: any GET endpoint
./scripts/beehiiv.sh raw /publications/$BEEHIIV_PUBLICATION_ID/custom_fields
```

Pipe output through `python3 -m json.tool` or `jq` for readable formatting.

### Example workflows

**"How did the last send do?"**
```bash
./scripts/beehiiv.sh posts 1 | python3 -m json.tool
# grab the post id from the top result, then:
./scripts/beehiiv.sh post <post_id> | python3 -m json.tool
```
Report: open rate, click rate, top 3 clicked URLs, unsub count, spam reports.

**"Where are we on subscriber growth this week?"**
```bash
./scripts/beehiiv.sh stats | python3 -m json.tool
```
Compare `active_subscriptions` to last week's number (if you logged it).

**"Which post is our best-performing ever?"**
```bash
./scripts/beehiiv.sh posts 50 | python3 -c "
import sys, json
d = json.load(sys.stdin)
rows = []
for p in d['data']:
    s = p.get('stats', {}).get('email', {})
    rows.append((s.get('open_rate', 0), p.get('title'), s.get('click_rate', 0)))
for r in sorted(rows, reverse=True):
    print(r)
"
```

## Reporting convention

When invoking this connector to answer a question, always:

1. State the headline number first (e.g., "X active subscribers, up Y from last week")
2. Flag any metric outside healthy ranges (see benchmarks below)
3. Tie findings back to the scoreboard they affect (the project's scoreboard, from `brand.md` section 9)
4. Propose a specific next action if a number is off trend

## Healthy ranges (general newsletter benchmarks)

Default flags to use when `brand.md` section 9 does not set its own targets. These are industry reference points for email newsletters, not project-specific goals. If `brand.md` names different targets, those win.

- Welcome email open rate: 60-80%
- Welcome email click rate: 10-20%
- Regular edition open rate: 40%+
- Regular edition click rate: 3%+
- Unsubscribe rate per send: <0.5%
- Spam rate per send: <0.1%

## Write operations

Not wrapped. Intentional. Any POST/PATCH/DELETE to beehiiv goes through the dashboard with the project owner's eyes on it. If scripted writes are needed later, they get their own skill with its own approval flow.

## Related

- The project's `brand.md`: section 8 (whether beehiiv is the connected source) and section 9 (the scoreboard this reports against).
- `turma:youtube-connector`: the same read-only pattern for a YouTube channel.
- The benchmarks above are general email-newsletter reference points; the project's own targets live in `brand.md`.

## Hard rules

- Reads the project's `brand.md` first. The connected source and the scoreboard come from there, never hardcoded.
- Reads data only. Never writes to beehiiv (no POST/PATCH/DELETE). Writes go through the dashboard at Yellow tier.
- Never edits operating canon (the project's SOUL / IDENTITY / CLAUDE / SPEC / memory files, if present).
- Never exports subscriber PII without explicit owner approval (Yellow tier).
- Connector output is raw project data: keep it private. Never commit it, never push it, never paste it into public content. This is turma's standing boundary (see the plugin README).
- No dashes, no AI tells in any reported output.
