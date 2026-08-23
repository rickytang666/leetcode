#!/usr/bin/env bash

set -euo pipefail

if [ -t 1 ] && [ -z "${NO_COLOR+x}" ] && [ "${TERM:-}" != "dumb" ]; then
  bold=$'\033[1m'
  dim=$'\033[2m'
  green=$'\033[32m'
  yellow=$'\033[33m'
  red=$'\033[31m'
  reset=$'\033[0m'
else
  bold=""
  dim=""
  green=""
  yellow=""
  red=""
  reset=""
fi

easy=$(find 1-easy -mindepth 2 -maxdepth 2 -type d | wc -l | tr -d ' ')
medium=$(find 2-medium -mindepth 2 -maxdepth 2 -type d | wc -l | tr -d ' ')
hard=$(find 3-hard -mindepth 2 -maxdepth 2 -type d | wc -l | tr -d ' ')
total=$((easy + medium + hard))

printf '%sleetcode corpus%s\n' "${bold}" "${reset}"
printf '  %s%-8s%s %5d\n' "${green}" "easy" "${reset}" "${easy}"
printf '  %s%-8s%s %5d\n' "${yellow}" "medium" "${reset}" "${medium}"
printf '  %s%-8s%s %5d\n' "${red}" "hard" "${reset}" "${hard}"
printf '  %s%-8s%s %5d\n' "${dim}" "total" "${reset}" "${total}"
