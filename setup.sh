set -euo pipefail
shopt -s nullglob

# Dependencies are installed once with `npm ci` (locally and in CI).
BIN="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/node_modules/.bin"
if [[ ! -x "$BIN/markdown-to-html" || ! -x "$BIN/marp" ]]; then
  echo "Missing build tools: run npm ci first" >&2
  exit 1
fi

node generate.mjs
"$BIN/markdown-to-html" --source README.md --output index.html
node enhance-index.mjs

if [[ ! -f 2025-06-pycon-sg/llm-cli.html || 2025-06-pycon-sg/llm-cli.md -nt 2025-06-pycon-sg/llm-cli.html ]]
then
  (
    cd 2025-06-pycon-sg
    "$BIN/markdown-to-html" \
      --source llm-cli.md \
      --output llm-cli.html \
      --title 'Cool LLM CLI Python uses'
  )
fi

wget -q --no-clobber https://cdn.jsdelivr.net/gh/sanand0/marpessa/marpessa.css

for d in */
do
  readme="$d/README.md"
  index="$d/index.html"
  [[ -f "$readme" ]] || continue
  grep --quiet "^marp:\s*true" "$readme" || continue
  if [[ ! -f "$index" || "$readme" -nt "$index" ]]
  then
    (cd "$d" && "$BIN/marp" --theme-set ../marpessa.css --html README.md -o index.html)
  fi
done
