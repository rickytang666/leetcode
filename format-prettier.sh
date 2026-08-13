#!/usr/bin/env bash

set -euo pipefail

usage() {
  cat <<'EOF'
usage: ./format-prettier.sh [--check] [--all]

Formats tracked repo text with Prettier.

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
  echo "No files matched."
  exit 0
fi

xargs -0 "${prettier_cmd[@]}" "$mode" <"$tmp_file"
