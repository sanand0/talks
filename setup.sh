shopt -s nullglob

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
