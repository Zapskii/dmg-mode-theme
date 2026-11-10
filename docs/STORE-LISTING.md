# Chrome Web Store listing copy

Paste-ready text for the developer console. Assets live in `store/`:
`screenshot-1280x800.png` and `promo-tile-440x280.png`; the 128px icon is
`theme/assets/icon-128.png`. Upload `dist/dmg-mode-theme-<version>.zip` from `./build.sh`.

> Naming the Game Boy is fine: the DMG Mode extension's listing says "look like
> it is running on a Game Boy" and passed review. Keep it descriptive (no
> Nintendo logos, no claim of affiliation).

## Basics

- **Name:** DMG Mode Theme
- **Summary (132 chars max):** Chrome in the original Game Boy's four shades of pea green. Companion theme to the DMG Mode extension.
- **Category:** Themes
- **Language:** English (United Kingdom)
- **Pricing:** Free

## Description

```
DMG Mode Theme is a free, open-source Chrome theme that dresses your browser in
the four-shade green of the original Game Boy (DMG) LCD.

• Window frame and background tabs in dark green, deepening when the window
  is unfocused or in incognito
• Active tab and toolbar in pea green, with a pale green address bar
• A pixel-art Game Boy on the New Tab page, drawn in the same four shades

Pair it with the DMG Mode extension to turn the pages themselves four-shade too.

Colours: #0F380F, #306230, #8BAC0F, #9BBC0F.

New Tab artwork is based on "Nintendo Game Boy 1989 - High Poly Model" by
lion.gelders (sketchfab.com/3d-models/nintendo-game-boy-1989-high-poly-model-300c418fb222409abe354926eaa208b2),
licensed under CC BY 4.0 (creativecommons.org/licenses/by/4.0). It was
rendered, pixelated and reduced to the four-shade palette.

Not affiliated with or endorsed by Nintendo. Game Boy is a trademark of Nintendo.
```

## Single purpose

```
A browser theme that colours Chrome's frame, tabs, toolbar and New Tab page in a
four-shade green palette.
```

## Permission justifications

None: a theme declares no permissions and runs no code.

## Privacy practices tab

- **Does the item collect user data?** No.
- **Remote code:** No. A theme contains only a manifest and images.
- **Data use certification:** none of the listed data types are collected, sold or transferred.

## Firefox (addons.mozilla.org)

Upload `dist/dmg-mode-theme-firefox-<version>.zip` as a **theme**. The add-on ID is
`dmg-mode-theme@zapski`; it can't change after the first upload. Use the same name and
summary as above (with "Chrome" read as "Firefox").

- **Licence (AMO picker):** Creative Commons Attribution 4.0. This matches the model the
  artwork is adapted from (CC BY 4.0, confirmed on its Sketchfab page: no NonCommercial,
  NoDerivs or ShareAlike terms, so any licence would be allowed, but CC BY keeps it simple).
- **Screenshot:** `store/screenshot-firefox-1280x800.png`, taken in Firefox.
- A theme has no code, so there's no source upload and nothing to justify to the reviewer.

### Description

Firefox has no separate private-window frame colour and can't show a New Tab image,
so this differs from the Chrome copy:

```
DMG Mode Theme is a free, open-source Firefox theme that dresses your browser in
the four-shade green of the original Game Boy (DMG) LCD.

• Window frame and background tabs in dark green, deepening when the window
  is unfocused
• Active tab and toolbar in pea green, with a pale green address bar
• Menus, sidebar and address bar dropdown in the same greens
• A pixel-art Game Boy in the corner of the tab strip, drawn in the same
  four shades, and a dark green New Tab page

Pair it with the DMG Mode extension to turn the pages themselves four-shade too.

The Game Boy artwork is based on "Nintendo Game Boy 1989 - High Poly Model" by
lion.gelders (sketchfab.com/3d-models/nintendo-game-boy-1989-high-poly-model-300c418fb222409abe354926eaa208b2),
licensed under CC BY 4.0 (creativecommons.org/licenses/by/4.0). It was
rendered, pixelated and reduced to the four-shade palette.

Not affiliated with or endorsed by Nintendo. Game Boy is a trademark of Nintendo.
```

## Pre-submission checklist

- [ ] `theme/manifest.json` version bumped if re-uploading
- [ ] `./build.sh`, then load `theme/` unpacked once and check the New Tab page
- [ ] Add a licence to the repo (no `LICENSE` file yet), or drop "open-source" from both descriptions
- [ ] Upload the zip, screenshot and promo tile; paste the text above
- [ ] `npx addons-linter dist/dmg-mode-theme-firefox-<version>.zip` is clean before the AMO upload
