# ghostshelf tooling

Two scripts and a renderer. Method is in `SKILL.md`; this is the plumbing that runs it.

## Install into a project

```bash
cp -r <turma>/skills/ghostshelf/remotion ./remotion
cp -r <turma>/skills/ghostshelf/scripts ./scripts
cp <turma>/skills/ghostshelf/batch.example.json ./batch.json
cp <turma>/skills/ghostshelf/.env.example ./.env      # then fill it

cd remotion && npm install && cd ..
pip install requests
npm install -g @gitroom/postiz-cli   # only needed to upload media
```

Then edit `remotion/src/theme.ts` once: handle, logo, wordmark, palettes. That file is the only thing standing between the renderer and the project's brand. Pull the values from the project's `brand.md`.

## The loop

```bash
# 1. write props (one JSON per slide, or one per reel) into props/<slug>/
# 2. render
./scripts/render_batch.py batch.json

# 3. eyeball out/ , then get the owner's approval on batch.json as it stands
# 4. schedule
set -a && source .env && set +a
./scripts/schedule_batch.py batch.json --dry-run
./scripts/schedule_batch.py batch.json
```

`--dry-run` prints every call and sends nothing. Run it first, every time.

## Props

A carousel is a folder of slide props, sorted by the trailing number in the filename. A reel is one props file.

```json
{"layout": "cover", "theme": "brand", "kicker": "Built With AI",
 "title": "The headline", "subtitle": "The line under it",
 "slideNo": 1, "slideTotal": 10, "footnote": "save this"}
```

Slide layouts: `cover`, `statement`, `list`, `prompt`, `detail`, `photo`. Reel props take `kicker`, `lines` (an array; duration follows the count), and `cta`.

## Preview without rendering

```bash
cd remotion && npx remotion studio src/index.ts
```

## Approval binding

The owner approves `batch.json` as it stands: caption, media, destination, and publish time as one unit. Editing any of them after the nod voids the approval. See `turma:pauta`, contract 4.
