#!/usr/bin/env bash
# Take a screenshot of a URL and save as WebP.
# Usage: screenshot-url.sh <url> <output-file.webp>
#
# Dependencies (tries in order):
#   1. Playwright CLI (npx playwright)
#   2. Puppeteer via Node (npx puppeteer)
#   3. Chromium / Google Chrome headless
#
# Viewport: 1280×800, waits for network idle.

set -euo pipefail

URL="${1:?Usage: screenshot-url.sh <url> <output.webp>}"
OUT="${2:?Usage: screenshot-url.sh <url> <output.webp>}"

mkdir -p "$(dirname "$OUT")"

# Derive a PNG temp file (most tools capture PNG; we convert to WebP at end)
TMP_PNG="$(mktemp /tmp/screenshot-XXXXXX.png)"
trap 'rm -f "$TMP_PNG"' EXIT

echo "Screenshotting $URL → $OUT ..."

# ── Method 1: Playwright CLI ─────────────────────────────────────────────────
if command -v npx &>/dev/null && npx --yes playwright --version &>/dev/null 2>&1; then
  npx playwright screenshot \
    --browser chromium \
    --viewport-size "1280,800" \
    --wait-for-timeout 3000 \
    "$URL" "$TMP_PNG"

# ── Method 2: Puppeteer (inline script) ─────────────────────────────────────
elif command -v node &>/dev/null && node -e "require('puppeteer')" &>/dev/null 2>&1; then
  node - "$URL" "$TMP_PNG" <<'JSEOF'
const pup = require('puppeteer');
const [,, url, out] = process.argv;
(async () => {
  const browser = await pup.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 800 });
  await page.goto(url, { waitUntil: 'networkidle2', timeout: 30000 });
  await page.screenshot({ path: out, fullPage: false });
  await browser.close();
})();
JSEOF

# ── Method 3: Chromium headless ─────────────────────────────────────────────
elif command -v chromium &>/dev/null || command -v chromium-browser &>/dev/null || command -v google-chrome &>/dev/null; then
  CHROME="$(command -v chromium chromium-browser google-chrome 2>/dev/null | head -1)"
  "$CHROME" \
    --headless=new \
    --no-sandbox \
    --disable-gpu \
    --window-size=1280,800 \
    --screenshot="$TMP_PNG" \
    "$URL" &>/dev/null

else
  echo "ERROR: No screenshot tool found. Install one of:" >&2
  echo "  npm install -g playwright && npx playwright install chromium" >&2
  echo "  npm install -g puppeteer" >&2
  echo "  sudo apt install chromium" >&2
  exit 1
fi

# ── Convert PNG → WebP ───────────────────────────────────────────────────────
if command -v cwebp &>/dev/null; then
  cwebp -q 80 "$TMP_PNG" -o "$OUT" &>/dev/null
elif command -v convert &>/dev/null; then
  convert "$TMP_PNG" -quality 80 "$OUT"
elif command -v magick &>/dev/null; then
  magick "$TMP_PNG" -quality 80 "$OUT"
else
  # Fall back to PNG if no WebP encoder available
  cp "$TMP_PNG" "${OUT%.webp}.png"
  echo "WARNING: No WebP encoder found; saved as ${OUT%.webp}.png instead." >&2
fi

echo "Saved: $OUT"
