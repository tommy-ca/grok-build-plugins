## Why

Grok Build installs plugins one repo at a time. A marketplace index lets operators add one catalog. xAI Official already names `pstack` as the Cursor wrap. First-party install must be `tommy-ca/pstack`. The catalog must not duplicate `skills/`.

## What Changes

- Catalog repo with `.grok-plugin/marketplace.json` pinning `tommy-ca/pstack` by 40-hex sha.
- Default install command is `grok plugin install tommy-ca/pstack --trust`.
- Marketplace add is optional.

## Capabilities

### New Capabilities

- `grok-build-marketplace`: Grok marketplace index for first-party plugins, starting with pstack.

### Modified Capabilities

None.

## Impact

- `/home/tommyk/projects/grok-build-plugins` and `https://github.com/tommy-ca/grok-build-plugins`.
- Plugin payload remains `tommy-ca/pstack`.
