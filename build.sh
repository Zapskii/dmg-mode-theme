#!/usr/bin/env bash
# Zips theme/ into dist/ for the Chrome Web Store, and again with the Firefox
# manifest (theme/manifest.json overlaid with manifest.firefox.json) for AMO.
set -euo pipefail
cd "$(dirname "$0")"
version=$(node -p 'require("./theme/manifest.json").version')
out="dist/dmg-mode-theme-$version.zip"
ffout="dist/dmg-mode-theme-firefox-$version.zip"
mkdir -p dist && rm -f "$out" "$ffout"

# Chrome: everything except the Firefox-only header image.
(cd theme && zip -r -X -q "../$out" . -x '*.DS_Store' -x 'Cached Theme.pak' -x 'images/frame-corner.png')
echo "Built $out"

# Firefox: merged manifest; Firefox themes can't show a New Tab image, so leave it out.
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT
cp -R theme/. "$tmp"
rm -f "$tmp/Cached Theme.pak" "$tmp/images/ntp-background.png"
node tools/firefox-manifest.js > "$tmp/manifest.json"
(cd "$tmp" && zip -r -X -q "$OLDPWD/$ffout" . -x '*.DS_Store')
echo "Built $ffout"
