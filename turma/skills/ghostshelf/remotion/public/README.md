# public/

Static assets the renderer can reach with `staticFile()`.

Put here:
- `logo.png` — transparent PNG, referenced by `THEME.logo` in `src/theme.ts`. Leave `THEME.logo` empty to render the handle with no logo.
- Any background images used by the `photo` slide layout. Reference them by filename: `{"layout": "photo", "bg": "bg1.png"}`.

These are the project's own brand assets. They stay in the host project, never in turma.
