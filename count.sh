#!/bin/bash

easy=$(find 1-easy -mindepth 2 -maxdepth 2 -type d | wc -l | tr -d ' ')
medium=$(find 2-medium -mindepth 2 -maxdepth 2 -type d | wc -l | tr -d ' ')
hard=$(find 3-hard -mindepth 2 -maxdepth 2 -type d | wc -l | tr -d ' ')
total=$((easy + medium + hard))

echo "eay:   $easy"
echo "medium: $medium"
echo "hard:   $hard"
echo "TOTAL:  $total"
