## ADDED Requirements

### Requirement: pstack-herdr is an optional pstack overlay

Feature: grok-build-marketplace
Rule: Overlay sibling, not a pstack pack
Rule: Arena and interrogate stay local; herdr implements after Act-on

The marketplace MUST list `pstack-herdr` as a local source `./pstack-herdr`. That folder MUST contain a grok `plugin.json` with `skills` and no `hooks`, `commands`, or MCP. `pstack-herdr` MUST NOT live in the pstack plugin tree. Shipped overlay docs MUST tell the operator to install and enable `tommy-ca/pstack` for arena, interrogate, and poteto. Arena runners, arena cross-judge, interrogate reviewers, and prove-it judgment MUST stay on pstack Task (`local` in the herdr agents map). Session-sized implement roles MAY route to ready herdr kinds only after Act-on. The overlay MUST NOT spawn N× the same herdr kind and call it an arena. The overlay MUST NOT add a `pstack/` folder. Pending herdr kinds MUST NOT be treated as live routes.

#### Scenario: overlay is a local sibling

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** `plugins[]` is read
- **THEN** `pstack-herdr` uses local path `./pstack-herdr`
- **AND** pstack remains a pinned git url
- **AND** there is no nested `pstack/` directory

#### Scenario: arena and interrogate stay local

- **GIVEN** the overlay skills and herdr agents map
- **WHEN** arena or interrogate roles are resolved
- **THEN** they stay on pstack Task (`local` in `pstack-herdr-agents`)
- **AND** session-sized implement roles may route to ready herdr kinds only after Act-on

#### Scenario: no fake N-agy arena

- **GIVEN** an arena or judgment panel
- **WHEN** herdr routing is considered
- **THEN** the overlay does not spawn N× the same herdr kind as a fake arena
- **AND** adversarial or generation diversity stays on local model diversity (or true multi-kind only when kinds are ready)

## MODIFIED Requirements

### Requirement: Catalog lists grok-native sibling plugins

Feature: grok-build-marketplace
Rule: Cursor sibling layout without vendoring cursor/plugins

The marketplace MUST list `agent-compatibility`, `cli-for-agent`, `tommy-mode`, `long-horizon-swarm`, and `pstack-herdr` as local sources (`./agent-compatibility`, `./cli-for-agent`, `./tommy-mode`, `./long-horizon-swarm`, `./pstack-herdr`). `tommy-mode` MUST NOT live in the pstack plugin tree. `long-horizon-swarm` MUST NOT live in the pstack plugin tree. `pstack-herdr` MUST NOT live in the pstack plugin tree. Those folders MUST contain a grok `plugin.json` with `skills` (and `agents` when the plugin has roles). They MUST NOT declare `hooks`, `commands`, or MCP. `cursor-team-kit`, canvases, `cursor-sdk`, and `orchestrate` MUST NOT be required.

#### Scenario: siblings are local, pstack is remote

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** `plugins[]` is read
- **THEN** `pstack` uses a pinned git url
- **AND** `agent-compatibility`, `cli-for-agent`, `tommy-mode`, `long-horizon-swarm`, and `pstack-herdr` use local paths
- **AND** there is no `plugins/` directory and no `pstack/` plugin folder

### Requirement: pstack is not a Cursor-style sibling folder

Feature: grok-build-marketplace
Rule: catalog is an index
Rule: Cursor sibling dirs are for grok-native ports only

The marketplace MUST list `pstack` as a git url plus sha of `https://github.com/tommy-ca/pstack.git`. It MUST NOT add a `pstack/` folder at the catalog root. It MUST NOT nest `plugins/pstack`. Cursor `plugins` uses sibling directories at repo root. This catalog already uses that shape for `agent-compatibility`, `cli-for-agent`, `tommy-mode`, `long-horizon-swarm`, and `pstack-herdr`. pstack is not that kind of member. Shipped docs MUST keep `grok plugin install tommy-ca/pstack --trust`. They MUST NOT document `tommy-ca/grok-build-plugins#pstack` as the default. Existing tags MUST NOT be moved.

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
