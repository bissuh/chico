# Drop your 3 background images here

The CTA renders three scenes, each with a full-bleed 9:16 background:

- `bg1.png`: the "trapped" scene (under headline 1, the alarm line)
- `bg2.png`: the "action" scene (under headline 2)
- `bg3.png`: the "resolution" scene (under the URL)

Rules that matter more than the art style:

1. **9:16 vertical** (1080×1920 or any 9:16 ratio).
2. **Negative space where the text lands.** Scene 1 text sits center, scene 3 text sits center with the URL hero below. Keep those zones uncluttered.
3. **A dominant tone that matches your `brandColor`.** A 60%-opacity brand-color multiply is laid over every image, so busy or off-palette images still lock to your brand. But starting close to your color looks best.

No backgrounds? The CTA still renders. Each scene falls back to a clean brand-color gradient. Ship that first, add art later.

These files are gitignored by default (binary assets). Commit them only if you want them in your repo.
