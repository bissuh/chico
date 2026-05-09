#!/bin/bash
#
# Append the TBP CTA to the end of any short, normalized to 1080x1920 9:16.
# Source video is preserved. Output is a copy with the CTA concatenated.
#
# Usage:
#   append_cta.sh <source.mp4> <cta.mp4> <output.mp4>
#
# Example:
#   append_cta.sh "Shorts to Post/clip.mp4" outbox/assets/CTAvideo_v7.mp4 "Shorts to Post/with_cta/clip.mp4"

set -euo pipefail

if [ "$#" -ne 3 ]; then
  echo "usage: $0 <source.mp4> <cta.mp4> <output.mp4>" >&2
  exit 1
fi

SRC="$1"
CTA="$2"
OUT="$3"

if [ ! -f "$SRC" ]; then echo "missing source: $SRC" >&2; exit 1; fi
if [ ! -f "$CTA" ]; then echo "missing cta: $CTA" >&2; exit 1; fi

mkdir -p "$(dirname "$OUT")"

NORM='scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2,setsar=1'

ffmpeg -y -loglevel error \
  -i "$SRC" \
  -i "$CTA" \
  -filter_complex "
    [0:v]${NORM}[v0];
    [0:a]aresample=44100[a0];
    [1:v]${NORM}[v1];
    [1:a]aresample=44100[a1];
    [v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]
  " \
  -map "[v]" -map "[a]" \
  -c:v libx264 -preset veryfast -crf 20 \
  -c:a aac -b:a 192k \
  -movflags +faststart \
  "$OUT"

DUR=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$OUT")
SIZE=$(stat -f%z "$OUT" 2>/dev/null || stat -c%s "$OUT")
echo "  ✓ $(basename "$OUT")  ${DUR}s  $((SIZE/1024))KB"
