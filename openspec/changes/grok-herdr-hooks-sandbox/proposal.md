## Why

`grok --sandbox devbox` is herdr-tracked because that profile skips Direct global hook write protection. `homelab` extends `workspace`, so `~/.grok/hooks/` is bind-mounted read-only. `herdr integration install grok` cannot overwrite `herdr.json` or `herdr-agent-state.sh` from a daily-driver agent turn. SessionStart tracking itself does not need those files writable. It writes `/tmp` and a unix socket. Adding `read_write` for `~/.grok/hooks` on a workspace-derived profile cannot rearrange those binds.

## What Changes

- Spec why `devbox` tracks herdr and why `homelab` still runs SessionStart read-only.
- Ship `[profiles.herdr-install]` that extends `devbox` for install/update of the grok integration.
- Ship a host-shell script that runs `herdr integration install grok`.
- Map the fact in pstack `HARNESS.md`. Do not pretend `read_write` unbinds `hooks/`.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: herdr grok SessionStart vs sandbox hook pin.

## Impact

Catalog docs, `.grok/sandbox.toml`, `scripts/install-herdr-grok-hooks.sh`, tests, pstack `HARNESS.md`. Not a fake whitelist on `homelab`.
