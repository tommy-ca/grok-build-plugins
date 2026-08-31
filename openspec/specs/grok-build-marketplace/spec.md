# grok-build-marketplace Specification

## Purpose
TBD - created by archiving change grok-build-plugins-marketplace. Update Purpose after archive.

## Requirements

### Requirement: Catalog lists pstack without copying the skill tree

Feature: grok-build-marketplace
Rule: tommy-ca/pstack is the plugin source of truth

The marketplace MUST list a plugin named `pstack` whose source is a git URL of `https://github.com/tommy-ca/pstack.git` pinned to a full 40-hex sha. It MUST NOT rsync `skills/` into a second copy.

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

Shipped catalog docs MUST say `grok plugin marketplace add` rewrites `~/.grok/config.toml` and fails with EROFS (os error 30) inside a sandboxed Grok agent session. They MUST tell the operator to run add from a host shell. They MUST keep `grok plugin install tommy-ca/pstack --trust` as the in-session install path.

#### Scenario: Agent nested grok cannot add a marketplace

- **GIVEN** `__GROK_INSIDE_BWRAP=1` and `config.toml` bind-mounted read-only
- **WHEN** shipped docs describe `grok plugin marketplace add`
- **THEN** they name EROFS on `~/.grok/config.toml`
- **AND** they name a host shell as the fix

### Requirement: v1 catalog is pstack only

Feature: grok-build-marketplace
Rule: Optional Cursor siblings stay optional

`cursor-team-kit` and `make-bot-ui` MUST NOT be required Grok plugins.

#### Scenario: v1 catalog is pstack only

- **GIVEN** the v1 marketplace index
- **WHEN** plugins[] is read
- **THEN** the only installable plugin is `pstack`

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

Shipped catalog docs MUST say playbooks spawn `pstack:<role-key>` (`pstack:how-explorer`). They MUST say bare `how-explorer` is unknown even after enable.

#### Scenario: Docs name the live spawn type

- **GIVEN** pstack is enabled
- **WHEN** catalog docs describe subagents
- **THEN** they use `pstack:how-explorer`
- **AND** they do not claim the bare stem is a live type

### Requirement: Marketplace add still installs owner/repo

Feature: grok-build-marketplace
Rule: Bare pstack stays ambiguous after add

After `grok plugin marketplace add tommy-ca/grok-build-plugins`, shipped docs MUST still install `tommy-ca/pstack`, never bare `pstack`.

#### Scenario: Add does not change the install command

- **GIVEN** the catalog is added
- **WHEN** docs name install
- **THEN** the command is still `grok plugin install tommy-ca/pstack --trust`
