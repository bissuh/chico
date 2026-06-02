#!/usr/bin/env python3
"""
Stitch the first N seconds of each scraped short onto the front of your CTA video.

Reads {workdir}/assets/source_hooks/{channel_slug}/manifest.json,
extracts the first HOOK_SEC seconds of each source short,
concatenates your CTA video, normalizes to 1080x1920 9:16,
writes finished MP4s to {workdir}/assets/finished/{channel_slug}/{video_id}.mp4.

Skips video IDs that already have a finished file.

Usage:
    ./stitch_hooks.py <channel_slug> [<cta_path>] [<hook_seconds>]

Defaults:
    cta_path       = {workdir}/assets/cta.mp4
    hook_seconds   = 3

Examples:
    ./stitch_hooks.py some_creator
    ./stitch_hooks.py some_creator assets/cta.mp4 3

Working directory defaults to the current dir; override with CTA_WORKDIR.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

WORKDIR = Path(os.environ.get("CTA_WORKDIR", Path.cwd())).resolve()
ASSETS = WORKDIR / "assets"
HOOKS_DIR = ASSETS / "source_hooks"
FINISHED_DIR = ASSETS / "finished"

DEFAULT_CTA = ASSETS / "cta.mp4"
DEFAULT_HOOK_SEC = 3
TARGET_W, TARGET_H = 1080, 1920


def normalize_filter(target_w: int, target_h: int) -> str:
    return (
        f"scale={target_w}:{target_h}:force_original_aspect_ratio=decrease,"
        f"pad={target_w}:{target_h}:(ow-iw)/2:(oh-ih)/2,"
        f"setsar=1"
    )


def stitch(source: Path, cta: Path, output: Path, hook_sec: int) -> bool:
    """One ffmpeg call: trim source to hook_sec, normalize both, concat with CTA, re-encode."""
    nf = normalize_filter(TARGET_W, TARGET_H)
    filter_complex = (
        f"[0:v]trim=0:{hook_sec},setpts=PTS-STARTPTS,{nf}[v0];"
        f"[0:a]atrim=0:{hook_sec},asetpts=PTS-STARTPTS,aresample=44100[a0];"
        f"[1:v]{nf}[v1];"
        f"[1:a]aresample=44100[a1];"
        f"[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]"
    )
    cmd = [
        "ffmpeg",
        "-y",
        "-loglevel",
        "error",
        "-i",
        str(source),
        "-i",
        str(cta),
        "-filter_complex",
        filter_complex,
        "-map",
        "[v]",
        "-map",
        "[a]",
        "-c:v",
        "libx264",
        "-preset",
        "veryfast",
        "-crf",
        "20",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-movflags",
        "+faststart",
        str(output),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ! ffmpeg failed: {result.stderr.strip().splitlines()[-1]}")
        return False
    return True


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print(__doc__)
        sys.exit(1)

    channel_slug = sys.argv[1]
    cta = Path(sys.argv[2]).resolve() if len(sys.argv) >= 3 else DEFAULT_CTA
    hook_sec = int(sys.argv[3]) if len(sys.argv) == 4 else DEFAULT_HOOK_SEC

    if not cta.exists():
        sys.exit(f"CTA video not found: {cta}. Render it first (see remotion/), then place it at assets/cta.mp4")

    manifest_path = HOOKS_DIR / channel_slug / "manifest.json"
    if not manifest_path.exists():
        sys.exit(f"manifest not found: {manifest_path}. Run scrape_shorts.py first.")

    with open(manifest_path) as f:
        manifest = json.load(f)

    out_dir = FINISHED_DIR / channel_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    videos = manifest.get("videos", [])
    print(f"Channel: {manifest['channel_title']}")
    print(f"CTA:     {cta}")
    print(f"Output:  {out_dir}")
    print(f"Hook:    {hook_sec}s")
    print()

    succeeded = 0
    skipped = 0
    failed = 0

    for i, video in enumerate(videos, 1):
        vid = video["id"]
        source_rel = video.get("local_path")
        if not source_rel:
            failed += 1
            continue
        source = WORKDIR / source_rel
        if not source.exists():
            print(f"[{i}/{len(videos)}] {vid}: source missing, skipping")
            failed += 1
            continue

        out_path = out_dir / f"{vid}.mp4"
        if out_path.exists():
            print(f"[{i}/{len(videos)}] {vid}: already done")
            skipped += 1
            continue

        print(f"[{i}/{len(videos)}] {vid}: stitching {video['title'][:60]!r}")
        if stitch(source, cta, out_path, hook_sec):
            succeeded += 1
        else:
            failed += 1

    print()
    print(f"Done. {succeeded} new, {skipped} already done, {failed} failed.")
    print(f"Finished videos: {out_dir}")


if __name__ == "__main__":
    main()
