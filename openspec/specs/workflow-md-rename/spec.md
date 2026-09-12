## Purpose

Hard-rename repo-root `EXTERNAL-LOOP.md` → `WORKFLOW.md` and flip living cites (HARNESS/README/verify). Preserve Symphony twin body; orch loads tip WORKFLOW.md before dispatch (Drove Band B out-of-repo).

## Requirements

### Requirement: Hard-rename EXTERNAL-LOOP.md to WORKFLOW.md

Feature: workflow-md-rename
Rule: Filename flip only; Symphony twin content preserved

After apply, tommy-ca/grok-build-plugins repo-root MUST ship `WORKFLOW.md` and MUST NOT ship `EXTERNAL-LOOP.md` as the live twin path. Apply MUST hard-rename (`git mv` or equivalent) `EXTERNAL-LOOP.md` → `WORKFLOW.md`. The renamed file MUST preserve the Symphony WORKFLOW.md-shaped twin already landed by closed `herdr-agy-workflow-bind` (frontmatter-equivalent runtime + Markdown body contract). Apply MUST NOT rewrite session-path or isolation content as part of this change. Apply MUST NOT remint closed `thermos-grok-port`, `lhs-swarm-economics-refresh`, or `herdr-agy-workflow-bind` archives. Apply MUST NOT require an Elixir Symphony daemon and MUST NOT invent LIVE/LIVE_PASS.

#### Scenario: Live twin path is WORKFLOW.md

- **GIVEN** tip after this change applies
- **WHEN** an operator lists repo root
- **THEN** `WORKFLOW.md` exists
- **AND** `EXTERNAL-LOOP.md` is absent as the live twin path
- **AND** `WORKFLOW.md` retains Symphony twin shape (runtime keys + body contract)

#### Scenario: Content not reminted

- **GIVEN** apply for `workflow-md-rename`
- **WHEN** the rename commit is inspected
- **THEN** the change is a hard-rename (or equivalent path flip) of the existing twin
- **AND** Session arms Herd→herdr→agy and isolation trinity prose are not stripped
- **AND** closed thermos / lhs / herdr-agy archives are not reminted

#### Scenario: Propose PR does not land the rename

- **GIVEN** Wave-4 propose-only artefacts for `workflow-md-rename`
- **WHEN** the propose PR is reviewed
- **THEN** product `EXTERNAL-LOOP.md` is still present and unrenamed in that PR
- **AND** product `WORKFLOW.md` is absent from that PR
- **AND** apply tasks remain HOLD until Todd/Horizon go

### Requirement: Living product cites flip to WORKFLOW.md

Feature: workflow-md-rename
Rule: HARNESS + README + verify assert name WORKFLOW.md

After apply, living product cites MUST name repo-root `WORKFLOW.md` (not `EXTERNAL-LOOP.md`):

- `long-horizon-swarm/HARNESS.md` fleet-seat / session-arms cites
- `long-horizon-swarm/README.md` fleet-seat cite
- `scripts/verify-long-horizon-swarm.sh` harness assert MUST require `WORKFLOW.md` (not `EXTERNAL-LOOP.md`)

Session arms Herd→herdr→agy and isolation trinity (CAO = cloud VM; Herd session = herdr pane + `kind=agy`; Heavilifter = on-box worktree recovery) MUST remain stated. Dual orch MUST remain forbidden. Apply MUST NOT clone arena/interrogate. Drove box SoT skill/persona/roles-map cite flips are **out of scope** for the gbp git Apply PR (separate Drove/Opus/eggbot Metadata apply — tasks note only).

#### Scenario: HARNESS and README cite WORKFLOW.md

- **GIVEN** tip after this change applies
- **WHEN** an operator opens `long-horizon-swarm/HARNESS.md` and `long-horizon-swarm/README.md`
- **THEN** both cite repo-root `WORKFLOW.md`
- **AND** neither asserts live path `EXTERNAL-LOOP.md`
- **AND** Session arms and isolation trinity remain named
- **AND** dual orch remains forbidden

#### Scenario: Verify assert expects WORKFLOW.md

- **GIVEN** the apply branch
- **WHEN** an operator runs `scripts/verify-long-horizon-swarm.sh`
- **THEN** the script exits 0
- **AND** the harness assert requires `WORKFLOW.md`
- **AND** the harness assert does not require `EXTERNAL-LOOP.md`

#### Scenario: Box SoT cite flip stays out of gbp git PR

- **GIVEN** Wave-5 gbp git Apply for this change
- **WHEN** ownership of sand-workflow / roles-map / persona EXTERNAL-LOOP→WORKFLOW cite flips is assigned
- **THEN** Drove/Opus/eggbot own those box SoT edits
- **AND** the gbp git Apply PR is not required to contain those box files
- **AND** tasks note the out-of-scope Metadata apply


### Requirement: Orchestrators MUST load tip WORKFLOW.md before dispatch

Feature: workflow-md-rename
Rule: Symphony-class — orch follows in-repo WORKFLOW.md; refuse/hold if absent

After apply, fleet orchestrators MUST treat tip repo-root `WORKFLOW.md` as the in-repo Symphony WORKFLOW twin and MUST load its frontmatter-equivalent runtime + Markdown body **before** dispatch:

1. **Drove** continuous tick: MUST load tip `WORKFLOW.md` before spawn; MUST refuse or hold spawn when the file is missing or missing required keys/sections — at minimum tracker/board, polling/tick, workspace/isolation, agent concurrency, and Session arms (Herd→herdr→agy).
2. **Horizon** single-change / leaf apply: briefs MUST cite tip `WORKFLOW.md`; Session arms, isolation trinity, and lever-first VERIFY MUST be taken from that file (not invented ad-hoc).
3. **Herd** session arms: herdr→agy path MUST follow the path named in tip `WORKFLOW.md` (not an ad-hoc alternate).

This requirement is the OpenSpec contract for orch behaviour. Flipping box SoT sand-workflow skill bodies (`drove-external-loop`, `fleet-org-raci`, `inner-outer-orch`, `eng-lead-merge-authority`) to say "read tip WORKFLOW.md" is **Drove Apply / Band B Metadata** — not a gbp product file in the propose or gbp git Apply PR unless Todd/Horizon later expands scope.

#### Scenario: Drove refuses spawn when WORKFLOW.md missing or incomplete

- **GIVEN** a Drove continuous-tick brief ready to spawn
- **WHEN** tip `WORKFLOW.md` is missing OR lacks required keys (tracker/polling/workspace/agent/session arms)
- **THEN** Drove refuses or holds spawn
- **AND** it does not dispatch implement arms until tip WORKFLOW.md is present and complete

#### Scenario: Horizon briefs cite tip WORKFLOW.md

- **GIVEN** a Horizon single-change / leaf apply brief after this change applies
- **WHEN** Session arms, isolation trinity, or lever-first VERIFY are specified
- **THEN** the brief cites tip `WORKFLOW.md`
- **AND** those rules are taken from that file (not invented ad-hoc)

#### Scenario: Herd follows named session arms

- **GIVEN** a Herd session implement / PR-review after this change applies
- **WHEN** the session path is chosen
- **THEN** Herd→herdr→agy follows the path named in tip `WORKFLOW.md`
- **AND** an ad-hoc alternate path that ignores tip WORKFLOW.md is refused

#### Scenario: Box skill flip is Drove Band B not gbp propose

- **GIVEN** Wave-4 propose-only artefacts for `workflow-md-rename`
- **WHEN** sand-workflow skill body edits for "read tip WORKFLOW.md" are considered
- **THEN** those edits are listed as Drove Apply / Band B Metadata tasks only
- **AND** the gbp propose PR does not contain `/home/box/sand-data/workflows/` skill body edits

### Requirement: Propose PR is OpenSpec-only

Feature: workflow-md-rename
Rule: Wave-4 lands artefacts; Apply HOLD; no product rename

Wave-4 MUST add only `openspec/changes/workflow-md-rename/` artefacts. It MUST NOT rename `EXTERNAL-LOOP.md`, create product `WORKFLOW.md`, or edit `long-horizon-swarm/HARNESS.md`, `long-horizon-swarm/README.md`, or `scripts/verify-long-horizon-swarm.sh`. It MUST NOT remint closed thermos / lhs / herdr-agy archives. Apply remains HOLD until Todd/Horizon go. OpenSpec `validate --type change --strict` MUST PASS on the propose artefacts.

#### Scenario: Propose tree is artefacts only

- **GIVEN** Wave-4 propose-only artefacts for `workflow-md-rename`
- **WHEN** the propose PR diff is reviewed
- **THEN** the only new paths are under `openspec/changes/workflow-md-rename/`
- **AND** product `EXTERNAL-LOOP.md` is unchanged
- **AND** product HARNESS / README / verify script are unchanged
- **AND** thermos / lhs / herdr-agy archives are not reminted
