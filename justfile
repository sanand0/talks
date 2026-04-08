# Do NOT lint - it messes up AI sub-list indentations, e.g. ordered list inside unordered list
# lint:
#   dprint fmt -c https://raw.githubusercontent.com/sanand0/scripts/refs/heads/live/dprint.jsonc **/*.md
build:
  bash setup.sh
