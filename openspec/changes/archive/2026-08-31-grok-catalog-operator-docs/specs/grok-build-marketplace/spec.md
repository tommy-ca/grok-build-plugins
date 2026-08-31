## ADDED Requirements

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

## MODIFIED Requirements

None.

## REMOVED Requirements

None.

## RENAMED Requirements

None.
