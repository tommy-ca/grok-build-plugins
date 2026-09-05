## ADDED Requirements

### Requirement: long-horizon-swarm is an optional pstack overlay

Feature: grok-build-marketplace
Rule: Overlay sibling, not a pstack pack

The marketplace MUST list `long-horizon-swarm` as a local source `./long-horizon-swarm`. That folder MUST contain a grok `plugin.json` with `skills` and no `agents`, `hooks`, `commands`, or MCP. Shipped overlay docs MUST tell the operator to install and enable `tommy-ca/pstack` first. The overlay skill MUST refuse to spawn when poteto-mode is missing. Recurse MUST be parent-owned units. The overlay MUST NOT run `orch init`, MUST NOT teach `chatroom_send`, and MUST NOT add a `pstack/` folder.

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
- **AND** it does not name `orch init`
- **AND** it does not name `chatroom_send`

## MODIFIED Requirements

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

## REMOVED Requirements

None.

## RENAMED Requirements

None.
