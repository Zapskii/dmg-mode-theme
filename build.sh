#!/usr/bin/env bash
# Zips theme/ into dist/ for the Chrome Web Store.
set -euo pipefail
cd "$(dirname "$0")"
version=$(node -p 'require("./theme/manifest.json").version')
mkdir -p dist && rm -f "dist/dmg-mode-theme-$version.zip"
(cd theme && zip -r -X -q "../dist/dmg-mode-theme-$version.zip" . -x '*.DS_Store')
echo "Built dist/dmg-mode-theme-$version.zip"
