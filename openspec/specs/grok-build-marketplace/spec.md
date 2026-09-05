# grok-build-marketplace Specification

## Purpose
Catalog lists pstack as a remote pin and grok-native siblings as local folders. It does not vendor cursor/plugins or nest pstack.

## Requirements

### Requirement: Catalog lists pstack without copying the skill tree

Feature: grok-build-marketplace
Rule: tommy-ca/pstack is the plugin source of truth

The marketplace MUST list a plugin named `pstack` whose source is a git URL of `https://github.com/tommy-ca/pstack.git` pinned to a full 40-hex sha. It MUST NOT rsync `skills/` into a second copy. It MUST NOT nest pstack as `plugins/pstack` or as a `pstack/` sibling folder in this repo.

#### Scenario: Pin is recorded

- **GIVEN** a published marketplace index
- **WHEN** provenance is inspected
- **THEN** the pstack entry includes a 40-character lowercase hex git sha

### Requirement: Documented install is owner/repo

Feature: grok-build-marketplace
Rule: Bare pstack is not the default while xAI Official lists the Cursor wrap

Shipped docs MUST use `grok plugin install tommy-ca/pstack --trust`. They MUST warn that xAI Official already names `pstack` from `cursor/plugins`.

#### Scenario: Bare pstack name is not the documented default

- **GIVEN** xAI Official lists a plugin named `pstack` sourced from `cursor/plugins`
- **WHEN** shipped catalog docs name the install command
- **THEN** they use owner/repo `tommy-ca/pstack`
- **AND** they warn that bare `pstack` can resolve to the Cursor wrap

### Requirement: Nested marketplace add documents sandbox EROFS

Feature: grok-build-marketplace
Rule: Agent bwrap cannot rewrite config.toml

Shipped catalog docs MUST say `grok plugin marketplace add` rewrites `~/.grok/config.toml` and fails with EROFS (os error 30) inside a sandboxed Grok agent session. They MUST tell the operator to run add from a host shell. They MUST keep `grok plugin install tommy-ca/pstack --trust` as the in-session install path. They MUST say `~/.grok/hooks/` is read-only under `workspace` and `homelab`. They MUST NOT claim `read_write` of that directory unbinds the pin.

#### Scenario: Agent nested grok cannot add a marketplace

- **GIVEN** `__GROK_INSIDE_BWRAP=1` and `config.toml` bind-mounted read-only
- **WHEN** shipped docs describe `grok plugin marketplace add`
- **THEN** they name EROFS on `~/.grok/config.toml`
- **AND** they name a host shell as the fix

### Requirement: Herdr SessionStart tracking does not write hooks

Feature: grok-build-marketplace
Rule: pane.report_agent_session is tmp plus unix socket

Docs MUST state that `herdr-agent-state.sh` writes a temp file under `$TMPDIR` and reports to `$HERDR_SOCKET_PATH`. `grok --sandbox devbox` is herdr-tracked for install because that profile skips Direct global hook write protection. `herdr integration install grok` MUST be a host shell, `grok --sandbox herdr-install`, `grok --sandbox off`, or `grok --sandbox devbox`.

#### Scenario: why devbox is herdr-tracked for install

- **GIVEN** `18-sandbox.md` Direct global hook write protection
- **WHEN** the operator uses `grok --sandbox devbox`
- **THEN** that protection is not applied
- **AND** `herdr integration install grok` can write `~/.grok/hooks/herdr.json`

#### Scenario: homelab still reports if hooks exist

- **GIVEN** herdr grok hooks are already installed and `HERDR_ENV=1`
- **WHEN** SessionStart runs under `homelab`
- **THEN** the script may report over the unix socket without writing `~/.grok/hooks/`

### Requirement: Catalog lists grok-native sibling plugins

Feature: grok-build-marketplace
Rule: Cursor sibling layout without vendoring cursor/plugins

The marketplace MUST list `agent-compatibility`, `cli-for-agent`, `tommy-mode`, and `long-horizon-swarm` as local sources (`./agent-compatibility`, `./cli-for-agent`, `./tommy-mode`, `./long-horizon-swarm`). `tommy-mode` MUST NOT live in the pstack plugin tree. `long-horizon-swarm` MUST NOT live in the pstack plugin tree. Those folders MUST contain a grok `plugin.json` with `skills` (and `agents` when the plugin has roles). They MUST NOT declare `hooks`, `commands`, or MCP. `cursor-team-kit`, canvases, `cursor-sdk`, and `orchestrate` MUST NOT be required.

#### Scenario: siblings are local, pstack is remote

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** `plugins[]` is read
- **THEN** `pstack` uses a pinned git url
- **AND** `agent-compatibility`, `cli-for-agent`, `tommy-mode`, and `long-horizon-swarm` use local paths
- **AND** there is no `plugins/` directory and no `pstack/` plugin folder

### Requirement: Documented install also enables pstack

Feature: grok-build-marketplace
Rule: Trust is not [plugins].enabled

Shipped catalog docs MUST tell the operator to run `grok plugin enable pstack` after `grok plugin install tommy-ca/pstack --trust`. They MUST say `inspect` listing the plugin as enabled is trust. They MUST say enable rewrites `~/.grok/config.toml` and fails with EROFS (os error 30) inside a sandboxed agent, and that the fix is a host shell or `grok --sandbox off plugin enable pstack`.

#### Scenario: Enable is documented next to install

- **GIVEN** shipped catalog README and SPEC
- **WHEN** the operator follows install
- **THEN** they see `grok plugin enable pstack`
- **AND** they see EROFS and `--sandbox off` as the sandbox escape
- **AND** they do not treat inspect "enabled" as the enable list

### Requirement: Spawn types are plugin-qualified

Feature: grok-build-marketplace
Rule: grok 1.0.13 names pstack:how-explorer

Shipped catalog docs MUST say pstack playbooks spawn `pstack:<role-key>` (`pstack:how-explorer`). They MUST say agent-compatibility children are `agent-compatibility:<role>` (`agent-compatibility:startup-review`). They MUST say bare stems are unknown even after enable.

#### Scenario: Docs name the live spawn type

- **GIVEN** pstack is enabled
- **WHEN** catalog docs describe subagents
- **THEN** they use `pstack:how-explorer`
- **AND** they do not claim the bare stem is a live type

#### Scenario: sibling docs name qualified review roles

- **GIVEN** shipped catalog README
- **WHEN** an operator enables agent-compatibility
- **THEN** docs name `agent-compatibility:startup-review`
- **AND** they say not to spawn `startup-review`

### Requirement: Operator docs match live inspect and enable

Feature: grok-build-marketplace
Rule: grok 1.0.13 session snapshot and config.toml EROFS

Shipped README and sibling plugin READMEs MUST tell the operator to start a new session after enable. They MUST say live spawn types are in `inspect.agents[]`, and that `provides.agents` is the agents directory count. They MUST say nested `grok plugin enable` and `marketplace add` rewrite `~/.grok/config.toml` and fail with EROFS even when `__GROK_INSIDE_BWRAP` is unset. They MUST name `grok plugin list --json --available` for browsing catalog names.

#### Scenario: new session after enable

- **GIVEN** shipped README and sibling READMEs
- **WHEN** an operator enables a sibling
- **THEN** the pages say to start a new session

#### Scenario: inspect agents vs provides

- **GIVEN** shipped README
- **WHEN** an operator reads how to prove enable
- **THEN** the page names `inspect.agents`
- **AND** it says `provides.agents` is a directory count

### Requirement: Marketplace add still installs owner/repo

Feature: grok-build-marketplace
Rule: Bare pstack stays ambiguous after add

After `grok plugin marketplace add tommy-ca/grok-build-plugins`, shipped docs MUST still install `tommy-ca/pstack`, never bare `pstack`.

#### Scenario: Add does not change the install command

- **GIVEN** the catalog is added
- **WHEN** docs name install
- **THEN** the command is still `grok plugin install tommy-ca/pstack --trust`

### Requirement: Local sibling versions are unique in one git tag namespace

Feature: grok-build-marketplace
Rule: TagName is v plus plugin.json version
Rule: pstack is not tagged from this repo

Each local sibling `plugin.json` version MUST match `MAJOR.MINOR.PATCH-<plugin-name>.N`. Those versions MUST be unique across local siblings. The matching marketplace `plugins[].version` MUST equal that `plugin.json` version. The catalog root MUST NOT have `plugin.json`. `scripts/release.sh` MUST call `grok --sandbox off plugin tag --push` on local sibling folders only. It MUST NOT pass `--force`. If a local tag exists and origin does not, it MUST `git push origin` that ref. After the tag is on origin it MUST converge to a GitHub Release with `gh release view` or `gh release create --verify-tag --latest=false`. Nested grok MUST NOT be the tagger. `.github/workflows/release.yml` MUST run on `v*` and MUST do the same Release step. That workflow MUST NOT invoke `grok plugin tag`. It MUST NOT declare `workflow_dispatch`. pstack MUST remain a remote url plus sha and MUST NOT be a `release.sh` target.

#### Scenario: sibling versions cannot collide

- **GIVEN** local plugins `agent-compatibility`, `cli-for-agent`, `tommy-mode`, and `long-horizon-swarm`
- **WHEN** `plugin.json` versions are read
- **THEN** each version contains that plugin name
- **AND** no two local versions are equal

#### Scenario: catalog root is not tagged

- **GIVEN** the catalog checkout
- **WHEN** `grok plugin tag .` runs
- **THEN** it fails because `plugin.json` is missing

#### Scenario: host-shell script tags one local sibling

- **GIVEN** unique versions on origin/main
- **AND** `release.yml` already exists on the default branch
- **WHEN** an operator runs `scripts/release.sh agent-compatibility` from a host shell
- **THEN** the script calls `grok --sandbox off plugin tag --push` on `./agent-compatibility`
- **AND** it does not pass `--force`
- **AND** it does not tag pstack

#### Scenario: dual-writer GitHub Release

- **GIVEN** origin has tag `v1.0.0-agent-compatibility.0`
- **WHEN** `scripts/release.sh` or `release.yml` runs
- **THEN** a GitHub Release for that tag exists
- **AND** neither writer uses `--force`
- **AND** create uses `--latest=false`

#### Scenario: local tag exists and origin does not

- **GIVEN** `refs/tags/v{version}` exists locally
- **AND** origin does not have that tag
- **WHEN** `grok --sandbox off plugin tag --push` fails
- **THEN** the script runs `git push origin` for that tag

### Requirement: Sibling versions are SemVer identity, not calendar uniqueness

Feature: grok-build-marketplace
Rule: uniqueness is plugin name in one git tag namespace

Local sibling versions MUST remain `MAJOR.MINOR.PATCH-<plugin-name>.N` (SemVer 2.0 prerelease used as namespace). They MUST NOT be calendar-only (`YYYY.MM.DD`, `YYYY.MM.MICRO`) and MUST NOT use a date as the uniqueness key. Two siblings shipping the same day MUST still have distinct versions. Ship day belongs in GitHub Release notes. Existing tags MUST NOT be moved.

#### Scenario: date is not uniqueness

- **GIVEN** two local siblings
- **WHEN** both would ship on the same calendar day
- **THEN** their `plugin.json` versions still differ by plugin name
- **AND** neither version is a date-only CalVer string

### Requirement: Local sibling identity is not grokbuild adapter identity

Feature: grok-build-marketplace
Rule: many local plugins, one git tag namespace
Rule: do not copy pstack grokbuild token onto locals

Local sibling versions MUST remain `MAJOR.MINOR.PATCH-<plugin-name>.N`. They MUST NOT use pstack's adapter grammar `MAJOR.MINOR.PATCH-grokbuild.N`. Shared `-grokbuild.0` already collided (`v1.0.0-grokbuild.0`). The marketplace pstack row MAY copy pstack's live version string for display. That row is url+sha and MUST NOT be a catalog tag. Existing tags MUST NOT be moved.

#### Scenario: local versions exclude grokbuild

- **GIVEN** local plugins `agent-compatibility`, `cli-for-agent`, `tommy-mode`, and `long-horizon-swarm`
- **WHEN** `plugin.json` versions are read
- **THEN** none contain `grokbuild`
- **AND** each contains that plugin name

#### Scenario: marketplace pstack version is display-only

- **GIVEN** the pstack marketplace row
- **WHEN** source is url+sha
- **THEN** `plugins[].version` may match pstack's grokbuild grammar
- **AND** `scripts/release.sh` does not tag pstack from this repo

#### Scenario: pstack grammar is not copied onto locals

- **GIVEN** a later change that would unify with tommy-ca/pstack
- **WHEN** local sibling versions are considered
- **THEN** they stay `MAJOR.MINOR.PATCH-<plugin-name>.N`
- **AND** existing tags are not moved

### Requirement: pstack is not a Cursor-style sibling folder

Feature: grok-build-marketplace
Rule: catalog is an index
Rule: Cursor sibling dirs are for grok-native ports only

The marketplace MUST list `pstack` as a git url plus sha of `https://github.com/tommy-ca/pstack.git`. It MUST NOT add a `pstack/` folder at the catalog root. It MUST NOT nest `plugins/pstack`. Cursor `plugins` uses sibling directories at repo root. This catalog already uses that shape for `agent-compatibility`, `cli-for-agent`, `tommy-mode`, and `long-horizon-swarm`. pstack is not that kind of member. Shipped docs MUST keep `grok plugin install tommy-ca/pstack --trust`. They MUST NOT document `tommy-ca/grok-build-plugins#pstack` as the default. Existing tags MUST NOT be moved.

#### Scenario: pstack stays a remote pin

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** the pstack row is read
- **THEN** `source` is url plus a 40-hex sha
- **AND** there is no `pstack/` directory
- **AND** there is no `plugins/` directory

#### Scenario: Cursor layout is not a pstack nest

- **GIVEN** a later change that would add `pstack/` to match cursor/plugins
- **WHEN** catalog membership is considered
- **THEN** pstack remains url+sha
- **AND** local siblings remain the grok-native ports only

### Requirement: long-horizon-swarm is an optional pstack overlay

Feature: grok-build-marketplace
Rule: Overlay sibling, not a pstack pack

The marketplace MUST list `long-horizon-swarm` as a local source `./long-horizon-swarm`. That folder MUST contain a grok `plugin.json` with `skills` and no `agents`, `hooks`, `commands`, or MCP. Shipped overlay docs MUST tell the operator to install and enable `tommy-ca/pstack` first. The overlay skill MUST refuse to spawn when poteto-mode is missing. Recurse MUST be parent-owned units. When `bun` or `node` can run pstack `skills/poteto-mode/scripts/orch/orch.ts`, the overlay MUST run `orch init` with store `long-horizon/<id>/`. When neither runtime exists (Grok chat sandbox), it MUST skip orch and use HostStore plus extras. It MUST NOT teach `chatroom_send`, and MUST NOT add a `pstack/` folder.

The sibling MUST ship overlay skills `long-horizon-swarm`, `field-guide`, `planner-worker-split`, `review-lenses`, `coordination-layer`, `megafile-gate`, `ossify-break`, and `openspec-intent-flow`. It MUST NOT ship `long-horizon-swarm-grok-adapter`, `.cursor-plugin`, `GROK-CHAT.md`, or Cursor `rules/`. The entry playbook MUST copy a ten-step TaskTree and MUST call `openspec-intent-flow` when the user names OpenSpec. Each overlay skill MUST set top-level `disable-model-invocation: true`. Overlay extras MUST live under `long-horizon/<id>/`. The unit board MUST be orch when bun or node exists, else HostStore.

#### Scenario: overlay is a local sibling

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** `plugins[]` is read
- **THEN** `long-horizon-swarm` uses local path `./long-horizon-swarm`
- **AND** pstack remains a pinned git url
- **AND** there is no `pstack/` directory

#### Scenario: overlay refuses without pstack

- **GIVEN** the overlay skill
- **WHEN** poteto-mode is missing
- **THEN** the skill tells the operator to install `tommy-ca/pstack --trust` and enable pstack
- **AND** it does not spawn workers

#### Scenario: overlay uses Grok Build spawn

- **GIVEN** the overlay playbook
- **WHEN** a worker is spawned
- **THEN** the text names `spawn_subagent` and `pstack:`
- **AND** recurse is parent-owned units
- **AND** children do not spawn
- **AND** it does not name `chatroom_send`

#### Scenario: overlay runs orch when bun or node exists

- **GIVEN** overlay HARNESS or REQUIRES and the playbook
- **WHEN** durable state is described
- **THEN** the playbook names `orch init`
- **AND** it probes bun then node
- **AND** it skips orch when neither exists
- **AND** Grok chat is the named no-runtime case

#### Scenario: overlay ships zip overlay skills grok-native

- **GIVEN** `long-horizon-swarm/skills/`
- **WHEN** skill directories are listed
- **THEN** they include `field-guide`, `planner-worker-split`, `review-lenses`, `coordination-layer`, `megafile-gate`, `ossify-break`, and `openspec-intent-flow`
- **AND** they do not include `long-horizon-swarm-grok-adapter`
- **AND** each overlay `SKILL.md` has `disable-model-invocation: true`

#### Scenario: overlay playbook is a TaskTree

- **GIVEN** `skills/long-horizon-swarm/playbooks/long-horizon-swarm.md`
- **WHEN** the playbook is read
- **THEN** it copies ten numbered steps
- **AND** it names `openspec-intent-flow`
- **AND** it names `field-guide`
- **AND** it names TaskTree or TaskNode
