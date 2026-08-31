## 1. Specs

- [x] 1.1 Name why `devbox` skips hook write-deny and herdr install can write `~/.grok/hooks`.
- [x] 1.2 Name SessionStart tracking uses `$TMPDIR` and `$HERDR_SOCKET_PATH`, not hook writes.
- [x] 1.3 Forbid documenting `read_write` of `~/.grok/hooks` on `homelab` as a working whitelist.
- [x] 1.4 `openspec validate grok-herdr-hooks-sandbox --type change --strict`.

## 2. Apply

- [x] 2.1 `.grok/sandbox.toml` `[profiles.herdr-install] extends = "devbox"`.
- [x] 2.2 `scripts/install-herdr-grok-hooks.sh` for a host shell.
- [x] 2.3 README, SPEC.md, pstack HARNESS.md.
- [x] 2.4 Tests drive those files.

## 3. Delivery

- [x] 3.1 Do not mix Pi OpenSpec commits.
- [x] 3.2 Do not edit `~/.grok/sandbox.toml` from a sandboxed agent (EROFS).
