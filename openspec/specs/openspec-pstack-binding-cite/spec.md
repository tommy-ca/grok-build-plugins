# openspec-pstack-binding-cite Specification

## Purpose
Cite fleet openspec-pstack-orch compose in SPEC/docs/LHS (propose gated B8, parallel after tasks, exclusive worktrees); no vendor; no Drove quotas; Soft-after band language from #1/#2.

## Requirements

### Requirement: Tip cites openspec-pstack-orch compose

Feature: openspec-pstack-binding-cite
Rule: Cite binding; do not vendor; do not invent Drove quotas

Shipped gbp SPEC and/or openspec-intent-flow docs MUST cite the fleet OpenSpec × pstack orch binding at `/workspace/fleet-external-agents/openspec-pstack-orch/` (or an equivalent mirrored LHS summary that points back to that package). The cite MUST state three compose rules: (1) OpenSpec propose completes before implementer spawn (B8 KEEP); (2) parallelism unlocks after `tasks.md` exists (Parallel band / P-parallel leaves); (3) parallel units use exclusive worktrees or conceptKey write targets. The cite MUST NOT vendor-copy the whole openspec-pstack-orch tree into tommy-ca/grok-build-plugins. The cite MUST NOT publish Drove `max_concurrent` standing-order numbers as gbp product requirements.

#### Scenario: Compose cite names three rules

- **GIVEN** tip SPEC or openspec-intent-flow docs after this Soft-after change applies
- **WHEN** an operator reads how OpenSpec and pstack orch compose
- **THEN** docs cite openspec-pstack-orch (path or mirrored summary)
- **AND** they state propose is gated before apply spawn
- **AND** they state parallelism is after tasks / Parallel bands
- **AND** they state exclusive worktrees (or exclusive write targets) per live leaf

#### Scenario: No vendor package in gbp

- **GIVEN** a change that would copy openspec-pstack-orch into the catalog repo
- **WHEN** Soft-after binding cite scope is considered
- **THEN** only a cite or short mirrored summary is allowed
- **AND** the full package tree is not vendored as a gbp sibling

#### Scenario: No Drove quota invent in gbp cite

- **GIVEN** the binding cite text in gbp SPEC/docs/LHS
- **WHEN** quota or concurrency language is considered
- **THEN** gbp text does not invent or prescribe Drove `max_concurrent` standing-order numbers
- **AND** fleet quota policy remains outside gbp product requirements

### Requirement: Soft-after depends on parallel-band convention language

Feature: openspec-pstack-binding-cite
Rule: Soft-after A — after tasks bands (and herd fan-out) language exists

This binding cite Act-on is Soft-after Parallel band convention language from `gbp-tasks-parallel-bands` (and ideally herd fan-out language from `gbp-herd-fanout-serial-apply`). Docs-only parallel propose is allowed once band language exists in the propose set. Apply SHOULD land after #1/#2 convention surfaces are on the integration branch unless Todd go authorizes docs-only Soft-after earlier. The cite MUST NOT claim parallelism-sync done from propose prose alone.

#### Scenario: Soft-after ordering honesty

- **GIVEN** Wave-4 propose artefacts for #1, #2, and this Soft-after id
- **WHEN** apply order is planned
- **THEN** binding cite is Soft-after A relative to tasks Parallel band convention
- **AND** propose drafts may exist together once band language is in the propose set
- **AND** done-claims wait for post-apply Prove bars
