#!/usr/bin/env node
// Prints the Firefox manifest: theme/manifest.json overlaid with manifest.firefox.json.
// Top-level keys in the overlay replace the Chrome ones (so "theme" is replaced whole,
// because Firefox uses different colour names); null removes a key.
const fs = require('node:fs');
const path = require('node:path');

const root = path.join(__dirname, '..');
const read = (f) => JSON.parse(fs.readFileSync(path.join(root, f), 'utf8'));

const m = { ...read('theme/manifest.json'), ...read('manifest.firefox.json') };
for (const k of Object.keys(m)) if (m[k] === null) delete m[k];
process.stdout.write(JSON.stringify(m, null, 2) + '\n');
