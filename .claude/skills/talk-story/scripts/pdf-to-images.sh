#!/usr/bin/env bash
# Convert a PDF slide deck to compressed AVIF (or WebP fallback) images.
# Usage: pdf-to-images.sh <pdf-file> <output-dir>
#
# Output: <output-dir>/slide-01.avif, slide-02.avif, ...
# Dependencies (in order of preference):
#   - pdftoppm (poppler-utils) + avifenc (libavif-apps)
#   - pdftoppm (poppler-utils) + ImageMagick convert
#   - ghostscript + ImageMagick convert

set -euo pipefail

PDF="${1:?Usage: pdf-to-images.sh <pdf-file> <output-dir>}"
OUTDIR="${2:?Usage: pdf-to-images.sh <pdf-file> <output-dir>}"

if [ ! -f "$PDF" ]; then
  echo "ERROR: PDF not found: $PDF" >&2
  exit 1
fi

mkdir -p "$OUTDIR"

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

echo "Converting $PDF to images in $OUTDIR ..."

# ── Extract pages as PPM ──────────────────────────────────────────────────────
if command -v pdftoppm &>/dev/null; then
  # 150 DPI is a good balance: readable at 1280px wide, small file size
  pdftoppm -r 150 -png "$PDF" "$TMPDIR/slide"
  EXT="png"
elif command -v gs &>/dev/null; then
  gs -dBATCH -dNOPAUSE -sDEVICE=png16m -r150 \
     -sOutputFile="$TMPDIR/slide-%03d.png" "$PDF" &>/dev/null
  EXT="png"
else
  echo "ERROR: Install poppler-utils (pdftoppm) or ghostscript to convert PDFs." >&2
  echo "  Ubuntu/Debian: sudo apt install poppler-utils" >&2
  echo "  macOS:         brew install poppler" >&2
  exit 1
fi

# ── Pick resize tool ─────────────────────────────────────────────────────────
if command -v magick &>/dev/null; then
  RESIZE_CMD="magick"
elif command -v convert &>/dev/null; then
  RESIZE_CMD="convert"
else
  echo "ERROR: Install ImageMagick to resize images." >&2
  echo "  Ubuntu/Debian: sudo apt install imagemagick" >&2
  echo "  macOS:         brew install imagemagick" >&2
  exit 1
fi

# ── Encode to AVIF or WebP ───────────────────────────────────────────────────
COUNT=0
for SRC in "$TMPDIR"/slide-*."$EXT"; do
  [ -f "$SRC" ] || continue
  COUNT=$((COUNT + 1))
  N="$(printf '%02d' "$COUNT")"
  RESIZED="$TMPDIR/resized-$N.png"
  DEST_AVIF="$OUTDIR/slide-$N.avif"
  DEST_WEBP="$OUTDIR/slide-$N.webp"

  # Resize to max 1280px wide, preserving aspect ratio
  "$RESIZE_CMD" "$SRC" -resize '1280x>' "$RESIZED"

  if command -v avifenc &>/dev/null; then
    avifenc --quality 55 --speed 6 "$RESIZED" "$DEST_AVIF" &>/dev/null
    echo "  slide-$N.avif"
  else
    # ImageMagick WebP fallback
    "$RESIZE_CMD" "$RESIZED" -quality 82 "$DEST_WEBP"
    echo "  slide-$N.webp"
  fi
done

echo "Done: $COUNT slide images written to $OUTDIR"
