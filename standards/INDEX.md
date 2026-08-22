# standards/ (working notes)

The bar Chico measures work against. Each file here is a checklist or rubric he
loads when asked to **evaluate** something, as opposed to produce it.

Where this sits in the repo:

| Folder            | Function                                  |
| ----------------- | ----------------------------------------- |
| `knowledge-base/` | what Chico reads to learn (raw input)     |
| `playbooks/`      | how Chico runs one project (per project)  |
| `turma/skills/`   | how Chico does the work (method, public)  |
| **`standards/`**  | **the bar he grades against (rubric)**    |

## The sync contract

These are **copies**. The source of truth lives upstream, in the project repo
that owns each file. When Bissuh attaches new learnings upstream, the copy here
goes stale silently, which is the failure mode this folder has to avoid.

```
./standards/sync.sh              check every standard for drift, writes nothing
./standards/sync.sh --diff NAME  see exactly what changed upstream
./standards/sync.sh --pull NAME  overwrite the local copy from its source
./standards/sync.sh --pull-all   overwrite every local copy
```

Paths live in `standards/.sources`. **Run the check before any evaluation that
uses a standard.** Sync is one direction on purpose: a two way sync with no
conflict resolution is how an edit gets silently lost. If a standard should
live here instead of upstream, retire the source and drop its line from
`.sources`.

## The standards

### `social-app-design-principles.md`
**Covers:** viral growth, network effects, distribution, retention moats.
Testing discipline, idea filtering, beachhead audiences, engagement loops, and
the investment layer.

**Invoke when:** evaluating a consumer or social product feature, a launch plan,
a growth loop, or a retention story. Also when a product "has engagement" but
churns.

**Strongest material:** Section 7, the investment layer. Engagement keeps users
running, investment is what stops them jumping to a newer treadmill. The two
test questions are the sharpest thing in the file: does session 1,000 beat
session 10, and what would a leaving user have to rebuild from scratch. Also
strong: the three needs filter (love, money, play), the inflection point table,
and the 1 session to 7 opens loop heuristic.

**Watch out:** it is absolutist by design ("NEVER build an app to meet up with
friends", older audiences counted "on one finger"). Section 9 admits this and
tells you to discount the whole document. Treat the rules as priors with a
stated reason, not laws. The 9 point approval checklist at the end is the part
to actually run.

### `design-principles.md`
**Covers:** UI and UX craft for interfaces. Design tokens, hierarchy, spacing,
icons, interactive states, dark mode, charts, media overlays, redundancy
removal, and a pre ship checklist.

**Invoke when:** auditing a screen, a dashboard, a landing page, or a component
before it ships. Section XIV is the fast pass; the numbered sections are the
deep read.

**Strongest material:** the parts that give the reason and not just the number.
The halving rule behind the 8px grid, contrast as the actual source of
hierarchy, the shadow notice test, the gradient scrim for text over media, and
the signifiers section.

**Watch out:** it carries hard numbers presented as laws (60/30/10, max 4 font
sizes, max 2 weights, 100ms and 300ms feedback thresholds). Most of them do
carry a stated reason, which is what separates them from numerology. Where a
number has no reason attached, treat it as a default and not a rule.

### `ai-development-guide.md`
**Covers:** where an AI feature actually belongs in a product, and where it does
not. A do and do not list plus fit signals.

**Invoke when:** someone proposes an AI feature, or when deciding which part of
a workflow to point a model at.

**Strongest material:** the framing that AI should collapse steps in a workflow
users already have, never teach a new behavior. And the fit signals, especially
"users trust the output but hate the effort required to get there."

**Watch out:** it is 30 lines. A filter, not a method. It tells you what to
build and nothing about how. Pair it with a real product spec.

## Operating notes

**These files are not ours and they contain em dashes.** Never paste from a
standard into published output. Anything that graduates from here gets rewritten
in our own words and run through `turma:anti-ai-linguo`. They stay verbatim
because editing a source document falsifies it and breaks the sync diff. See the
provenance section in `README.md`.

**Public as of 2026-08-22.** Bissuh's call. Everything here is tracked except
`.sources`, which holds absolute paths and the names of the repos that own each
file. The attribution gap is real and recorded in `README.md`: neither of the two
larger documents names its original author, so the repo credits none and guesses
none. Worth closing if a source can be identified.

## Graduation candidates

**Rewritten 2026-08-22.** This section originally rejected `design-principles.md`
on the grounds that it is "interface craft, not growth craft." Bissuh widened the
mandate that same day and chose to let turma hold all craft rather than split it
across two layers, which repeals that reason entirely. Re-derived:

- **`social-app-design-principles.md`, section 7, the investment layer.** Still
  the strongest single piece of material in the folder. Engagement keeps users
  running; investment is what stops them switching. turma has nothing on
  retention moats, and `power-law`, `positioning` and `conversion-craft` all
  stop short of it. Strong candidate under either mandate.
- **`design-principles.md`.** In scope, and it lands in turma like anything
  else. The strongest material is the part that gives a reason rather than a
  number: the halving rule behind the 8px grid, contrast as the actual source of
  hierarchy, the shadow notice test, the gradient scrim. Strip the numerology
  before it becomes a skill, the same way `seo-strategy` rejected the SEO
  Machine's word-count rules.
- **`ai-development-guide.md`.** Thirty lines. A filter, not a method. Thin for
  its own skill regardless of mandate.

The mechanism question is separate from the placement question. One
`/audit <target> <standard>` entry point that loads a standard and runs its
checklist scales better than one skill per rubric: one mechanism, N standards,
and a new standard is just a file drop.

## Adding a new standard

1. Drop the file in `standards/`.
2. Add its `name<TAB>source path` line to `.sources`.
3. Add a section here: covers, invoke when, strongest material, watch out.
4. Run `./standards/sync.sh` to confirm it registers.
