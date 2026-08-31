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

### Enable is required and hits EROFS in the agent sandbox

- **GIVEN** pstack is installed with `--trust` and missing from `[plugins].enabled`
- **WHEN** shipped docs name the next command
- **THEN** the command is `grok plugin enable pstack`
- **AND** they say `inspect` "enabled" is trust
- **AND** they say enable rewrites `config.toml` and fails with EROFS (os error 30) inside the agent sandbox
- **AND** they name a host shell or `grok --sandbox off plugin enable pstack`
- **AND** they say spawn types are `pstack:how-explorer`, not `how-explorer`

### Marketplace add from a sandboxed agent is EROFS

- **GIVEN** a Grok agent session with `__GROK_INSIDE_BWRAP=1` and `config.toml` bind-mounted read-only
- **WHEN** the agent runs `grok plugin marketplace add`
- **THEN** the nested CLI fails with EROFS (os error 30) on `~/.grok/config.toml`
- **AND** docs tell the operator to run add from a host shell
- **AND** `grok plugin install tommy-ca/pstack --trust` remains the in-session path

### Catalog lists grok-native siblings

- **GIVEN** the marketplace index
- **WHEN** `plugins[]` is read
- **THEN** `pstack` is a pinned git url
- **AND** `agent-compatibility` and `cli-for-agent` are local paths `./agent-compatibility` and `./cli-for-agent`
- **AND** there is no `plugins/` directory and no `pstack/` plugin folder
- **AND** `cursor-team-kit` and `make-bot-ui` are not required
- **AND** docs spawn `agent-compatibility:startup-review`, not `startup-review`
