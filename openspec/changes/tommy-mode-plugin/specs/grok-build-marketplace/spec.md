## ADDED Requirements

None.

## MODIFIED Requirements

### Requirement: Catalog lists grok-native sibling plugins

Feature: grok-build-marketplace
Rule: Cursor sibling layout without vendoring cursor/plugins

The marketplace MUST list `agent-compatibility`, `cli-for-agent`, and `tommy-mode` as local sources (`./agent-compatibility`, `./cli-for-agent`, `./tommy-mode`). Those folders MUST contain a grok `plugin.json` with `skills` (and `agents` when the plugin has roles). They MUST NOT declare `hooks`, `commands`, or MCP. `tommy-mode` MUST NOT live in the pstack plugin tree.

#### Scenario: siblings are local, pstack is remote

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** `plugins[]` is read
- **THEN** `pstack` uses a pinned git url
- **AND** `agent-compatibility`, `cli-for-agent`, and `tommy-mode` use local paths
- **AND** there is no `plugins/` directory and no `pstack/` plugin folder

## REMOVED Requirements

None.

## RENAMED Requirements

None.
