#!/bin/bash
# Bake a trending audio track into a CTA video.
#
# Usage:
#   ./bake_audio.sh <source_video> <cta_video> <output_name>
#
# Example:
#   ./bake_audio.sh inbox/tiktok.mp4 outbox/assets/CTAvideo.mp4 CTAvideo_with_audio_v2.mp4
#
# The audio is trimmed to match the CTA video's duration with a 1s fadeout.
# Both source files keep their originals untouched. Output goes to outbox/assets/.

set -euo pipefail

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <source_video> <cta_video> <output_name>" >&2
    exit 1
fi

SOURCE_VIDEO="$1"
CTA_VIDEO="$2"
OUTPUT_NAME="$3"

ASSETS_DIR="$(cd "$(dirname "$0")/../assets" && pwd)"
CLIPS_DIR="$ASSETS_DIR/source_audio_clips"
mkdir -p "$CLIPS_DIR"

CTA_DURATION="$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$CTA_VIDEO" | cut -d. -f1)"
[ -z "$CTA_DURATION" ] && CTA_DURATION=6
FADE_START=$((CTA_DURATION - 1))

BASE="$(basename "$SOURCE_VIDEO" .mp4)"
FULL_AUDIO="$CLIPS_DIR/${BASE}_full.mp3"
TRIMMED_AUDIO="$CLIPS_DIR/${BASE}_trimmed_${CTA_DURATION}s.mp3"
OUTPUT_PATH="$ASSETS_DIR/$OUTPUT_NAME"

echo "Extracting full audio from $SOURCE_VIDEO..."
ffmpeg -y -loglevel error -i "$SOURCE_VIDEO" -vn -acodec mp3 -b:a 192k "$FULL_AUDIO"

echo "Trimming to ${CTA_DURATION}s with 1s fadeout..."
ffmpeg -y -loglevel error -i "$FULL_AUDIO" -t "$CTA_DURATION" -af "afade=t=out:st=${FADE_START}:d=1" "$TRIMMED_AUDIO"

echo "Overlaying on $CTA_VIDEO..."
ffmpeg -y -loglevel error -i "$CTA_VIDEO" -i "$TRIMMED_AUDIO" -map 0:v -map 1:a -c:v copy -c:a aac -shortest "$OUTPUT_PATH"

echo ""
echo "Done. Output: $OUTPUT_PATH"
ffprobe -v error -show_entries stream=codec_type,codec_name,duration -show_entries format=duration,size -of default=noprint_wrappers=1 "$OUTPUT_PATH"
