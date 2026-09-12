## ADDED Requirements

### Requirement: Thin EXTERNAL-LOOP.md pointer at repo root

Feature: gbp-external-loop-docs
Rule: One-page pointer; not a second SoT; cite fleet skills + research

Shipped tommy-ca/grok-build-plugins MUST include a repo-root `EXTERNAL-LOOP.md` that is a **thin pointer**, not a second source of truth. The file MUST cite (by sand-workflow id or equivalent fleet path):

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

- **GIVEN** tip after this change applies
- **WHEN** an operator opens repo-root `EXTERNAL-LOOP.md`
- **THEN** the file exists and is one-page / thin
- **AND** it cites inner-outer-orch, fleet-org-raci, drove-external-loop, herd-with-herdr
- **AND** it cites the Drove Symphony external-loop research audit path

#### Scenario: Symphony maps to fleet surfaces

- **GIVEN** `EXTERNAL-LOOP.md` after apply
- **WHEN** an operator looks for Symphony→fleet equivalence
- **THEN** tracker≈boards/OpenSpec tasks is stated
- **AND** concurrency≈max_concurrent+backpressure is stated
- **AND** isolation≈CAO VM / worktree / herdr pane is stated
- **AND** WORKFLOW≈brief+standing-orders is stated
- **AND** stop≈VERIFIED|human_review|quota is stated

#### Scenario: Roles and must-nots named

- **GIVEN** `EXTERNAL-LOOP.md` after apply
- **WHEN** role and orch rules are read
- **THEN** Drove / Horizon / CAO / Herd / Heavilifter duties match the mapping above
- **AND** dual orch is forbidden
- **AND** lever-first VERIFY and herd-journal→reconcile are named
- **AND** thermos #15→#17 is cited as CloudAgent plan-block → Heavilifter recovery
- **AND** no Elixir Symphony daemon, no LIVE invent, no thermos remint is required

#### Scenario: Propose PR does not land product pointer

- **GIVEN** Wave-4 propose-only artefacts for `gbp-external-loop-docs`
- **WHEN** the propose PR is reviewed
- **THEN** product `EXTERNAL-LOOP.md` is absent from that PR
- **AND** apply tasks remain HOLD until Todd/Horizon go

### Requirement: rooms-map gbp charter row honesty

Feature: gbp-external-loop-docs
Rule: Spec requires exact row; Drove/eggbot applies to box SoT

The change MUST document that Drove (or eggbot under desk policy) applies the live rooms-map row to box SoT `/workspace/fleet-external-agents/rooms-map.md`. That update is **not** required to land inside the tommy-ca/grok-build-plugins git PR. Spec and tasks MUST require the row content exactly:

`| 91ada72e-0abc-40f8-bb44-971a584fbdf3 | grok-build-plugins | gbp / thermos / marketplace plugin programs only | Drove, Herd, Horizon, CAO, Heavilifter (+ Planner when seated) | live |`

Apply MAY split: Metadata/docs in gbp (EXTERNAL-LOOP.md + OpenSpec merge) and a separate box update for rooms-map. Propose MUST NOT claim the rooms-map row is already live from OpenSpec prose alone.

#### Scenario: Required row content is named in OpenSpec

- **GIVEN** propose artefacts for `gbp-external-loop-docs`
- **WHEN** apply readiness for rooms-map is checked
- **THEN** tasks/spec name the exact id `91ada72e-0abc-40f8-bb44-971a584fbdf3`
- **AND** intended name is `grok-build-plugins`
- **AND** charter is gbp / thermos / marketplace plugin programs only
- **AND** members include Drove, Herd, Horizon, CAO, Heavilifter (+ Planner when seated)
- **AND** status is `live`

#### Scenario: Box SoT owner is Drove/eggbot not the gbp propose PR

- **GIVEN** Wave-4 propose PR for this change
- **WHEN** rooms-map apply ownership is assigned
- **THEN** Drove/eggbot owns the live edit of `/workspace/fleet-external-agents/rooms-map.md`
- **AND** the gbp git propose PR is not required to contain that file
- **AND** done-claims for the row wait until the box SoT row exists (Metadata verify)
