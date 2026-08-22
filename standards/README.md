# standards/

The bar Chico grades against. Each file here is a checklist or rubric he loads
when the job is to **evaluate** something rather than produce it: audit this
screen, pressure test this feature, is this growth loop real.

This is a different job from the neighbouring folders. `knowledge-base/` is what
Chico reads to learn, `playbooks/` is how he runs one project, `turma/skills/`
is how he does the work. `standards/` is the yardstick.

## What is here

| File | Grades |
| ---- | ------ |
| `design-principles.md` | interfaces. Tokens, hierarchy, spacing, icons, states, dark mode, charts, media overlays, and a pre ship checklist. |
| `social-app-design-principles.md` | consumer and social products. Test discipline, idea filters, beachhead audiences, engagement loops, and the investment layer that separates retention from a treadmill. |
| `ai-development-guide.md` | AI features. Where a model belongs in a workflow and where it does not. |

`INDEX.md` carries the working notes for each one: when to reach for it, its
strongest material, and what to distrust in it. Read that before running an
evaluation, not just the rubric itself.

## Keeping them honest

These are **copies**. The source of truth for each lives in the project repo
that owns it, so a standard here goes stale the moment its source picks up a new
lesson, silently, which is the failure this folder exists to avoid.

```
./standards/sync.sh              check every standard for drift, writes nothing
./standards/sync.sh --diff NAME  see exactly what changed upstream
./standards/sync.sh --pull NAME  overwrite the local copy from its source
./standards/sync.sh --pull-all   overwrite every local copy
```

Paths live in `.sources`, which is gitignored because it holds absolute paths.
Copy `.sources.example` and fill in your own. Sync runs one direction on
purpose: a two way sync with no conflict resolution eventually eats an edit.

Run the check before any evaluation. A stale rubric is worse than no rubric,
because it still feels authoritative.

## Provenance, and why these read differently

**Most of this is not ours.** These are working copies of guidance gathered from
several places and refined in use. `design-principles.md` credits Stripe, Airbnb
and Linear as influences on its title line; `social-app-design-principles.md`
opens by grounding itself in a decade of building consumer social apps. Neither
records its original author, so this repo does not claim one and does not guess.
If you recognise a source, say so and it gets credited.

They are kept **verbatim**, which is why they break house style. This repo bans
em dashes in anything public, and these files are full of them. Editing them to
match our voice would falsify a source document and break the diff that keeps
them in sync, so they stay as written.

The rule that follows: **never paste from a standard into published output.**
Anything that graduates from here gets rewritten in our own words and run
through `turma:anti-ai-linguo`. A rubric is something to think with, not
something to quote.

## Adding one

1. Drop the file in `standards/`.
2. Add its `name<TAB>source path` line to `.sources`.
3. Add a section to `INDEX.md`: covers, invoke when, strongest material, watch out.
4. Run `./standards/sync.sh` to confirm it registers.
