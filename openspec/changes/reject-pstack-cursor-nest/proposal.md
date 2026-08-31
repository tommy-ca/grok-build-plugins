## Why

Cursor `plugins` is a marketplace of sibling folders. This catalog already uses that shape for grok-native ports. pstack is a remote pin because grok installs `tommy-ca/pstack` as a repo-root plugin and xAI Official already publishes bare `pstack`. A later agent could "follow Cursor" by adding `pstack/` here. That would dump a 400-file multi-host tree into the grok index, share the catalog tag namespace, and break `grok plugin install tommy-ca/pstack --trust`.

## What Changes

- Specs say matching Cursor means local siblings for grok-native ports only.
- pstack MUST stay url+sha. `pstack/` at catalog root is forbidden. `plugins/pstack` stays forbidden.
- Documented install stays `tommy-ca/pstack --trust`. `owner/repo#subdir` is not the pstack default.
- Tests already ban the folder. Lock the docs. No retag. No version bump. Do not extract siblings in this change.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: pstack is not a Cursor-style sibling folder in this catalog.

## Impact

Live marketplace spec, ADR 0006, README, SPEC, `tests/test_marketplace.py`. Not tommy-ca/pstack's tree. Not existing git tags.
