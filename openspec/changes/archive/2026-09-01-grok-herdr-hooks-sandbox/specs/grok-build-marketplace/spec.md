## MODIFIED Requirements

### Requirement: Nested marketplace add documents sandbox EROFS

Feature: grok-build-marketplace
Rule: Agent bwrap cannot rewrite config.toml or global hooks

Shipped catalog docs MUST say `grok plugin marketplace add` rewrites `~/.grok/config.toml` and fails with EROFS (os error 30) inside a sandboxed Grok agent session. They MUST tell the operator to run add from a host shell. They MUST keep `grok plugin install tommy-ca/pstack --trust` as the in-session install path.

They MUST also say `~/.grok/hooks/` is bind-mounted read-only under `workspace`, `homelab`, `read-only`, and `strict`. `herdr integration install grok` MUST be documented as a host-shell or `grok --sandbox herdr-install` / `grok --sandbox off` / `grok --sandbox devbox` action. Docs MUST NOT claim that adding `read_write` of `~/.grok/hooks` on `homelab` unbinds that pin.

#### Scenario: Agent nested grok cannot add a marketplace

- **GIVEN** `__GROK_INSIDE_BWRAP=1` and `config.toml` bind-mounted read-only
- **WHEN** shipped docs describe `grok plugin marketplace add`
- **THEN** they name EROFS on `~/.grok/config.toml`
- **AND** they name a host shell as the fix

#### Scenario: herdr grok hooks install is not a homelab whitelist

- **GIVEN** `[sandbox] profile = "homelab"` extends `workspace`
- **WHEN** shipped docs describe `herdr integration install grok`
- **THEN** they name `~/.grok/hooks/` EROFS under that profile
- **AND** they name `devbox`, `herdr-install`, or `off` as the profiles that skip hook write-deny

## ADDED Requirements

### Requirement: Herdr SessionStart tracking does not write hooks

Feature: grok-build-marketplace
Rule: pane.report_agent_session is tmp plus unix socket

Docs MUST state that `herdr-agent-state.sh` on SessionStart writes a temp file under `$TMPDIR` and sends `pane.report_agent_session` to `$HERDR_SOCKET_PATH`. That path is `~/.config/herdr/herdr.sock` on this host. Tracking can succeed on `homelab` when the hook files already exist. `grok --sandbox devbox` is correctly tracked for install/update because that profile does not pin `~/.grok/hooks/` read-only.

#### Scenario: why devbox is herdr-tracked for install

- **GIVEN** `18-sandbox.md` Direct global hook write protection
- **WHEN** the operator uses `grok --sandbox devbox`
- **THEN** that protection is not applied
- **AND** `herdr integration install grok` can write `~/.grok/hooks/herdr.json` and `herdr-agent-state.sh`

#### Scenario: homelab still reports if hooks exist

- **GIVEN** herdr grok hooks are already installed and `HERDR_ENV=1`
- **WHEN** SessionStart runs under `homelab`
- **THEN** the script may report over the unix socket without writing `~/.grok/hooks/`
