#!/usr/bin/env python3
"""
Upload every stitched short in {workdir}/assets/finished/{channel_slug}/ to Postiz.
Captures the returned hosted URL and writes {workdir}/assets/postiz_uploads.json
as the persistent ledger so we never re-upload the same video.

Usage:
    ./upload_finished.py [channel_slug]
    ./upload_finished.py             # uploads from every finished/ subfolder
    ./upload_finished.py some_creator  # only this channel

Requires: postiz CLI installed, POSTIZ_API_KEY in env (loaded externally).
    set -a && source .env && set +a
Working directory defaults to the current dir; override with CTA_WORKDIR.
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

WORKDIR = Path(os.environ.get("CTA_WORKDIR", Path.cwd())).resolve()
FINISHED_DIR = WORKDIR / "assets" / "finished"
LEDGER_PATH = WORKDIR / "assets" / "postiz_uploads.json"


def load_ledger() -> dict:
    if not LEDGER_PATH.exists():
        return {}
    with open(LEDGER_PATH) as f:
        return json.load(f)


def save_ledger(ledger: dict) -> None:
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, sort_keys=True)


def upload(path: Path) -> dict | None:
    """Calls postiz upload, returns parsed JSON dict or None on failure."""
    result = subprocess.run(
        ["postiz", "upload", str(path)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  ! upload failed: {result.stderr.strip()}")
        return None
    payload = result.stdout
    start = payload.find("{")
    if start == -1:
        print(f"  ! no JSON in postiz output: {payload[:200]}")
        return None
    try:
        return json.loads(payload[start:])
    except json.JSONDecodeError as e:
        print(f"  ! JSON parse error: {e}")
        return None


def main():
    if not os.environ.get("POSTIZ_API_KEY"):
        sys.exit("POSTIZ_API_KEY not in env. Source .env first: set -a && source .env && set +a")

    only_channel = sys.argv[1] if len(sys.argv) > 1 else None

    ledger = load_ledger()
    print(f"Loaded ledger with {len(ledger)} prior uploads")

    if only_channel:
        channel_dirs = [FINISHED_DIR / only_channel]
        if not channel_dirs[0].exists():
            sys.exit(f"Channel folder not found: {channel_dirs[0]}")
    else:
        channel_dirs = sorted(d for d in FINISHED_DIR.iterdir() if d.is_dir())

    new_uploads = 0
    skipped = 0
    failed = 0

    for channel_dir in channel_dirs:
        slug = channel_dir.name
        videos = sorted(channel_dir.glob("*.mp4"))
        print(f"\n--- {slug} ({len(videos)} files) ---")
        for video in videos:
            video_id = video.stem
            ledger_key = f"{slug}/{video_id}"
            if ledger_key in ledger:
                print(f"  skip {video_id} (already uploaded)")
                skipped += 1
                continue
            print(f"  upload {video_id}...")
            payload = upload(video)
            if payload is None:
                failed += 1
                continue
            ledger[ledger_key] = {
                "channel_slug": slug,
                "video_id": video_id,
                "local_path": str(video.relative_to(WORKDIR)),
                "postiz_id": payload.get("id"),
                "postiz_url": payload.get("path"),
                "uploaded_at": datetime.now(timezone.utc).isoformat(),
            }
            new_uploads += 1
            save_ledger(ledger)

    print(f"\nDone. {new_uploads} new uploads, {skipped} skipped, {failed} failed.")
    print(f"Ledger: {LEDGER_PATH}")


if __name__ == "__main__":
    main()
