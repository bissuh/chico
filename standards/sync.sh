#!/usr/bin/env bash
# standards/sync.sh: keep the local standards honest against their upstream sources.
#
#   ./standards/sync.sh              check every standard, write nothing
#   ./standards/sync.sh --diff NAME  show the full diff against the source
#   ./standards/sync.sh --pull NAME  overwrite the local copy from its source
#   ./standards/sync.sh --pull-all   overwrite every unforked copy
#
# One direction only, on purpose. A two-way sync with no conflict resolution
# is how you silently lose an edit.
#
# A standard can be a COPY or a FORK. A copy tracks its source exactly, and any
# difference is drift to be pulled. A fork carries our own additions on top of
# the source, so a difference is expected and --pull would destroy our work.
# Mark a fork with a third tab-separated column in .sources reading "fork".
# For a fork, --diff is the tool: read what moved upstream and merge it by hand.

set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REG="$DIR/.sources"
[ -f "$REG" ] || {
  echo "no registry at $REG"
  echo "copy .sources.example to .sources and point each standard at its source."
  exit 1
}

mode="${1:-check}"; target="${2:-}"; force="${3:-}"
drift=0; missing=0; checked=0; forked=0

while IFS=$'\t' read -r name src kind; do
  case "$name" in ''|'#'*) continue;; esac
  [ -n "$target" ] && [ "$name" != "$target" ] && continue
  checked=$((checked + 1))
  local_file="$DIR/$name"
  kind="${kind:-copy}"

  if [ ! -f "$src" ]; then
    echo "MISSING SOURCE  $name"
    echo "                $src"
    missing=$((missing + 1)); continue
  fi

  if diff -q "$local_file" "$src" >/dev/null 2>&1; then
    echo "in sync         $name"
    continue
  fi

  added=$(diff "$local_file" "$src" | grep -c '^>' || true)
  removed=$(diff "$local_file" "$src" | grep -c '^<' || true)

  if [ "$kind" = "fork" ]; then
    forked=$((forked + 1))
    echo "FORKED          $name  (upstream has +$added lines we don't; we have +$removed it doesn't)"
    case "$mode" in
      --diff) diff -u "$local_file" "$src" || true ;;
      --pull|--pull-all)
        if [ "$force" = "--force" ] && [ "$mode" = "--pull" ]; then
          cp "$src" "$local_file"
          echo "                FORCED. local additions discarded."
        else
          echo "                refused. this is a fork; --pull would discard our additions."
          echo "                use --diff to see what moved upstream and merge by hand,"
          echo "                or --pull $name --force to deliberately throw ours away."
        fi ;;
    esac
    continue
  fi

  drift=$((drift + 1))
  echo "DRIFT           $name  (+$added / -$removed lines upstream)"
  case "$mode" in
    --diff) diff -u "$local_file" "$src" || true ;;
    --pull|--pull-all)
      cp "$src" "$local_file"
      echo "                pulled. local copy now matches source." ;;
  esac
done < "$REG"

[ "$checked" -eq 0 ] && { echo "no standard matched '${target}'"; exit 1; }
echo
echo "$checked checked, $drift drifted, $forked forked, $missing missing."
[ "$drift" -gt 0 ] && [ "$mode" = "check" ] && \
  echo "run: ./standards/sync.sh --diff <name>   to see what changed"
[ "$forked" -gt 0 ] && [ "$mode" = "check" ] && \
  echo "forks carry our own additions. --diff to review upstream, never --pull blindly."
exit 0
