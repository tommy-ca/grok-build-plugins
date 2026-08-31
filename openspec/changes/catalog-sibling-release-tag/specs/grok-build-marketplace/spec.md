## ADDED Requirements

### Requirement: Local sibling versions are unique in one git tag namespace

Feature: grok-build-marketplace
Rule: TagName is v plus plugin.json version
Rule: pstack is not tagged from this repo

Each local sibling `plugin.json` version MUST match `MAJOR.MINOR.PATCH-<plugin-name>.N`. Those versions MUST be unique across local siblings. The matching marketplace `plugins[].version` MUST equal that `plugin.json` version. The catalog root MUST NOT have `plugin.json`. `scripts/release.sh` MUST call `grok --sandbox off plugin tag --push` on local sibling folders only. It MUST NOT pass `--force`. If a local tag exists and origin does not, it MUST `git push origin` that ref. After the tag is on origin it MUST converge to a GitHub Release with `gh release view` or `gh release create --verify-tag --latest=false`. Nested grok MUST NOT be the tagger. `.github/workflows/release.yml` MUST run on `v*` and MUST do the same Release step. That workflow MUST NOT invoke `grok plugin tag`. It MUST NOT declare `workflow_dispatch`. pstack MUST remain a remote url plus sha and MUST NOT be a `release.sh` target.

#### Scenario: sibling versions cannot collide

- **GIVEN** local plugins `agent-compatibility`, `cli-for-agent`, and `tommy-mode`
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
