# DMG Mode Theme

A Chrome theme in the DMG Mode pea-green palette (`#0f380f` `#306230` `#8bac0f` `#9bbc0f`). Companion to the [DMG Mode extension](https://github.com/Zapskii/dmg-mode).

| Part | Shade |
|---|---|
| Window frame, background tabs | `#306230` (`#0f380f` when unfocused or incognito) |
| Active tab, toolbar | `#8bac0f` |
| Address bar, New Tab page | `#9bbc0f` |
| Text and icons | `#0f380f` |

## Install (development)

1. `chrome://extensions` → turn on **Developer mode** → **Load unpacked** → pick `theme/`.
2. To go back: `chrome://settings/appearance` → **Reset to default**.

## Build

`./build.sh` zips `theme/` into `dist/dmg-mode-theme-<version>.zip` for the Chrome Web Store.
