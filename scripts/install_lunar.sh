#!/usr/bin/env bash
set -euo pipefail
ROOT="${1:-external/LUNAR}"
if [[ -e "$ROOT" ]]; then
  echo "Destination exists: $ROOT; refusing to overwrite." >&2
  exit 2
fi
mkdir -p "$(dirname "$ROOT")"
git clone https://github.com/CMMRLab/LUNAR.git "$ROOT"
git -C "$ROOT" rev-parse HEAD
echo "Pin this commit SHA in your run manifest for reproducibility."
