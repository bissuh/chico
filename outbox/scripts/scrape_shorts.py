#!/usr/bin/env python3
"""
Scrape top YouTube Shorts from a channel by view count.
Saves source MP4s to outbox/assets/source_hooks/{channel_slug}/.
Writes manifest.json with id, title, views, duration, published_at, url.
Skips downloads that already exist.

Usage:
    ./scrape_shorts.py <channel_url_or_handle> <count>

Examples:
    ./scrape_shorts.py https://www.youtube.com/@AlexHormozi 20
    ./scrape_shorts.py @MyFirstMillionPod 10

Requires YOUTUBE_API_KEY in repo .env. yt-dlp must be on PATH.
"""

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(REPO_ROOT / ".env")

YT_API_KEY = os.environ.get("YOUTUBE_API_KEY")
if not YT_API_KEY:
    sys.exit("YOUTUBE_API_KEY missing from .env")

BASE = "https://www.googleapis.com/youtube/v3"
HOOKS_DIR = REPO_ROOT / "outbox" / "assets" / "source_hooks"


def parse_input(arg: str) -> str:
    """Return a clean @handle or UC... channel id from any of: handle, URL, or ID."""
    arg = arg.strip()
    m = re.search(r"youtube\.com/(@[A-Za-z0-9_.-]+)", arg)
    if m:
        return m.group(1)
    m = re.search(r"youtube\.com/channel/(UC[\w-]+)", arg)
    if m:
        return m.group(1)
    if arg.startswith("@") or arg.startswith("UC"):
        return arg
    return arg


def resolve_channel_id(handle_or_id: str) -> tuple[str, str]:
    """Returns (channel_id, channel_title)."""
    if handle_or_id.startswith("UC"):
        r = requests.get(
            f"{BASE}/channels",
            params={"part": "snippet", "id": handle_or_id, "key": YT_API_KEY},
            timeout=30,
        )
        r.raise_for_status()
        items = r.json().get("items", [])
        if not items:
            sys.exit(f"Channel id {handle_or_id} not found")
        return items[0]["id"], items[0]["snippet"]["title"]

    handle = handle_or_id.lstrip("@")
    r = requests.get(
        f"{BASE}/channels",
        params={"part": "snippet", "forHandle": f"@{handle}", "key": YT_API_KEY},
        timeout=30,
    )
    r.raise_for_status()
    items = r.json().get("items", [])
    if not items:
        sys.exit(f"Handle @{handle} not found")
    return items[0]["id"], items[0]["snippet"]["title"]


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")


def search_shorts(channel_id: str, count: int) -> list[str]:
    """Return up to `count` short video IDs ordered by viewCount.
    YouTube's `videoDuration=short` is <4 minutes — broader than Shorts proper.
    We filter by duration <60s in fetch_video_details to keep only true Shorts."""
    ids: list[str] = []
    page_token = None
    while len(ids) < count * 3:
        params = {
            "part": "id",
            "channelId": channel_id,
            "type": "video",
            "videoDuration": "short",
            "order": "viewCount",
            "maxResults": 50,
            "key": YT_API_KEY,
        }
        if page_token:
            params["pageToken"] = page_token
        r = requests.get(f"{BASE}/search", params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        for item in data.get("items", []):
            vid = item["id"].get("videoId")
            if vid:
                ids.append(vid)
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return ids


def fetch_video_details(video_ids: list[str]) -> list[dict]:
    """Batch-fetch video details. Returns list with id, title, views, duration_sec, published_at."""
    out = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i : i + 50]
        r = requests.get(
            f"{BASE}/videos",
            params={
                "part": "snippet,statistics,contentDetails",
                "id": ",".join(batch),
                "key": YT_API_KEY,
            },
            timeout=30,
        )
        r.raise_for_status()
        for item in r.json().get("items", []):
            duration_sec = parse_iso8601_duration(item["contentDetails"]["duration"])
            out.append(
                {
                    "id": item["id"],
                    "title": item["snippet"]["title"],
                    "views": int(item["statistics"].get("viewCount", 0)),
                    "duration_sec": duration_sec,
                    "published_at": item["snippet"]["publishedAt"],
                    "url": f"https://www.youtube.com/shorts/{item['id']}",
                }
            )
    return out


def parse_iso8601_duration(s: str) -> int:
    m = re.match(r"PT(?:(\d+)M)?(?:(\d+)S)?", s)
    if not m:
        return 0
    minutes = int(m.group(1) or 0)
    seconds = int(m.group(2) or 0)
    return minutes * 60 + seconds


def download_short(video: dict, out_dir: Path) -> Path:
    out = out_dir / f"{video['id']}.mp4"
    if out.exists():
        return out
    cmd = [
        "yt-dlp",
        "-f",
        "mp4/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
        "--merge-output-format",
        "mp4",
        "-o",
        str(out),
        video["url"],
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  ! yt-dlp failed for {video['id']}: {result.stderr.strip().splitlines()[-1]}")
        return None
    return out


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    raw_arg, count_str = sys.argv[1], sys.argv[2]
    count = int(count_str)

    handle_or_id = parse_input(raw_arg)
    channel_id, channel_title = resolve_channel_id(handle_or_id)
    slug = slugify(channel_title)
    out_dir = HOOKS_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Channel: {channel_title} ({channel_id})")
    print(f"Output:  {out_dir}")

    video_ids = search_shorts(channel_id, count)
    print(f"Found {len(video_ids)} candidate shorts (videoDuration=short)")

    details = fetch_video_details(video_ids)
    shorts = [v for v in details if v["duration_sec"] <= 90]
    shorts.sort(key=lambda v: v["views"], reverse=True)
    shorts = shorts[:count]
    print(f"Top {len(shorts)} after duration filter (<=90s) and view sort")

    downloaded = []
    for i, video in enumerate(shorts, 1):
        print(f"[{i}/{len(shorts)}] {video['views']:>10,} views — {video['title'][:70]}")
        path = download_short(video, out_dir)
        if path:
            video["local_path"] = str(path.relative_to(REPO_ROOT))
            downloaded.append(video)

    manifest = {
        "channel_id": channel_id,
        "channel_title": channel_title,
        "channel_slug": slug,
        "scraped_count": len(downloaded),
        "videos": downloaded,
    }
    manifest_path = out_dir / "manifest.json"
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nDone. {len(downloaded)} videos in {out_dir}")
    print(f"Manifest: {manifest_path}")


if __name__ == "__main__":
    main()
