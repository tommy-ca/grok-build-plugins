# grok-build-plugins

## Catalog lists pstack without copying the skill tree

The marketplace lists plugin `pstack` whose source is `https://github.com/tommy-ca/pstack.git` pinned to a 40-hex sha. It does not rsync `skills/`. Cursor wrap and open-pstack are not the Grok default.

### Operator installs owner/repo

- **GIVEN** xAI Official already lists a plugin named `pstack` from `cursor/plugins`
- **WHEN** shipped docs name the install command
- **THEN** the command is `grok plugin install tommy-ca/pstack --trust`
- **AND** they warn that bare `pstack` can resolve to the Cursor wrap

### Pin is recorded

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** provenance is inspected
- **THEN** `plugins[0].source.sha` is 40 lowercase hex
- **AND** after a pstack release the sha is set to `git rev-parse origin/main` of `tommy-ca/pstack`

### Marketplace add from a sandboxed agent is EROFS

- **GIVEN** a Grok agent session with `__GROK_INSIDE_BWRAP=1` and `config.toml` bind-mounted read-only
- **WHEN** the agent runs `grok plugin marketplace add`
- **THEN** the nested CLI fails with EROFS (os error 30) on `~/.grok/config.toml`
- **AND** docs tell the operator to run add from a host shell
- **AND** `grok plugin install tommy-ca/pstack --trust` remains the in-session path

### v1 is pstack only

- **GIVEN** the v1 index
- **WHEN** `plugins[]` is read
- **THEN** the only name is `pstack`
- **AND** `cursor-team-kit` and `make-bot-ui` are not required
