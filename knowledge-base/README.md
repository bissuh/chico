# Knowledge Base — sources Chico studies

This is Chico's self-education stack. These are the creators and businesses TBP borrows tactics from. Organize by source, add dated notes, extract tactics into `memory/playbook.md`.

## How this folder works

Each source gets its own subfolder. Inside each:
- `profile.md` — who they are, why they matter to TBP
- `teardown.md` — structural analysis of their best work
- `tactics.md` — extracted patterns TBP can test
- `notes/` — dated logs from new material ingested

## Priority sources (week-one ingestion)

### Newsletter operators
- **Matt McGarry — Newsletter Operator**
  - Why: the canonical newsletter growth operator
  - What to study: welcome email structure, recommendation flywheel, scaling playbook
- **Louis Nicholls — Sparkloop**
  - Why: built the infra layer behind half of newsletter growth
  - What to study: recommendation network mechanics, paid vs. reciprocal

### Solo creator canon
- **Dan Koe**
  - Why: TBP's article structure benchmark (already referenced in project instructions)
  - What to study: long-form X article structure, one-person business loop
- **Justin Welsh**
  - Why: LinkedIn distribution, solopreneur productization
  - What to study: content-to-product pipeline, $5M solo business structure
- **Dickie Bush — Ship 30 for 30**
  - Why: writing cadence, audience-building via cohort
  - What to study: writing discipline, atomic essay format
- **Sahil Bloom**
  - Why: narrative framing, cross-platform repurposing
  - What to study: one-idea-to-ten-posts workflow

### Newsletter businesses at scale (teardowns)
- **Morning Brew**
  - Why: sold for $75M, the reference case for newsletter exits
  - What to study: voice at scale, ad network, referral program
- **The Hustle**
  - Why: sold to HubSpot, proved B2B newsletter play
  - What to study: voice, Trends premium tier, enterprise angle
- **Milk Road**
  - Why: niche crypto newsletter, fast exit
  - What to study: niche-first growth, voice, monetization speed
- **The Pomp Letter**
  - Why: creator-led paid newsletter at scale
  - What to study: premium conversion, creator trust

### Platform-specific
- **beehiiv case studies**
  - Why: we live on this platform, use what the platform ships
  - What to study: Boosts network, Recommendations engine, paid features

## Secondary sources (add later)

- Lenny Rachitsky (newsletter + product audience)
- Ben Thompson (Stratechery — premium model reference)
- Packy McCormick (Not Boring — narrative + venture angle)
- Tim Ferriss (audience-to-product pipeline, old but still works)

## What NOT to over-index on

- General "how to grow on Twitter" advice that ignores TBP's niche
- Newsletter advice aimed at B2B SaaS companies (different audience)
- Anything that optimizes for vanity metrics Bissuh does not care about (follower counts on platforms we won't use, etc.)

## Nightly ingestion job (when scheduled task is set up)

Routine:
1. Pull new content from priority sources (RSS, newsletter subs, podcast transcripts)
2. For each new piece, write one line into `notes/YYYY-MM-DD.md`:
   - Source, title, one key takeaway, one proposed TBP test
3. At end of week, propose top 3 experiments to add to the playbook (Yellow — Bissuh approves)

## Format for teardown files

When analyzing a piece of content:

```
# [Source] — [Title] — [Date published]

## Structure
- Hook:
- Body beats:
- CTA:

## Voice signature
- Sentence patterns:
- Vocabulary tells:
- Rhythm:

## What works
- [tactic]

## What wouldn't translate to TBP
- [tactic] — why it doesn't fit

## Test we could run
- [specific experiment]
```

Keep these short. The goal is extractable tactics, not literature review.
