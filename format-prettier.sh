#!/usr/bin/env bash

set -euo pipefail

if [ -t 1 ] && [ -z "${NO_COLOR+x}" ] && [ "${TERM:-}" != "dumb" ]; then
  bold=$'\033[1m'
  dim=$'\033[2m'
  green=$'\033[32m'
  cyan=$'\033[36m'
  reset=$'\033[0m'
else
  bold=""
  dim=""
  green=""
  cyan=""
  reset=""
fi

usage() {
  cat <<'EOF'
usage: ./format-prettier.sh [--check] [--all]

formats tracked repo text with prettier.

default: markdown only (*.md, *.mdx)
--all:   markdown plus js/ts/json/yaml/css/html/scss
--check: check formatting instead of writing
EOF
}

mode="--write"
scope="markdown"

while [ $# -gt 0 ]; do
  case "$1" in
    --check)
      mode="--check"
      ;;
    --all)
      scope="all"
      ;;
    -h | --help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      exit 2
      ;;
  esac
  shift
done

if command -v prettier >/dev/null 2>&1; then
  prettier_cmd=(prettier)
else
  prettier_cmd=(npx --yes prettier)
fi

tmp_file="$(mktemp)"
trap 'rm -f "$tmp_file"' EXIT

case "$scope" in
  markdown)
    find . \
      \( -path './.git' -o -path './.venv' -o -path './.workspace' \) -prune -o \
      -type f \( -name '*.md' -o -name '*.mdx' \) \
      -print0 >"$tmp_file"
    ;;
  all)
    find . \
      \( -path './.git' -o -path './.venv' -o -path './.workspace' \) -prune -o \
      -type f \( \
        -name '*.md' -o -name '*.mdx' -o \
        -name '*.js' -o -name '*.jsx' -o \
        -name '*.ts' -o -name '*.tsx' -o \
        -name '*.json' -o -name '*.yml' -o -name '*.yaml' -o \
        -name '*.css' -o -name '*.scss' -o -name '*.html' \
      \) \
      -print0 >"$tmp_file"
    ;;
esac

if [ ! -s "$tmp_file" ]; then
  printf '%sno files matched.%s\n' "${dim}" "${reset}"
  exit 0
fi

file_count=$(tr -cd '\0' <"$tmp_file" | wc -c | tr -d ' ')
if [ "$mode" = "--check" ]; then
  action="checking"
else
  action="formatting"
  before_checksums=()
  while IFS= read -r -d '' file; do
    before_checksums+=("$(cksum <"$file")")
  done <"$tmp_file"
fi

printf '%s%s%s %s%d%s files with prettier\n\n' \
  "${bold}" "${action}" "${reset}" "${cyan}" "${file_count}" "${reset}"
xargs -0 "${prettier_cmd[@]}" "$mode" <"$tmp_file"

if [ "$mode" = "--check" ]; then
  printf '\n%sdone: formatting check passed (no files changed)%s\n' "${green}${bold}" "${reset}"
else
  changed_count=0
  index=0
  while IFS= read -r -d '' file; do
    if [ "${before_checksums[$index]}" != "$(cksum <"$file")" ]; then
      changed_count=$((changed_count + 1))
    fi
    index=$((index + 1))
  done <"$tmp_file"
  file_label="files"
  if [ "$changed_count" -eq 1 ]; then
    file_label="file"
  fi
  printf '\n%sdone: %d %s changed%s\n' "${green}${bold}" "${changed_count}" "${file_label}" "${reset}"
fi
