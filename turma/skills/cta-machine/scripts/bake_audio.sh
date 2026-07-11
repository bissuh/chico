#!/bin/bash
# Bake a trending audio track into your CTA video.
#
# Why: a silent CTA dies in the feed. The pattern is to download a video that
# uses a trending sound, extract its audio, and overlay it onto your CTA.
# YouTube Content ID will detect the music and route any ad revenue to the
# rights holder. Your video stays up. Fine if your model is "drive subscribers
# to a destination," not "earn YouTube ad revenue."
#
# Usage:
#   ./bake_audio.sh <source_video> <cta_video> <output_name>
#
# Example:
#   yt-dlp -f mp4 "https://www.tiktok.com/@user/video/123" -o trending.mp4
#   ./bake_audio.sh trending.mp4 assets/cta.mp4 cta.mp4   # overwrites silent cta with audio version
#
# The audio is trimmed to match the CTA video's duration with a 1s fadeout.
# Both source files keep their originals untouched. Output goes to {workdir}/assets/.
# Working directory defaults to the current dir; override with CTA_WORKDIR.

set -euo pipefail

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <source_video> <cta_video> <output_name>" >&2
    exit 1
fi

SOURCE_VIDEO="$1"
CTA_VIDEO="$2"
OUTPUT_NAME="$3"

WORKDIR="${CTA_WORKDIR:-$PWD}"
ASSETS_DIR="$WORKDIR/assets"
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
