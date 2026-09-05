## ADDED Requirements

None.

## MODIFIED Requirements

### Requirement: Local sibling versions are unique in one git tag namespace

Feature: grok-build-marketplace
Rule: TagName is v plus plugin.json version
Rule: pstack is not tagged from this repo

Each local sibling `plugin.json` version MUST match `MAJOR.MINOR.PATCH-<plugin-name>.N`. Those versions MUST be unique across local siblings. The matching marketplace `plugins[].version` MUST equal that `plugin.json` version. The catalog root MUST NOT have `plugin.json`. `scripts/release.sh` MUST call `grok --sandbox off plugin tag --push` on local sibling folders only. It MUST NOT pass `--force`. If a local tag exists and origin does not, it MUST `git push origin` that ref. After the tag is on origin it MUST converge to a GitHub Release with `gh release view` or `gh release create --verify-tag --latest=false`. Nested grok MUST NOT be the tagger. `.github/workflows/release.yml` MUST run on `v*` and MUST do the same Release step. That workflow MUST NOT invoke `grok plugin tag`. It MUST NOT declare `workflow_dispatch`. pstack MUST remain a remote url plus sha and MUST NOT be a `release.sh` target.

#### Scenario: sibling versions cannot collide

- **GIVEN** local plugins `agent-compatibility`, `cli-for-agent`, `tommy-mode`, `long-horizon-swarm`, and `pstack-herdr`
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

### Requirement: Local sibling identity is not grokbuild adapter identity

Feature: grok-build-marketplace
Rule: many local plugins, one git tag namespace
Rule: do not copy pstack grokbuild token onto locals

Local sibling versions MUST remain `MAJOR.MINOR.PATCH-<plugin-name>.N`. They MUST NOT use pstack's adapter grammar `MAJOR.MINOR.PATCH-grokbuild.N`. Shared `-grokbuild.0` already collided (`v1.0.0-grokbuild.0`). The marketplace pstack row MAY copy pstack's live version string for display. That row is url+sha and MUST NOT be a catalog tag. Existing tags MUST NOT be moved.

#### Scenario: local versions exclude grokbuild

- **GIVEN** local plugins `agent-compatibility`, `cli-for-agent`, `tommy-mode`, `long-horizon-swarm`, and `pstack-herdr`
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

## REMOVED Requirements

None.

## RENAMED Requirements

None.
