## Purpose
Thin EXTERNAL-LOOP.md pointer at repo root plus rooms-map gbp charter row honesty — Symphony-class external loop mapped to fleet skills without a second SoT.

## Requirements
### Requirement: Thin WORKFLOW.md pointer at repo root

Feature: gbp-external-loop-docs
Rule: One-page pointer; not a second SoT; cite fleet skills + research

Shipped tommy-ca/grok-build-plugins MUST include a repo-root `WORKFLOW.md` that is a **thin pointer** / Symphony twin index, not a second source of truth (live path hard-renamed from historical `EXTERNAL-LOOP.md` by `workflow-md-rename`). The file MUST cite (by sand-workflow id or equivalent fleet path):

- `sand-workflow:inner-outer-orch`
- `sand-workflow:fleet-org-raci`
- `sand-workflow:drove-external-loop`
- `sand-workflow:herd-with-herdr`
- Research audit: `/workspace/fleet-external-agents/audits/2026-09-05-drove-symphony-external-loop-research.md` (fleet audit path / gist cite)

The pointer MUST map Symphony class concepts to fleet surfaces:

| Symphony | Fleet |
| --- | --- |
| tracker | boards / OpenSpec tasks |
| concurrency | max_concurrent + backpressure |
| isolation | CAO VM / worktree / herdr pane |
| WORKFLOW | brief + standing-orders |
| stop | VERIFIED \| human_review \| quota |

The pointer MUST name fleet roles: Drove = goal+quota+TaskTree tick; Horizon = single-change OpenSpec apply; CAO = parallel implement default; Herd = session herdr; Heavilifter = prove-it/recovery (not fan-out). It MUST state dual orch is forbidden; lever-first VERIFY; herd-journal→reconcile. It MUST cite thermos archive trail #15→#17 (propose→apply→archive under tip floor `35c8c6c`) as the worked example of CloudAgent plan-block → Heavilifter recovery. The pointer MUST NOT vendor full skill bodies, MUST NOT invent LIVE/LIVE_PASS, MUST NOT require an Elixir Symphony daemon, and MUST NOT remint `thermos-grok-port`.

#### Scenario: Pointer cites skills and research

- **GIVEN** tip after `workflow-md-rename` applies
- **WHEN** an operator opens repo-root `WORKFLOW.md`
- **THEN** the file exists and remains a pointer/index (not a skill-body dump)
- **AND** it cites inner-outer-orch, fleet-org-raci, drove-external-loop, herd-with-herdr
- **AND** it cites the Drove Symphony external-loop research audit path
- **AND** live path `EXTERNAL-LOOP.md` is absent

#### Scenario: Symphony maps to fleet surfaces

- **GIVEN** `WORKFLOW.md` after apply
- **WHEN** an operator looks for Symphony→fleet equivalence
- **THEN** tracker≈boards/OpenSpec tasks is stated
- **AND** concurrency≈max_concurrent+backpressure is stated
- **AND** isolation≈CAO VM / worktree / herdr pane is stated
- **AND** WORKFLOW≈brief+standing-orders is stated
- **AND** stop≈VERIFIED|human_review|quota is stated

#### Scenario: Roles and must-nots named

- **GIVEN** `WORKFLOW.md` after apply
- **WHEN** role and orch rules are read
- **THEN** Drove / Horizon / CAO / Herd / Heavilifter duties match the mapping above
- **AND** dual orch is forbidden
- **AND** lever-first VERIFY and herd-journal→reconcile are named
- **AND** thermos #15→#17 is cited as CloudAgent plan-block → Heavilifter recovery
- **AND** no Elixir Symphony daemon, no LIVE invent, no thermos remint is required

#### Scenario: Propose PR does not land product pointer

- **GIVEN** Wave-4 propose-only artefacts for `workflow-md-rename`
- **WHEN** the propose PR is reviewed
- **THEN** product `EXTERNAL-LOOP.md` remains unrenamed in that PR
- **AND** product `WORKFLOW.md` is absent from that PR
- **AND** apply tasks remain HOLD until Todd/Horizon go

## Requirements
- FROM: `### Requirement: Thin EXTERNAL-LOOP.md pointer at repo root`
- TO: `### Requirement: Thin WORKFLOW.md pointer at repo root`
