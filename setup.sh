set -euo pipefail
shopt -s nullglob

node generate.mjs
npx -y --package markdown-to-html-cli markdown-to-html --source README.md --output index.html
node enhance-index.mjs

if [[ ! -f 2025-06-pycon-sg/llm-cli.html || 2025-06-pycon-sg/llm-cli.md -nt 2025-06-pycon-sg/llm-cli.html ]]
then
  (
    cd 2025-06-pycon-sg
    npx -y --package markdown-to-html-cli markdown-to-html \
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
    (cd "$d" && npx -y @marp-team/marp-cli@latest --theme-set ../marpessa.css --html README.md -o index.html)
  fi
done
