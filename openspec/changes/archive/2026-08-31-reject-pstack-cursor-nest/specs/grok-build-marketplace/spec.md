## ADDED Requirements

### Requirement: pstack is not a Cursor-style sibling folder

Feature: grok-build-marketplace
Rule: catalog is an index
Rule: Cursor sibling dirs are for grok-native ports only

The marketplace MUST list `pstack` as a git url plus sha of `https://github.com/tommy-ca/pstack.git`. It MUST NOT add a `pstack/` folder at the catalog root. It MUST NOT nest `plugins/pstack`. Cursor `plugins` uses sibling directories at repo root. This catalog already uses that shape for `agent-compatibility`, `cli-for-agent`, and `tommy-mode`. pstack is not that kind of member. Shipped docs MUST keep `grok plugin install tommy-ca/pstack --trust`. They MUST NOT document `tommy-ca/grok-build-plugins#pstack` as the default. Existing tags MUST NOT be moved.

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
