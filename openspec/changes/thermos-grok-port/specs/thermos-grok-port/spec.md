## ADDED Requirements

### Requirement: Sibling plugin thermos ports upstream surfaces to Grok Build

Feature: thermos-grok-port
Rule: R-THERMOS-01 — catalog sibling, not a Cursor dump

The catalog MUST ship a sibling directory `thermos/` at repo root with a grok `plugin.json`, README, `HARNESS.md`, `skills/`, and `agents/` adapted from upstream cursor/plugins thermos (MIT). Skills MUST include `thermos` (orchestrator), `thermo-nuclear-review`, and `thermo-nuclear-code-quality-review`. Agents MUST include the dual-rubric review roles (upstream names `thermo-nuclear-review-subagent` and `thermo-nuclear-code-quality-review-subagent`, or harness-qualified equivalents). The folder MUST NOT declare `hooks`, `commands`, or MCP. The plugin MUST NOT live in the pstack plugin tree and MUST NOT nest as `plugins/thermos` or under `tommy-ca/pstack`.

#### Scenario: Installable sibling surfaces exist

- **GIVEN** Wave-5 apply has landed the thermos sibling
- **WHEN** an operator inspects `thermos/`
- **THEN** `plugin.json`, README, `HARNESS.md`, `skills/`, and `agents/` are present
- **AND** skills include the orchestrator plus both rubrics
- **AND** there is no `hooks`, `commands`, or MCP declaration

#### Scenario: Not nested in pstack

- **GIVEN** catalog membership rules (ADR 0001 / 0002 / 0006)
- **WHEN** thermos packaging is considered
- **THEN** thermos is a catalog-root sibling `./thermos`
- **AND** it is not under `tommy-ca/pstack` or `plugins/pstack`

### Requirement: Dual-rubric orchestrator uses Grok-native spawn map

Feature: thermos-grok-port
Rule: R-THERMOS-02 — parallel review then synthesize; not Cursor Task names only

The `thermos` orchestrator skill MUST gather scoped diff/context, launch **both** rubric reviewers in parallel, then synthesize deduplicated prioritized findings. `HARNESS.md` MUST map Grok primitives for slash, spawn, join, and cancel (for example `spawn_subagent`, plugin-qualified `thermos:<role>`, `get_command_or_subagent_output`, `kill_command_or_subagent`) and MAY cite poteto/swarm handoff. Shipped invoke docs MUST NOT treat Cursor `Task` / `subagent_type` / `run_in_background` as the **sole** API.

#### Scenario: Parallel dual-rubric then synthesize

- **GIVEN** an enabled thermos plugin and a scoped branch/PR diff
- **WHEN** the operator runs the thermos orchestrator
- **THEN** both bug/security and code-quality rubrics run as parallel reviewers
- **AND** the parent synthesizes deduped findings with evidence

#### Scenario: HARNESS names Grok primitives

- **GIVEN** shipped `thermos/HARNESS.md`
- **WHEN** an operator reads how to spawn and join reviewers
- **THEN** the harness names Grok spawn/join primitives (or poteto/swarm equivalents)
- **AND** it does not present Cursor Task flag names as the only invoke path

### Requirement: Poteto bind includes arena, interrogate, swarm handoff, and lever VERIFY

Feature: thermos-grok-port
Rule: R-THERMOS-03 — falsifiable VERIFY; not prose-only

The thermos port MUST bind poteto surfaces: **arena** (contested port/design forks), **interrogate** (post-apply stacked review lens), **swarm / long-horizon handoff** (parallel dual-rubric fan-out when a standing program owns the loop), and **lever VERIFY**. Lever VERIFY MUST cite a named lever script (for example `scripts/verify-thermos.sh`) and/or a `verify-thermos` / `verify-*` skill that a reviewer can rerun. Prose-only “review done” without a rerunnable lever MUST be rejected.

#### Scenario: Lever VERIFY is falsifiable

- **GIVEN** Wave-5 apply claims thermos VERIFIED
- **WHEN** a reviewer reruns the cited lever
- **THEN** the lever is a named script or verify-* skill
- **AND** pass/fail is observable without trusting prose alone

#### Scenario: Poteto surfaces are named

- **GIVEN** shipped thermos README or HARNESS
- **WHEN** poteto binding is inspected
- **THEN** arena, interrogate, swarm/long-horizon handoff, and lever VERIFY are named
- **AND** Cursor Task name clones are not the only binding language

### Requirement: Marketplace listing and SemVer hold catalog ADRs

Feature: thermos-grok-port
Rule: R-THERMOS-04 — SemVer `-thermos.N`; catalog-is-index; no pstack nest

The marketplace MUST list `thermos` as local source `./thermos` with `plugins[].version` equal to `thermos/plugin.json` version matching `MAJOR.MINOR.PATCH-thermos.N`. Catalog-is-index ADRs 0001–0006 MUST hold: no nest under pstack; sibling tags include plugin name; SemVer not CalVer; sibling ≠ grokbuild adapter grammar. Docs-only changes without installable `thermos/` surfaces MUST be rejected at apply.

#### Scenario: SemVer thermos namespace

- **GIVEN** landed `thermos/plugin.json` and marketplace row
- **WHEN** versions are read
- **THEN** both equal a `MAJOR.MINOR.PATCH-thermos.N` string
- **AND** the version does not use CalVer-only or `-grokbuild.N` identity

#### Scenario: Docs-only without surfaces rejected

- **GIVEN** an apply PR that only edits docs and OpenSpec prose
- **WHEN** installable `thermos/` plugin surfaces are missing
- **THEN** the apply is rejected
- **AND** VERIFIED is not claimed
