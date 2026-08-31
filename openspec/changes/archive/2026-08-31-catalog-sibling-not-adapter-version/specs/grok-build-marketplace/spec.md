## ADDED Requirements

### Requirement: Local sibling identity is not grokbuild adapter identity

Feature: grok-build-marketplace
Rule: many local plugins, one git tag namespace
Rule: do not copy pstack grokbuild token onto locals

Local sibling versions MUST remain `MAJOR.MINOR.PATCH-<plugin-name>.N`. They MUST NOT use pstack's adapter grammar `MAJOR.MINOR.PATCH-grokbuild.N`. Shared `-grokbuild.0` already collided (`v1.0.0-grokbuild.0`). The marketplace pstack row MAY copy pstack's live version string for display. That row is url+sha and MUST NOT be a catalog tag. Existing tags MUST NOT be moved.

#### Scenario: local versions exclude grokbuild

- **GIVEN** local plugins `agent-compatibility`, `cli-for-agent`, and `tommy-mode`
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
