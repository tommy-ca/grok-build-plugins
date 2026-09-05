# grok-build-plugins

## Catalog lists pstack without copying the skill tree

The marketplace lists plugin `pstack` whose source is `https://github.com/tommy-ca/pstack.git` pinned to a 40-hex sha. It does not rsync `skills/`. Cursor wrap and open-pstack are not the Grok default.

### Operator installs owner/repo

- **GIVEN** xAI Official already lists a plugin named `pstack` from `cursor/plugins`
- **WHEN** shipped docs name the install command
- **THEN** the command is `grok plugin install tommy-ca/pstack --trust`
- **AND** they warn that bare `pstack` can resolve to the Cursor wrap

### Local sibling versions are unique tags

- **GIVEN** local plugins `agent-compatibility`, `cli-for-agent`, `tommy-mode`, and `long-horizon-swarm`
- **WHEN** `plugin.json` versions are read
- **THEN** each version is SemVer `MAJOR.MINOR.PATCH-<plugin-name>.N`
- **AND** it does not contain `grokbuild`
- **AND** it is not calendar-only uniqueness
- **AND** no two local versions are equal
- **AND** `scripts/release.sh` tags those versions with `grok --sandbox off plugin tag --push`
- **AND** pstack is not a tag target in this repo

### Pin is recorded

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** provenance is inspected
- **THEN** `plugins[0].source.sha` is 40 lowercase hex
- **AND** after a pstack release the sha is set to `git rev-parse origin/main` of `tommy-ca/pstack`

### Enable is required and hits EROFS in the agent sandbox

- **GIVEN** pstack is installed with `--trust` and missing from `[plugins].enabled`
- **WHEN** shipped docs name the next command
- **THEN** the command is `grok plugin enable pstack`
- **AND** they say `[plugins].enabled` is the enable list
- **AND** they say enable rewrites `config.toml` and fails with EROFS (os error 30) from nested grok even when `__GROK_INSIDE_BWRAP` is unset
- **AND** they name a host shell or `grok --sandbox off plugin enable pstack`
- **AND** they say spawn types are `pstack:how-explorer`, not `how-explorer`
- **AND** they say start a new session after enable

### Marketplace add from a sandboxed agent is EROFS

- **GIVEN** a nested grok that cannot rewrite bind-mounted `config.toml`
- **WHEN** the agent runs `grok plugin marketplace add`
- **THEN** the nested CLI fails with EROFS (os error 30) on `~/.grok/config.toml`
- **AND** docs tell the operator to run add from a host shell
- **AND** `grok plugin install tommy-ca/pstack --trust` remains the in-session path

### Herdr grok hooks

- **GIVEN** `homelab` extends `workspace`
- **WHEN** `herdr integration install grok` runs inside a Grok agent turn
- **THEN** `~/.grok/hooks/` is EROFS
- **AND** docs do not claim `read_write` of that directory unbinds the pin
- **AND** install uses a host shell, `grok --sandbox herdr-install`, `grok --sandbox off`, or `grok --sandbox devbox`
- **AND** SessionStart tracking writes `$TMPDIR` and `$HERDR_SOCKET_PATH`, not the hooks directory
- **AND** `grok --sandbox devbox` is herdr-tracked for install because it skips Direct global hook write protection

### Catalog lists grok-native siblings

- **GIVEN** the marketplace index
- **WHEN** `plugins[]` is read
- **THEN** `pstack` is a pinned git url
- **AND** `agent-compatibility`, `cli-for-agent`, `tommy-mode`, and `long-horizon-swarm` are local paths `./agent-compatibility`, `./cli-for-agent`, `./tommy-mode`, and `./long-horizon-swarm`
- **AND** there is no `plugins/` directory and no `pstack/` plugin folder
- **AND** Cursor sibling dirs in this repo are grok-native ports only, not a nested pstack
- **AND** `cursor-team-kit` and `make-bot-ui` are not required
- **AND** docs spawn `agent-compatibility:startup-review`, not `startup-review`
- **AND** docs say start a new session after enable
- **AND** docs say live roles are `inspect.agents[]` and `provides.agents` is a directory count

### long-horizon-swarm is an optional pstack overlay

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** `plugins[]` is read
- **THEN** `long-horizon-swarm` uses local path `./long-horizon-swarm`
- **AND** pstack remains a pinned git url
- **AND** there is no `pstack/` directory

- **GIVEN** the overlay skill
- **WHEN** poteto-mode is missing
- **THEN** the skill tells the operator to install `tommy-ca/pstack --trust` and enable pstack
- **AND** it does not spawn workers

- **GIVEN** the overlay playbook
- **WHEN** a worker is spawned
- **THEN** the text names `spawn_subagent` and `pstack:`
- **AND** recurse is parent-owned units
- **AND** children do not spawn
- **AND** it does not invoke `scripts/orch/orch.ts`
- **AND** it does not name `chatroom_send`

- **GIVEN** overlay HARNESS or REQUIRES
- **WHEN** durable state is described
- **THEN** HostStore is the Grok board
- **AND** pstack `scripts/orch/orch.ts` is named as Codex compatibility
- **AND** Grok steps do not run `orch init`

- **GIVEN** `long-horizon-swarm/skills/`
- **WHEN** skill directories are listed
- **THEN** they include `field-guide`, `planner-worker-split`, `review-lenses`, `coordination-layer`, `megafile-gate`, `ossify-break`, and `openspec-intent-flow`
- **AND** they do not include `long-horizon-swarm-grok-adapter`

- **GIVEN** `skills/long-horizon-swarm/playbooks/long-horizon-swarm.md`
- **WHEN** the playbook is read
- **THEN** it copies ten numbered steps
- **AND** it names `openspec-intent-flow`
- **AND** it names `field-guide`
- **AND** it names TaskTree or TaskNode
