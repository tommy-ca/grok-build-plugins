## Why

pstack is installed with `--trust` and still has no skills or spawn types until it is in `[plugins].enabled`. Catalog docs omitted enable. Enable rewrites `config.toml` and hits EROFS in the agent sandbox, same as marketplace add. After enable, grok 1.0.13 registers `pstack:how-explorer`, not `how-explorer`.

## What Changes

- Catalog README and SPEC document enable, EROFS, `grok --sandbox off plugin enable pstack`, and qualified spawn names.
- After marketplace add, install stays `tommy-ca/pstack`, never bare `pstack`.
- Pin bump waits until pstack `feat/pstack-session-apply` is on `main`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: enable, spawn types, host-shell enable.

## Impact

- `tommy-ca/grok-build-plugins` README, SPEC.md, tests, this OpenSpec change.
