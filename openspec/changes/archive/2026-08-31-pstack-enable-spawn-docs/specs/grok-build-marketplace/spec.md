## ADDED Requirements

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
