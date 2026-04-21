---
name: beehiiv-api
description: Query The Billion Person's beehiiv data (subscribers, posts, stats, segments) via the v2 REST API. Invoke when Bissuh asks "how did last week's send do," "what's our subscriber count," "which post drove the most clicks," or any other read query about TBP's beehiiv state. Also invoke at the top of a weekly review or when a decision depends on real numbers rather than memory.
---

# beehiiv-api

Direct read access to TBP's beehiiv publication. Thin wrapper around the v2 REST API via `scripts/beehiiv.sh`.

## When to invoke

- Any question from Bissuh about TBP's current subscriber count, growth, open rate, click rate, or unsubscribe trend
- Before running a weekly review or producing a health-of-the-business summary
- When proposing an experiment and we need a baseline number to compare against
- When the answer to "is this idea working?" depends on real data, not memory

## When NOT to invoke

- Writing or scheduling a post → out of scope. Writes go through the beehiiv UI with Bissuh's approval (Yellow tier).
- Pulling full subscriber dumps for export → confirm with Bissuh first, this is a lot of data and PII.
- Anything under Red tier (billing, paid plans, plan changes).

## How to use

The wrapper lives at `scripts/beehiiv.sh`. It loads `BEEHIIV_API_KEY` and `BEEHIIV_PUB_ID` from `.env` at repo root (gitignored).

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

# Segments (starts empty until we create any)
./scripts/beehiiv.sh segments

# Automations (welcome sequences, etc)
./scripts/beehiiv.sh automations

# Escape hatch — any GET endpoint
./scripts/beehiiv.sh raw /publications/$BEEHIIV_PUB_ID/custom_fields
```

Pipe output through `python3 -m json.tool` or `jq` for readable formatting.

### Example workflows

**"How did last Saturday's send do?"**
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
Compare `active_subscriptions` to last week's number (if logged in `memory/` or `sessions/`).

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

When invoking this skill to answer a Bissuh question, always:

1. State the headline number first (e.g., "3,767 active subscribers, up X from last week")
2. Flag any metric outside healthy ranges (see targets below)
3. Tie findings back to the scoreboard they affect (narrative / health / thesis — see `memory/playbook.md`)
4. Propose a specific next action if a number is off trend

## Healthy ranges (McGarry benchmarks, canon in `knowledge-base/matt-mcgarry/`)

- Welcome email open rate: 60-80%
- Welcome email click rate: 10-20%
- Regular edition open rate: 40%+ (we are currently at 37%, slight gap)
- Regular edition click rate: 3%+ (we are currently at 1.7%, major gap)
- Unsubscribe rate per send: <0.5%
- Spam rate per send: <0.1%

## Write operations

Not wrapped. Intentional. Any POST/PATCH/DELETE to beehiiv goes through the dashboard with Bissuh's eyes on it. If we need scripted writes later, they get their own skill with its own approval flow.

## Related

- `backlog.md` → B-001 tracks the broader integration work
- `knowledge-base/matt-mcgarry/tactics.md` → the benchmarks above come from framework 3 (WEAC) and framework 4 (deliverability)
- `memory/playbook.md` → the three scoreboards we're reporting against

## Hard rules (inherits from `skills/README.md`)

This skill reads data only. It never edits operating canon, never writes to beehiiv, and never exports subscriber PII without explicit Bissuh approval (Yellow tier).
