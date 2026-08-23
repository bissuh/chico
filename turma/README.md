# turma

Chico's crew. A portable set of craft you install into any project: product judgment, design, engineering, marketing, and distribution.

## What this is

turma is Layer 1 of the Chico system: **the craft.** It's a Claude Code plugin that packages the frameworks, skills, and specialist agents Chico uses to make a project good and make it reach people. It knows nothing about your specific brand until you tell it. You drop one file (`brand.md`) into a project and the crew adapts to that project's voice, audience, and goal.

turma was growth craft only until 2026-08-22, when the mandate widened to cover whatever a project actually needs. The name still fits: turma is Portuguese for the crew, and the crew just got bigger.

Two layers, kept separate on purpose:

- **turma (this plugin) = the craft.** Agnostic. Installable. Versioned. It gets sharper over time.
- **Chico = the operator.** The character who wields the craft, runs the work, watches the numbers, and writes what worked back into the craft. Chico lives in the main repo, not here.

The plugin is the body of knowledge. Chico is the practitioner.

## What's inside

```
turma/
  .claude-plugin/plugin.json   the plugin manifest
  TOOLS.md                     the tool registry (what each skill uses, what it costs)
  skills/                      the specialists (frameworks + methods)
  agents/                      the chico agent (the operator, summonable into any project)
  commands/                    entry points (/turma:produce-week, /turma:growth-audit, etc.)
  templates/
    brand.template.md          the per-project config contract (the agnostic mechanism)
    learnings.template.md      the write-back format (how the craft learns)
    references.template.md     the reference bank (where ideas land before they become content)
  examples/
    brand.example.md           a filled reference config (fictional)
```

The skills read `brand.md` instead of hardcoding a brand. `turma:pauta` is the operating layer around them: it keeps the judgment (angles, opinions, approvals) with the project owner and the execution with the agent.

As the craft widens past growth, `brand.md` stops being sufficient on its own: it carries voice, audience and conversion, not a design system or a stack. New domains bring their own sibling contract and each skill declares which files it reads. `brand.md` keeps its current shape, so nothing already installed breaks.

Most skills are method only. Four ship runnable tooling next to the method, and none of it is required to use the skill:

- `ghostshelf/` a Remotion slide and reel renderer plus a batch scheduler for Instagram, TikTok, and YouTube Shorts. Themed from one file, `remotion/src/theme.ts`.
- `cta-machine/` a Remotion CTA renderer plus the scrape, stitch, upload, and schedule chain for a short-video engine.
- `search-console-connector/` a Search Console reader and an opportunity scorer.
- `beehiiv-connector/` and `youtube-connector/` thin read wrappers over their APIs.

Anything in those folders that publishes under a project's name is gated: the owner approves the exact artifact first. See `turma:pauta`, contract 4.

## The agnostic contract: brand.md

Every specialist reads one file the host project provides: `brand.md`. That file is the only place a brand's specifics live. Same skills, different `brand.md`, different project. See `templates/brand.template.md` for the fields and `examples/brand.example.md` for a filled one.

To use turma on a new project: copy `brand.template.md` into that project as `growth/brand.md`, fill it in, then invoke any specialist.

## What's public, what's private

turma (this plugin) is the craft. It's generic and safe to share or push to GitHub.

A project's real data is not. Never commit or push:
- a filled `brand.md` (a real audience, offer, numbers)
- a real `learnings.md` (raw results)
- API keys or connector output

Those live private: in the main repo's gitignored `clients/` workspace, or in each project's own gitignored `growth/` folder. The learning loop's rule is the same line: only the generalized, sanitized technique crosses back into turma. Hold that boundary and private business data structurally never reaches the public plugin.

## Install

Development (test it live without a marketplace):

```
claude --plugin-dir ./turma
```

Via the local marketplace (the main repo is the marketplace):

```
/plugin marketplace add /path/to/chico
/plugin install turma@chico-marketplace
```

Choose **project** scope to enable turma only in the project you're working in, or **user** scope for all projects. Skills are then invoked namespaced: `turma:story-craft`, `turma:name-craft`, and so on.

Note: the local marketplace `source` path gets validated on the first `/plugin marketplace add`. If the schema wants a different local-source form, it's a one-line fix in `.claude-plugin/marketplace.json`.

## How the craft learns

turma is not static. When Chico runs a specialist on a real project and sees a result, the generalizable lesson gets written back using `templates/learnings.template.md`, tagged by vertical, and eventually promoted into the skill itself. A hook that beats another 3:1 on a weight-loss audience becomes a tagged tactic every future install inherits.

The boundary: **raw project data never leaves the project.** Only the distilled, generalized technique travels back. One client's numbers don't land in another client's playbook, and they don't land on GitHub.

## Status

v0.10.0. Twenty two skills, the chico agent, four commands, three template contracts. The mandate widened past growth on 2026-08-22. `retention-craft` is the first skill on the other side of that line: it works on the product rather than the content, and it is the first to grade against a file in `standards/` instead of carrying its own bar. `aso-strategy` followed it, and pulled the two together: store ranking now weighs post-install signals, so retention and distribution stopped being separate problems for anything that ships to an app store. The rest of the shipped set is still growth heavy. The runtime (Chico as an autonomous agent wielding turma) is Layer 2, designed later.
