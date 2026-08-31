## ADDED Requirements

### Requirement: Catalog lists grok-native sibling plugins

Feature: grok-build-marketplace
Rule: Cursor sibling layout without vendoring cursor/plugins

The marketplace MUST list `agent-compatibility` and `cli-for-agent` as local sources (`./agent-compatibility`, `./cli-for-agent`). Those folders MUST contain a grok `plugin.json` with `skills` (and `agents` when the plugin has roles). They MUST NOT declare `hooks`, `commands`, or MCP. `cursor-team-kit`, canvases, `cursor-sdk`, and `orchestrate` MUST NOT be required.

#### Scenario: siblings are local, pstack is remote

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** `plugins[]` is read
- **THEN** `pstack` uses a pinned git url
- **AND** `agent-compatibility` and `cli-for-agent` use local paths
- **AND** there is no `plugins/` directory and no `pstack/` plugin folder

## MODIFIED Requirements

### Requirement: Catalog lists pstack without copying the skill tree

Feature: grok-build-marketplace
Rule: tommy-ca/pstack is the plugin source of truth

The marketplace MUST list a plugin named `pstack` whose source is a git URL of `https://github.com/tommy-ca/pstack.git` pinned to a full 40-hex sha. It MUST NOT rsync `skills/` into a second copy. It MUST NOT nest pstack as `plugins/pstack` or as a `pstack/` sibling folder in this repo.

#### Scenario: Pin is recorded

- **GIVEN** a published marketplace index
- **WHEN** provenance is inspected
- **THEN** the pstack entry includes a 40-character lowercase hex git sha

## REMOVED Requirements

### Requirement: v1 catalog is pstack only

**Reason**: Sibling grok-native plugins now ship in this catalog. pstack remains a remote pin.

**Migration**: Install siblings from the catalog after marketplace add. Keep `grok plugin install tommy-ca/pstack --trust` for pstack.

## RENAMED Requirements

None.
