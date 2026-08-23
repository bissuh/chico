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
| `design-principles.md` | interfaces. Tokens, hierarchy, spacing, icons, states, dark mode, charts, media overlays, progress and completion, and a pre ship checklist. |
| `social-app-design-principles.md` | consumer and social products. Test discipline, idea filters, beachhead audiences, engagement loops, the store-search bar for anything that ships to an app store, the retention mechanics that decide whether a game layer is real or theater, and the investment layer that separates retention from a treadmill. |
| `ai-development-guide.md` | AI features. Where a model belongs in a workflow and where it does not. |

`INDEX.md` carries the working notes for each one: when to reach for it, its
strongest material, and what to distrust in it. Read that before running an
evaluation, not just the rubric itself.

## Keeping them honest

Most of these started as **copies**. The source of truth for each lives in the
project repo that owns it, so a standard here goes stale the moment its source
picks up a new lesson, silently, which is the failure this folder exists to
avoid.

```
./standards/sync.sh              check every standard, writes nothing
./standards/sync.sh --diff NAME  see exactly what changed upstream
./standards/sync.sh --pull NAME  overwrite the local copy from its source
./standards/sync.sh --pull-all   overwrite every unforked copy
```

A standard is either a **copy** or a **fork**. A copy tracks its source exactly,
and any difference is drift to pull. A fork carries sections we wrote on top of
the inherited material, so a difference is permanent and expected. Sync reports a
fork as `FORKED` and **refuses to pull over it**, because that would silently
delete our work. On a fork, `--diff` is the tool: read what moved upstream and
merge it in by hand.

Paths live in `.sources`, which is gitignored because it holds absolute paths. A
third tab-separated column reading `fork` marks a fork. Copy `.sources.example`
and fill in your own. Sync runs one direction on purpose: a two way sync with no
conflict resolution eventually eats an edit.

Run the check before any evaluation. A stale rubric is worse than no rubric,
because it still feels authoritative.

## Provenance, and why these read differently

**Most of this is not ours.** These are working copies of guidance gathered from
several places and refined in use. `design-principles.md` credits Stripe, Airbnb
and Linear as influences on its title line; `social-app-design-principles.md`
opens by grounding itself in a decade of building consumer social apps. Neither
records its original author, so this repo does not claim one and does not guess.
If you recognise a source, say so and it gets credited.

**Some of it is ours, and it is marked.** Where we learn something a standard
should have covered, it gets written into the standard rather than filed
somewhere new. Those sections are ours and are listed here so the two are never
confused:

| File | Ours |
| ---- | ---- |
| `social-app-design-principles.md` | Section 7, Retention Mechanics. The store-search subsection at the end of Section 4, with its pre submit bar. The gamification and store rows in Section 9, and the mechanic-test gate on the final checklist. |
| `design-principles.md` | Section XX, Progress and Completion, and its pre ship line. |
| `ai-development-guide.md` | The competence rule in the don'ts, and the pride-versus-resentment fit signal. |

The **inherited** material is kept verbatim, which is why the files break house
style. This repo bans em dashes in anything public, and the inherited prose is
full of them. Editing it to match our voice would falsify a source document and
wreck the diff against upstream, so it stays as written. What we add is written
to house style, which is also the fastest way to tell the two apart on the page.

The rule that follows: **never paste from a standard into published output.**
Anything that graduates from here gets rewritten in our own words and run
through `turma:anti-ai-linguo`. A rubric is something to think with, not
something to quote.

## Adding one

1. Drop the file in `standards/`.
2. Add its `name<TAB>source path` line to `.sources`. Append a third `fork`
   column the moment you write your own section into it.
3. Add a section to `INDEX.md`: covers, invoke when, strongest material, watch out.
4. Run `./standards/sync.sh` to confirm it registers.

A standard with no upstream owner simply gets no `.sources` line. Sync ignores
it, which is correct: there is nothing to drift from.
