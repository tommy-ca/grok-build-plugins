## Context

Herdr grok integration is `herdr integration install grok`. It writes `~/.grok/hooks/herdr.json` and `herdr-agent-state.sh`. The script on SessionStart copies stdin to `$TMPDIR`, then `pane.report_agent_session` on `$HERDR_SOCKET_PATH` (`~/.config/herdr/herdr.sock`). It does not write the hooks directory at report time.

`18-sandbox.md` Direct global hook write protection applies to `workspace`, `read-only`, `strict`, and custom profiles that extend those. `devbox` does not apply it. This host `[sandbox] profile = "homelab"` extends `workspace`. `mountinfo` shows `~/.grok/hooks` `ro`. Nested namespaces cannot rearrange those binds.

## Goals / Non-Goals

**Goals:** Document the root cause. Give a profile and a host script that can install/update herdr grok hooks. Keep daily driver on `homelab`.

**Non-Goals:** Making `homelab` write `~/.grok/hooks`. Switching daily driver to `devbox`. Weakening `config.toml` pins.

## Decisions

### D1. Tracking is socket, not hook writes

SessionStart already reports from `homelab` when the files exist. Unix connect to `herdr.sock` succeeded in this session.

### D2. Install/update needs `devbox` or `off`

Only those skip the hook pin. Profile `herdr-install` extends `devbox`. Operator runs `grok --sandbox herdr-install` or `grok --sandbox off` then `herdr integration install grok`.

### D3. Do not add `read_write` of `~/.grok/hooks` on `homelab`

It would not unbind the pin. A whitelist that still EROFS is a lie.

## Risks / Trade-offs

- [`herdr-install` writes most of `$HOME`] -> only for the install session, not daily `homelab`.
- [Operator forgets host shell] -> script comments the EROFS.

## Migration Plan

1. Spec and docs.
2. `.grok/sandbox.toml` plus install script.
3. HARNESS row.
4. Tests.

## Open Questions

None.
