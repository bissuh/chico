#!/usr/bin/env python3
"""
Render a batch manifest to images and videos with Remotion.

Carousels render one PNG per slide into out/<slug>/slide-N.png.
Reels render one MP4 into out/<slug>.mp4.

Usage:
  ./render_batch.py batch.json
  ./render_batch.py batch.json --only carousel-01-stack
  ./render_batch.py batch.json --dry-run

Reads GHOSTSHELF_WORKDIR (defaults to the current directory) for where
props/ and out/ live. The renderer itself lives in remotion/.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
ENTRY = "src/index.ts"


def sorted_props(d: Path):
    """Slide props sorted by trailing number, so slide-10 lands after slide-9."""
    def key(p: Path):
        stem = p.stem
        digits = ""
        for ch in reversed(stem):
            if ch.isdigit():
                digits = ch + digits
            else:
                break
        return (int(digits) if digits else 0, stem)

    return sorted(d.glob("*.json"), key=key)


def run(cmd, cwd, dry):
    print("   " + " ".join(str(c) for c in cmd))
    if dry:
        return True
    return subprocess.run(cmd, cwd=cwd).returncode == 0


def find_renderer(work, override):
    """Host project's own copy wins; the skill's bundled one is the fallback."""
    for candidate in ([Path(override).resolve()] if override else []) + [work / "remotion", SKILL_DIR / "remotion"]:
        if (candidate / ENTRY).exists():
            return candidate
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("manifest")
    ap.add_argument("--only", help="render just this slug")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--workdir", default=None, help="where props/ and out/ live (default: manifest's folder)")
    ap.add_argument("--renderer", default=None, help="path to the remotion/ project (default: <workdir>/remotion)")
    a = ap.parse_args()

    manifest = Path(a.manifest).resolve()
    if not manifest.exists():
        sys.exit(f"manifest not found: {manifest}")
    work = Path(a.workdir).resolve() if a.workdir else manifest.parent

    remotion = find_renderer(work, a.renderer)
    if remotion is None:
        sys.exit(f"renderer not found. Looked in {work / 'remotion'} and {SKILL_DIR / 'remotion'}.")
    print(f"renderer: {remotion}")

    batch = json.loads(manifest.read_text())
    out = work / "out"
    out.mkdir(parents=True, exist_ok=True)

    ok = failed = skipped = 0
    for post in batch.get("posts", []):
        slug = post["slug"]
        if a.only and slug != a.only:
            continue
        kind = post.get("type", "carousel")
        props = (work / post["props"]).resolve()

        if not props.exists():
            print(f"{slug}: props missing at {props}")
            failed += 1
            continue

        print(f"\n{slug}  ({kind})")

        if kind == "carousel":
            files = sorted_props(props) if props.is_dir() else [props]
            if not files:
                print(f"  no slide props in {props}")
                failed += 1
                continue
            dest = out / slug
            dest.mkdir(parents=True, exist_ok=True)
            for i, f in enumerate(files, start=1):
                target = dest / f"slide-{i}.png"
                if target.exists() and not post.get("force"):
                    skipped += 1
                    continue
                good = run(["npx", "remotion", "still", ENTRY, "Slide", str(target), f"--props={f}"], remotion, a.dry_run)
                ok += good
                failed += not good
        elif kind == "reel":
            target = out / f"{slug}.mp4"
            if target.exists() and not post.get("force"):
                print("  exists, skipping (set \"force\": true in the manifest to re-render)")
                skipped += 1
                continue
            good = run(["npx", "remotion", "render", ENTRY, "Reel", str(target), f"--props={props}"], remotion, a.dry_run)
            ok += good
            failed += not good
        else:
            print(f"  unknown type {kind}, skipping")
            skipped += 1

    print(f"\nDONE. rendered {ok}, skipped {skipped}, failed {failed}. Output: {out}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
