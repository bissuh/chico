#!/usr/bin/env python3
"""
Schedule stitched shorts on YouTube via the Postiz REST API.

Reads:
  - {workdir}/assets/postiz_uploads.json  (uploaded files with their hosted URLs)
  - {workdir}/assets/source_hooks/{slug}/manifest.json  (source video metadata for sort)

Sorts uploaded videos by source-channel view count (desc), takes the top --count.
Generates UTC schedule slots starting --start, every --interval hours.
For each slot, POSTs to Postiz /public/v1/posts to schedule a YouTube short.

Records postiz_post_id + scheduled_at_utc back into postiz_uploads.json so we
never re-schedule the same video.

The post title/description/tags are the SAME on every video (that sameness is
your brand signal). Set them once in .env:
  CTA_POST_TITLE, CTA_POST_DESCRIPTION, CTA_POST_TAGS (comma-separated)

Usage:
  ./schedule_via_postiz.py --start 2026-01-10T01:00:00Z --count 50 --interval 6
  ./schedule_via_postiz.py --start now --count 50 --type draft   # all as drafts
  ./schedule_via_postiz.py --dry-run --count 50                  # preview only

Requires POSTIZ_API_KEY and POSTIZ_YOUTUBE_INTEGRATION_ID in env.
Working directory defaults to the current dir; override with CTA_WORKDIR.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

WORKDIR = Path(os.environ.get("CTA_WORKDIR", Path.cwd())).resolve()
load_dotenv(WORKDIR / ".env")

API_KEY = os.environ.get("POSTIZ_API_KEY")
YT_INTEGRATION_ID = os.environ.get("POSTIZ_YOUTUBE_INTEGRATION_ID")
POSTIZ_BASE = "https://api.postiz.com/public/v1"

LEDGER_PATH = WORKDIR / "assets" / "postiz_uploads.json"
HOOKS_DIR = WORKDIR / "assets" / "source_hooks"

# Customize these in .env. The placeholders below are examples only.
DEFAULT_TITLE = os.environ.get(
    "CTA_POST_TITLE", "Your one-line hook | yourdomain.com"
)
DEFAULT_DESCRIPTION = os.environ.get(
    "CTA_POST_DESCRIPTION",
    "Get the free thing: yourdomain.com\n\nOne sentence about who it's for and why.",
)
_RAW_TAGS = os.environ.get(
    "CTA_POST_TAGS", "Shorts,Entrepreneur,Startup,Side Hustle"
)
DEFAULT_TAGS = [
    {"value": t.strip(), "label": t.strip()}
    for t in _RAW_TAGS.split(",")
    if t.strip()
]


def load_ledger() -> dict:
    with open(LEDGER_PATH) as f:
        return json.load(f)


def save_ledger(ledger: dict) -> None:
    with open(LEDGER_PATH, "w") as f:
        json.dump(ledger, f, indent=2, sort_keys=True)


def load_source_views() -> dict:
    """Return {video_id: {views, title, channel_slug}} from all source manifests."""
    out = {}
    for channel_dir in HOOKS_DIR.iterdir():
        if not channel_dir.is_dir():
            continue
        manifest = channel_dir / "manifest.json"
        if not manifest.exists():
            continue
        with open(manifest) as f:
            data = json.load(f)
        slug = data["channel_slug"]
        for video in data.get("videos", []):
            out[video["id"]] = {
                "views": video.get("views", 0),
                "title": video.get("title", ""),
                "channel_slug": slug,
                "source_url": video.get("url", ""),
            }
    return out


def parse_start(value: str) -> datetime:
    if value == "now":
        return datetime.now(timezone.utc).replace(microsecond=0)
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def schedule_post(
    *,
    iso_date: str,
    video_url: str,
    video_postiz_id: str,
    title: str,
    description: str,
    visibility: str,
    tags: list,
    post_type: str,
) -> tuple[bool, str]:
    """Returns (success, post_id_or_error)."""
    payload = {
        "type": post_type,
        "date": iso_date,
        "shortLink": False,
        "tags": [],
        "posts": [
            {
                "integration": {"id": YT_INTEGRATION_ID},
                "value": [
                    {
                        "content": description,
                        "image": [{"id": video_postiz_id, "path": video_url}],
                    }
                ],
                "settings": {
                    "__type": "youtube",
                    "title": title,
                    "type": visibility,
                    "selfDeclaredMadeForKids": "no",
                    "tags": tags,
                },
            }
        ],
    }
    r = requests.post(
        f"{POSTIZ_BASE}/posts",
        headers={
            "Authorization": API_KEY,
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=30,
    )
    if r.status_code >= 300:
        return False, f"HTTP {r.status_code}: {r.text[:300]}"
    try:
        body = r.json() if r.text else {}
    except Exception:
        body = {}
    if isinstance(body, list):
        body = body[0] if body else {}
    if not isinstance(body, dict):
        body = {}
    post_id = (
        body.get("postId")
        or body.get("id")
        or (body.get("posts", [{}]) or [{}])[0].get("id", "")
        or ""
    )
    return True, post_id or "(no id returned)"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--start", default="now", help="UTC ISO start time, or 'now'")
    parser.add_argument("--count", type=int, default=50, help="Number of videos to schedule")
    parser.add_argument("--interval", type=float, default=6, help="Hours between posts")
    parser.add_argument("--type", default="schedule", choices=["draft", "schedule", "now"])
    parser.add_argument("--visibility", default="public", choices=["public", "private", "unlisted"])
    parser.add_argument("--title", default=DEFAULT_TITLE)
    parser.add_argument("--description", default=DEFAULT_DESCRIPTION)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not API_KEY:
        sys.exit("POSTIZ_API_KEY missing from .env")
    if not YT_INTEGRATION_ID:
        sys.exit("POSTIZ_YOUTUBE_INTEGRATION_ID missing from .env")

    ledger = load_ledger()
    source_meta = load_source_views()

    candidates = []
    for key, entry in ledger.items():
        if entry.get("scheduled_at_utc"):
            continue
        vid = entry["video_id"]
        meta = source_meta.get(vid, {})
        candidates.append(
            {
                "ledger_key": key,
                "video_id": vid,
                "channel_slug": entry["channel_slug"],
                "postiz_id": entry["postiz_id"],
                "postiz_url": entry["postiz_url"],
                "source_views": meta.get("views", 0),
                "source_title": meta.get("title", ""),
            }
        )

    candidates.sort(key=lambda c: c["source_views"], reverse=True)
    selected = candidates[: args.count]
    print(f"Candidates: {len(candidates)} unscheduled, taking top {len(selected)} by source views")

    start = parse_start(args.start)
    interval = timedelta(hours=args.interval)

    print(f"\nSchedule preview (UTC, post type = {args.type}, visibility = {args.visibility}):")
    plan = []
    for i, c in enumerate(selected):
        slot = start + i * interval
        iso = slot.isoformat().replace("+00:00", "Z")
        plan.append((iso, c))
        print(f"  {iso}  {c['channel_slug']:<20s}  {c['source_views']:>10,}  {c['source_title'][:55]}")

    if args.dry_run:
        print("\n--dry-run: no API calls made")
        return

    print(f"\nPosting to Postiz ({len(plan)} calls)...")
    successes = 0
    failures = 0
    for iso, c in plan:
        ok, payload = schedule_post(
            iso_date=iso,
            video_url=c["postiz_url"],
            video_postiz_id=c["postiz_id"],
            title=args.title,
            description=args.description,
            visibility=args.visibility,
            tags=DEFAULT_TAGS,
            post_type=args.type,
        )
        if ok:
            successes += 1
            ledger[c["ledger_key"]]["scheduled_at_utc"] = iso
            ledger[c["ledger_key"]]["postiz_post_id"] = payload
            ledger[c["ledger_key"]]["scheduled_type"] = args.type
            save_ledger(ledger)
            print(f"  ok {iso}  {c['video_id']}  -> {payload}")
        else:
            failures += 1
            print(f"  xx {iso}  {c['video_id']}  {payload}")

    print(f"\nDone. {successes} scheduled, {failures} failed.")


if __name__ == "__main__":
    main()
