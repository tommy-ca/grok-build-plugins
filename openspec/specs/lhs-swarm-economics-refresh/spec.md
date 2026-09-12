## Purpose
Refresh long-horizon-swarm overlay for fleet EXTERNAL-LOOP seat bind, lever-first VERIFY, blog failure-mode refuse/stop checklist, and SemVer 1.2.0-long-horizon-swarm.N — without reminting thermos or gbp-external-loop-docs, and without cloning arena/interrogate.

## Requirements
### Requirement: Fleet seat bind in HARNESS and README

Feature: lhs-swarm-economics-refresh
Rule: Overlay host map names WORKFLOW.md fleet seats; still Grok primitives

After apply, `long-horizon-swarm/HARNESS.md` and `long-horizon-swarm/README.md` MUST bind overlay roles to fleet seats per repo-root `WORKFLOW.md` (cite, do not remint `gbp-external-loop-docs`; live path hard-renamed from historical `EXTERNAL-LOOP.md` by `workflow-md-rename`):

| Overlay need | Fleet seat |
| --- | --- |
| Propose / OpenSpec artefacts | Planner |
| Single-change OpenSpec apply/merge | Horizon |
| Continuous tick (goal + quota + TaskTree) | Drove |
| Default parallel implement | Cloud Agent Orchestrator (CAO) |
| Session herdr after Act-on | Herd |
| Prove-it / session recovery / on-box worktree when cloud blocked | Heavilifter |
| Verification cadence / maintain-verification | Nightly Audit Engineer |

The bind MUST state dual orch is forbidden (exactly one orch owner per brief). It MUST keep the existing Grok primitive map (`spawn_subagent` / `pstack:<role>` / orch-or-HostStore / join / cancel / worktree isolation). It MUST NOT vendor sand-workflow skill bodies. It MUST NOT invent Cursor VCS. It MUST NOT treat Heavilifter as primary N-arm fan-out. README MUST point operators at the HARNESS fleet table (or repeat it). Plugin MUST still ship no `agents/` unless a later ADR says otherwise; spawn stays `pstack:<role>`.

#### Scenario: HARNESS names fleet seats and Grok primitives

- **GIVEN** tip after `workflow-md-rename` applies
- **WHEN** an operator opens `long-horizon-swarm/HARNESS.md`
- **THEN** Drove / Horizon / CAO / Herd / Heavilifter / Planner / Nightly Audit duties match the mapping above
- **AND** dual orch is forbidden
- **AND** Grok primitives `spawn_subagent`, `pstack:`, orch-or-HostStore, and worktree isolation remain named
- **AND** `WORKFLOW.md` is cited without reminting `gbp-external-loop-docs`
- **AND** live cites do not assert path `EXTERNAL-LOOP.md`

#### Scenario: README is not spawn-only

- **GIVEN** `long-horizon-swarm/README.md` after apply
- **WHEN** an operator looks for who runs a standing program
- **THEN** the page names or points at the HARNESS fleet seat bind
- **AND** it still tells the operator to install and enable `tommy-ca/pstack` first
- **AND** it still says this plugin ships no agents
- **AND** it cites repo-root `WORKFLOW.md` (not `EXTERNAL-LOOP.md`)

#### Scenario: Propose PR does not refresh product HARNESS

- **GIVEN** Wave-4 propose-only artefacts for `workflow-md-rename`
- **WHEN** the propose PR is reviewed
- **THEN** product `long-horizon-swarm/HARNESS.md` and `README.md` are unchanged in that PR
- **AND** apply tasks remain HOLD until Todd/Horizon go

### Requirement: Fleet roles-map and persona cite honesty

Feature: lhs-swarm-economics-refresh
Rule: Spec names exact cites; Drove/eggbot applies box SoT

The change MUST document that Drove (or eggbot under desk policy) applies live cite lines to box SoT. Those updates are **not** required to land inside the tommy-ca/grok-build-plugins git PR. Apply MAY split: gbp git Apply lands overlay + SemVer + OpenSpec merge (Horizon leaf); Drove/eggbot lands roles-map / `fleet-roles.mdc` / personas. Propose MUST NOT claim those box files are already live from OpenSpec prose alone.

`/workspace/fleet-external-agents/roles-map.md` MUST gain a standing-program overlay cite block whose intended content is:

`## Standing program overlay (long-horizon-swarm)`

`When a brief is a standing program (hours/days, spec-as-root, TaskTree), cite overlay skills from tommy-ca/grok-build-plugins long-horizon-swarm (do not clone): planner-worker-split (planner≠worker + CostPolicy); field-guide; review-lenses (≥2 incl pstack interrogate); coordination-layer / megafile-gate / ossify-break; openspec-intent-flow. Arena and interrogate stay pstack cites. Lever-first VERIFY: Brief.VERIFY MUST name verify-* skill or scripts/verify-*.sh. Fleet seats per WORKFLOW.md: Drove tick, Horizon single-change, CAO parallel, Herd session herdr, Heavilifter recovery. Dual orch forbidden.`

`~/.cursor/rules/fleet-roles.mdc` MUST carry the same cite as a comment twin (alwaysApply map stays the role-key table). Agent personas for Drove, Horizon, Planner, CAO, Herd, Heavilifter, and Nightly Audit MUST each include a one-line cite of the overlay when a standing program is armed.

**Note (workflow-md-rename):** flipping box SoT / persona / roles-map cites from `EXTERNAL-LOOP.md` → `WORKFLOW.md` is **out of scope** for the gbp git Apply PR — Drove/Opus/eggbot Metadata apply (tasks note only).

#### Scenario: Required cite content is named in OpenSpec

- **GIVEN** propose artefacts for `workflow-md-rename` (or living lhs after merge)
- **WHEN** apply readiness for fleet roles-map is checked
- **THEN** tasks/spec name the standing-program overlay heading
- **AND** required skill cites include planner-worker-split, field-guide, review-lenses, megafile-gate, ossify-break, openspec-intent-flow
- **AND** lever-first VERIFY and WORKFLOW.md seats are named
- **AND** arena/interrogate stay pstack cites

#### Scenario: Box SoT owner is Drove/eggbot not the gbp propose PR

- **GIVEN** Wave-4 propose PR for `workflow-md-rename`
- **WHEN** roles-map / persona apply ownership is assigned
- **THEN** Drove/eggbot owns the live edit of `/workspace/fleet-external-agents/roles-map.md`, `~/.cursor/rules/fleet-roles.mdc`, and the named personas
- **AND** the gbp git propose PR is not required to contain those files
- **AND** done-claims for the cites wait until the box SoT lines exist (Metadata verify)
- **AND** EXTERNAL-LOOP→WORKFLOW box SoT cite flip remains out of scope for the gbp git Apply PR
