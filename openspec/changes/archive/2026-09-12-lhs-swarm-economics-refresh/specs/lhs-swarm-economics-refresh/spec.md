## ADDED Requirements

### Requirement: Fleet seat bind in HARNESS and README

Feature: lhs-swarm-economics-refresh
Rule: Overlay host map names EXTERNAL-LOOP fleet seats; still Grok primitives

After apply, `long-horizon-swarm/HARNESS.md` and `long-horizon-swarm/README.md` MUST bind overlay roles to fleet seats per repo-root `EXTERNAL-LOOP.md` (cite, do not remint `gbp-external-loop-docs`):

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

- **GIVEN** tip after this change applies
- **WHEN** an operator opens `long-horizon-swarm/HARNESS.md`
- **THEN** Drove / Horizon / CAO / Herd / Heavilifter / Planner / Nightly Audit duties match the mapping above
- **AND** dual orch is forbidden
- **AND** Grok primitives `spawn_subagent`, `pstack:`, orch-or-HostStore, and worktree isolation remain named
- **AND** EXTERNAL-LOOP.md is cited without reminting `gbp-external-loop-docs`

#### Scenario: README is not spawn-only

- **GIVEN** `long-horizon-swarm/README.md` after apply
- **WHEN** an operator looks for who runs a standing program
- **THEN** the page names or points at the HARNESS fleet seat bind
- **AND** it still tells the operator to install and enable `tommy-ca/pstack` first
- **AND** it still says this plugin ships no agents

#### Scenario: Propose PR does not refresh product HARNESS

- **GIVEN** Wave-4 propose-only artefacts for `lhs-swarm-economics-refresh`
- **WHEN** the propose PR is reviewed
- **THEN** product `long-horizon-swarm/HARNESS.md` and `README.md` are unchanged in that PR
- **AND** apply tasks remain HOLD until Todd/Horizon go

### Requirement: Lever-first VERIFY on Brief and handoff

Feature: lhs-swarm-economics-refresh
Rule: Named verify-* skill or scripts/verify-*.sh; refuse prose-only

The overlay playbook, standing-orders template, and handoff contract MUST require lever-first VERIFY. For a non-trivial leaf, Brief.VERIFY MUST name a `verify-*` skill or a `scripts/verify-*.sh` path. Overlay MUST refuse to spawn that leaf when VERIFY is prose-only (self-report, "looks good", or an enum with no lever path). Trivial leaves MAY skip with an explicit `skip: lever, <reason>` on the unit. Handoff Verification MUST record the lever path and outcome; the existing enum (`live-ui-verified` / `unit-test-verified` / `type-check-only` / `not-verified`) is not sufficient alone. Nightly Audit Engineer `maintain-verification` cadence MUST be cited as the standing refresh of per-repo levers. Overlay MUST NOT invent LIVE or LIVE_PASS. `scripts/verify-long-horizon-swarm.sh` remains the catalog prove lever for this sibling.

#### Scenario: Non-trivial leaf without a named lever is refused

- **GIVEN** a ready leaf whose Brief.VERIFY is prose only
- **WHEN** the parent would spawn a worker
- **THEN** the overlay refuses to spawn
- **AND** it names the missing `verify-*` skill or `scripts/verify-*.sh` path

#### Scenario: Handoff records the lever

- **GIVEN** a worker or verifier writes `long-horizon/<id>/handoffs/<task>.md` after apply
- **WHEN** Verification is filled
- **THEN** the file names the lever path that ran
- **AND** it records PASS / FAIL / INCONCLUSIVE against that lever
- **AND** INCONCLUSIVE is not a pass

#### Scenario: Nightly Audit cadence is cited

- **GIVEN** standing-orders or playbook after apply
- **WHEN** verification policy is read
- **THEN** Nightly Audit Engineer / maintain-verification is named for lever cadence
- **AND** LIVE / LIVE_PASS is not invented

### Requirement: Blog failure-mode checklist is falsifiable

Feature: lhs-swarm-economics-refresh
Rule: Playbook + standing-orders treat Cursor blog failure modes as refuse/stop checks

After apply, the entry playbook and `references/standing-orders-template.md` MUST include a named checklist that cites https://cursor.com/blog/agent-swarm-model-economics (Wilson Lin, Jul 2026) and treats each failure mode as a falsifiable refuse/stop or drain-incomplete check:

| Failure mode | Falsifiable check |
| --- | --- |
| split-brain | two live or pending nodes share a conceptKey → refuse spawn |
| planner contention | DesignDoc missing owner, or two writers on the same `design-docs/<conceptKey>.md` → refuse |
| merge reconciler | drain on a collision without `coordination-layer` record and `pstack:poteto-agent` reconciler → drain incomplete |
| megafiles | owned file over megafile-loc (default 800) → ISSUES not PASS; spawn decompose |
| ossify | core change without ossify-break DesignDoc reason → refuse |
| review lenses | land without ≥2 lenses including pstack interrogate → refuse land |
| Field Guide | spawn without `field-guide/index.md` → spawn-contract miss |
| model economics | spawn without CostPolicy model bind, or drain without a `spend.tsv` row → incomplete |

The checklist MUST NOT replace the overlay skills that already implement those mechanisms. It MUST keep planner≠worker, CostPolicy, Field Guide, review-lenses, megafile-gate, ossify-break, openspec-intent-flow, and refuse flat-swarm / dual-board / nested-spawn. Arena and interrogate MUST remain pstack cites (do not clone those skill trees into this plugin).

#### Scenario: Checklist is in playbook and standing-orders

- **GIVEN** tip after this change applies
- **WHEN** an operator reads the entry playbook and standing-orders template
- **THEN** both name the eight failure modes above
- **AND** each mode has a refuse/stop or drain-incomplete predicate
- **AND** the Cursor blog URL is cited

#### Scenario: Keep-list and pstack cites survive the refresh

- **GIVEN** overlay skills and playbook after apply
- **WHEN** keep-list and reuse surfaces are inspected
- **THEN** planner≠worker, CostPolicy, Field Guide, review-lenses, megafile-gate, ossify-break, and openspec-intent-flow are still present
- **AND** refuse still names flat-swarm, dual-board (second-board / dual-write), and nested-spawn
- **AND** arena and interrogate are called as pstack leaves, not copied into `long-horizon-swarm/skills/`

### Requirement: SemVer bump and prove lever stay green

Feature: lhs-swarm-economics-refresh
Rule: 1.2.0-long-horizon-swarm.N; verify script + marketplace tests PASS

Apply MUST bump `long-horizon-swarm/plugin.json` version and the matching `.grok-plugin/marketplace.json` `plugins[].version` from `1.1.0-long-horizon-swarm.0` to `1.2.0-long-horizon-swarm.N` (N chosen at apply; first land typically `0` unless that tag already exists). The string MUST remain unique across local siblings and MUST match ADR 0003–0005 (`MAJOR.MINOR.PATCH-<plugin-name>.N`, not CalVer, not `-grokbuild.N`). Existing tags MUST NOT be moved. `scripts/verify-long-horizon-swarm.sh` MUST exit 0 after the refresh (extend the script if new HARNESS/checklist/VERIFY assertions are needed). `python3 tests/test_marketplace.py` MUST PASS. `grok plugin validate ./long-horizon-swarm` MUST PASS. Docs-only apply without installable skill, HARNESS, or lever deltas MUST be rejected.

#### Scenario: Identity bumps together

- **GIVEN** apply for this change
- **WHEN** `plugin.json` and marketplace `plugins[]` for `long-horizon-swarm` are read
- **THEN** both versions equal `1.2.0-long-horizon-swarm.N`
- **AND** no other local sibling shares that version
- **AND** no existing tag was moved

#### Scenario: Prove lever is green

- **GIVEN** the refreshed overlay on the apply branch
- **WHEN** an operator runs `scripts/verify-long-horizon-swarm.sh`
- **THEN** the script exits 0
- **AND** `python3 tests/test_marketplace.py` PASS
- **AND** `grok plugin validate ./long-horizon-swarm` PASS

#### Scenario: Docs-only apply is rejected

- **GIVEN** a Wave-5 candidate that only edits README prose
- **WHEN** apply readiness is judged
- **THEN** the candidate is rejected
- **AND** HARNESS, playbook or standing-orders, lever-first VERIFY, and the SemVer bump are still required

### Requirement: Fleet roles-map and persona cite honesty

Feature: lhs-swarm-economics-refresh
Rule: Spec names exact cites; Drove/eggbot applies box SoT

The change MUST document that Drove (or eggbot under desk policy) applies live cite lines to box SoT. Those updates are **not** required to land inside the tommy-ca/grok-build-plugins git PR. Apply MAY split: gbp git Apply lands overlay + SemVer + OpenSpec merge (Horizon leaf); Drove/eggbot lands roles-map / `fleet-roles.mdc` / personas. Propose MUST NOT claim those box files are already live from OpenSpec prose alone.

`/workspace/fleet-external-agents/roles-map.md` MUST gain a standing-program overlay cite block whose intended content is:

`## Standing program overlay (long-horizon-swarm)`

`When a brief is a standing program (hours/days, spec-as-root, TaskTree), cite overlay skills from tommy-ca/grok-build-plugins long-horizon-swarm (do not clone): planner-worker-split (planner≠worker + CostPolicy); field-guide; review-lenses (≥2 incl pstack interrogate); coordination-layer / megafile-gate / ossify-break; openspec-intent-flow. Arena and interrogate stay pstack cites. Lever-first VERIFY: Brief.VERIFY MUST name verify-* skill or scripts/verify-*.sh. Fleet seats per EXTERNAL-LOOP.md: Drove tick, Horizon single-change, CAO parallel, Herd session herdr, Heavilifter recovery. Dual orch forbidden.`

`~/.cursor/rules/fleet-roles.mdc` MUST carry the same cite as a comment twin (alwaysApply map stays the role-key table). Agent personas for Drove, Horizon, Planner, CAO, Herd, Heavilifter, and Nightly Audit MUST each include a one-line cite of the overlay when a standing program is armed.

#### Scenario: Required cite content is named in OpenSpec

- **GIVEN** propose artefacts for `lhs-swarm-economics-refresh`
- **WHEN** apply readiness for fleet roles-map is checked
- **THEN** tasks/spec name the standing-program overlay heading
- **AND** required skill cites include planner-worker-split, field-guide, review-lenses, megafile-gate, ossify-break, openspec-intent-flow
- **AND** lever-first VERIFY and EXTERNAL-LOOP seats are named
- **AND** arena/interrogate stay pstack cites

#### Scenario: Box SoT owner is Drove/eggbot not the gbp propose PR

- **GIVEN** Wave-4 propose PR for this change
- **WHEN** roles-map / persona apply ownership is assigned
- **THEN** Drove/eggbot owns the live edit of `/workspace/fleet-external-agents/roles-map.md`, `~/.cursor/rules/fleet-roles.mdc`, and the named personas
- **AND** the gbp git propose PR is not required to contain those files
- **AND** done-claims for the cites wait until the box SoT lines exist (Metadata verify)

### Requirement: Propose PR is OpenSpec-only

Feature: lhs-swarm-economics-refresh
Rule: Wave-4 lands artefacts; no product plugin edits; no remint

Wave-4 MUST add only `openspec/changes/lhs-swarm-economics-refresh/` artefacts. It MUST NOT edit product `long-horizon-swarm/` files, marketplace versions, or `scripts/verify-long-horizon-swarm.sh`. It MUST NOT remint `thermos-grok-port` or `gbp-external-loop-docs`. It MUST NOT clone arena/interrogate. Apply remains HOLD until Todd/Horizon go. OpenSpec `validate --type change --strict` MUST PASS on the propose artefacts.

#### Scenario: Propose tree is artefacts only

- **GIVEN** Wave-4 propose-only artefacts for `lhs-swarm-economics-refresh`
- **WHEN** the propose PR diff is reviewed
- **THEN** the only new paths are under `openspec/changes/lhs-swarm-economics-refresh/`
- **AND** `long-horizon-swarm/plugin.json` is still `1.1.0-long-horizon-swarm.0`
- **AND** thermos and gbp-external-loop-docs are not reminted
