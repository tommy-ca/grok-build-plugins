## ADDED Requirements

None.

## MODIFIED Requirements

### Requirement: long-horizon-swarm is an optional pstack overlay

Feature: grok-build-marketplace
Rule: Overlay sibling, not a pstack pack

The marketplace MUST list `long-horizon-swarm` as a local source `./long-horizon-swarm`. That folder MUST contain a grok `plugin.json` with `skills` and no `agents`, `hooks`, `commands`, or MCP. Shipped overlay docs MUST tell the operator to install and enable `tommy-ca/pstack` first. The overlay skill MUST refuse to spawn when poteto-mode is missing. Recurse MUST be parent-owned units. When `bun` or `node` can run pstack `skills/poteto-mode/scripts/orch/orch.ts`, the overlay MUST run `orch init` with store `long-horizon/<id>/`. When neither runtime exists (Grok chat sandbox), it MUST skip orch and use HostStore plus extras. It MUST NOT teach `chatroom_send`, and MUST NOT add a `pstack/` folder.

The sibling MUST ship overlay skills `long-horizon-swarm`, `field-guide`, `planner-worker-split`, `review-lenses`, `coordination-layer`, `megafile-gate`, `ossify-break`, and `openspec-intent-flow`. It MUST NOT ship `long-horizon-swarm-grok-adapter`, `.cursor-plugin`, `GROK-CHAT.md`, or Cursor `rules/`. The entry playbook MUST copy a ten-step TaskTree and MUST call `openspec-intent-flow` when the user names OpenSpec. Each overlay skill MUST set top-level `disable-model-invocation: true`. Overlay extras MUST live under `long-horizon/<id>/`. The unit board MUST be orch when bun or node exists, else HostStore.

#### Scenario: overlay is a local sibling

- **GIVEN** `.grok-plugin/marketplace.json`
- **WHEN** `plugins[]` is read
- **THEN** `long-horizon-swarm` uses local path `./long-horizon-swarm`
- **AND** pstack remains a pinned git url
- **AND** there is no `pstack/` directory

#### Scenario: overlay refuses without pstack

- **GIVEN** the overlay skill
- **WHEN** poteto-mode is missing
- **THEN** the skill tells the operator to install `tommy-ca/pstack --trust` and enable pstack
- **AND** it does not spawn workers

#### Scenario: overlay uses Grok Build spawn

- **GIVEN** the overlay playbook
- **WHEN** a worker is spawned
- **THEN** the text names `spawn_subagent` and `pstack:`
- **AND** recurse is parent-owned units
- **AND** children do not spawn
- **AND** it does not name `chatroom_send`

#### Scenario: overlay runs orch when bun or node exists

- **GIVEN** overlay HARNESS or REQUIRES and the playbook
- **WHEN** durable state is described
- **THEN** the playbook names `orch init`
- **AND** it probes bun then node
- **AND** it skips orch when neither exists
- **AND** Grok chat is the named no-runtime case

#### Scenario: overlay ships zip overlay skills grok-native

- **GIVEN** `long-horizon-swarm/skills/`
- **WHEN** skill directories are listed
- **THEN** they include `field-guide`, `planner-worker-split`, `review-lenses`, `coordination-layer`, `megafile-gate`, `ossify-break`, and `openspec-intent-flow`
- **AND** they do not include `long-horizon-swarm-grok-adapter`
- **AND** each overlay `SKILL.md` has `disable-model-invocation: true`

#### Scenario: overlay playbook is a TaskTree

- **GIVEN** `skills/long-horizon-swarm/playbooks/long-horizon-swarm.md`
- **WHEN** the playbook is read
- **THEN** it copies ten numbered steps
- **AND** it names `openspec-intent-flow`
- **AND** it names `field-guide`
- **AND** it names TaskTree or TaskNode

## REMOVED Requirements

None.

## RENAMED Requirements

None.
