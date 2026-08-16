# Outbox

Finished drafts land here for Bissuh to review. One file per deliverable.

## File header format

Every outbox file starts with frontmatter:

```
---
type: [x-post | linkedin-post | tiktok-script | email | landing-page | lead-magnet | research | other]
status: [draft | review-needed | approved | published | dropped]
tier: [green | yellow | red]
created: YYYY-MM-DD
for: [which channel / audience / campaign]
---
```

## Status lifecycle

1. `draft`: Chico is still working on it, not ready for review
2. `review-needed`: ready for Bissuh, flagged in the session log
3. `approved`: Bissuh said yes to the exact artifact: this text, these assets, this destination, this publish time. Change any of those and the file drops back to `review-needed`. Chico ships exactly what was approved.
4. `published`: it's live, include the URL at bottom of file
5. `dropped`: decided not to ship, include one-line reason

## Folder layout (optional, use if it gets busy)

```
outbox/
  social/
  email/
  landing-pages/
  lead-magnets/
  research/
  archive/   (move here after published, 30+ days old)
```

## Rules

- Never move something from `review-needed` to `approved` without Bissuh's explicit yes.
- Approval binds to the exact artifact (`turma:pauta` contract 4). Any edit after the yes, however small, reopens review. No "quick tweak after the approval" ships unreviewed.
- "Freeze publishing" from Bissuh stops everything mid-flight, no questions asked. Anything ambiguous during a ship (an error, a changed asset, a stale link) comes back as a review item, never a silent retry.
- Once `published`, do not delete. Archive. We learn from what shipped.
- If a draft is `draft` for more than 3 days, flag it. Either finish or drop.
- When publishing a final version, copy-paste the final URL into the file and commit the status change.
