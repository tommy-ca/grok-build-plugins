### Long-horizon swarm

**You own the spec and the tree. You never write product code.** Overlay on Orchestrate. Use when the work is a standing program that must run for hours or days, the user steps away, or the user names long-horizon swarm / swarm economics / spec-as-root. One-session tasks stay on Autonomous run. Short fan-out stays on `/swarm`.

Open a todolist with Orchestrate steps first, then the steps below copied in verbatim. A skipped step stays listed with `skip: <reason>`.

This playbook calls overlay skills and pstack leaves by name. It does not replace them.

If `openspec/changes/<id>/` exists, treat it as the Spec-lowering pipeline via **openspec-intent-flow**. Artifact order is proposal -> (specs, design) -> adr -> tasks. Refuse worker spawn until tasks.md exists. GIVEN/WHEN/THEN scenarios are Brief.ACCEPTANCE.

OverlayGate is refuse or run. Parse `grok inspect --json` `.skills[].name` at this boundary.

1) Frame the Spec. Prefer an OpenSpec intent-driven change folder (`openspec/changes/<id>/`) via the **openspec-intent-flow** skill. Write proposal.md first. Specs and design may proceed in parallel. adr.md before tasks.md. No blob spec fallback. State the done predicate as something countable. If one agent could finish inside the session budget, `skip: route to Autonomous run` and stop.
2) Confirm the host runtime. Open the trail via show-me-your-work. Write standing orders from `references/standing-orders-template.md` before any spawn. Prefer `bun` to run pstack `skills/poteto-mode/scripts/orch/orch.ts`. If bun is missing, try `node`. If the CLI runs, `orch init --store long-horizon/<id>` is the overlay unit board for the rest of this playbook. If it cannot run (Grok chat sandbox, or node-only host that cannot execute this bun CLI), skip orch. Seed HostStore frontier and extras only. Before any `spawn_subagent`, seed Field Guide via the **field-guide** skill under `long-horizon/<id>/`. Create `design-docs/` and `spend.tsv` there as extras. Write `openspec/config.yaml` with `schema: intent-driven` when using OpenSpec. Do not invent a third store.
3) Lower the accepted artifacts into a TaskTree. Each `tasks.md` box becomes a TaskNode. `conceptKey` equals the OpenSpec capability id. Role and model come from **planner-worker-split**. Two live nodes must not share a conceptKey. Contested decomposition or a one-way artifact shape runs the pstack `arena` skill (Phases A–F) before implementer spawn; write the synthesis note under `long-horizon/<id>/arena/<unit-id>.md`. Uncontested nodes list `skip: arena, <reason>` on the unit. Refuse to spawn if tasks.md exists without adr.md.
4) Write the throughput checkpoint as four todo items (Feature step 3). Blocking first steps. Independent workstreams. Shared mutable state. Smallest safe decomposition.
5) Author a Brief per ready leaf using the Orchestrate brief template. Fields are GOAL, SCOPE, CONTEXT, ACCEPTANCE, VERIFY, TIMEBOX, FORBIDDEN, REPORT, STANDING, FIELD_GUIDE. Acceptance lines are the Gherkin scenarios for that capability, copied not paraphrased. Inject `field-guide/index.md` and standing orders verbatim. Missing Brief fields are a refuse-to-spawn condition.
6) Spawn workers with exclusive write targets.

```
spawn_subagent
  prompt: Brief
  description: <3-5 words>
  subagent_type: pstack:feature
  background: true
  isolation: worktree
  model: <toml key feature, or grok-4.6, omit if inherit-parent>
```

Spawn verifiers `pstack:independent-verifier`. Planner is this session. Depth 1. Recurse is parent-owned units. Children do not call `spawn_subagent`. Use `/swarm` only for short coverage or race slices inside a leaf.
7) Drain through Orchestrate. If Field Guide `index.md` is missing, that is a spawn-contract miss. Do not invent a first index here. On every drain: classify inbox pointers, record a SpendRow, run **coordination-layer** `record`, apply **megafile-gate**, apply **ossify-break** if core files are frozen, reconcile DesignDoc collisions with `pstack:poteto-agent`.
8) Stacked review before land. Run **review-lenses** (at least 2: output-only, codebase-only, plus live if the unit is behavioral). Include pstack `/interrogate` as one named view. Do not auto-apply findings. Single-family harnesses record `family: same-degraded`. Interrogate alone does not meet the two-lens bar. Write the ledger row on the board step 2 selected (orch store, else HostStore). CI green is not a verdict.
9) Land continuous via `playbooks/shipping.md` / stacker rules. Advance the same board's frontier only on merge or new head SHA. New SHA voids the ledger row.
10) Close. Confirm every Gherkin scenario on the real artifact. Archive the OpenSpec change (`openspec archive <slug>` or merge deltas into `openspec/specs/` by hand and move the folder to `changes/archive/`). Audit the trail via show-me-your-work. Encode recurring corrections into field-guide AND structure. Leave the selected board intact. After a session restart, re-read the OpenSpec change folder, `long-horizon/<id>/`, and the selected board. In-session children are gone. Respawn from stored briefs.

**Reply:** change folder path, done predicate, tree size, spend split, landed units with verdicts, open gates, field-guide index length vs budget, archive path.

#### OpenSpec intent-driven gates

When the user names OpenSpec, `/opsx`, or intent-driven flows, or `openspec/config.yaml` exists, run these gates on top of the steps above. Call the **openspec-intent-flow** skill.

0. **Explore (optional).** `/opsx:explore` is Investigation / how / prototype. No files.

P. **Propose.** Write `openspec/changes/<slug>/` artifacts in order: proposal.md → (specs deltas || design.md) → adr.md → tasks.md. Capabilities listed in the proposal are conceptKeys. Stop unless the user also asked to apply.

A. **Apply.** Lower each `tasks.md` checkbox to a Unit. Each `#### Scenario` becomes a Brief.ACCEPTANCE line. Spawn workers only after adr.md and tasks.md exist. `openspec/specs/` stays read-only.

U. **Update.** Implementation surprises revise the change-folder artifacts and Field Guide, not living specs.

R. **Archive.** After ledger-verified land: merge deltas into `openspec/specs/`, move the change folder to `openspec/changes/archive/`, curate Field Guide, encode lessons.

Binding table: `references/openspec-binding.md` in this plugin.

#### Article loop (swarm economics)

Map from https://cursor.com/blog/agent-swarm-model-economics onto the steps above. Do not add a second playbook.

| Article | Playbook | Artifact |
| --- | --- | --- |
| 1 Planner receives goal | step 1 | OpenSpec proposal / spec |
| 2 Decompose into tree | step 3 | tasks.md → TaskTree |
| 3 Delegate | step 5 | Brief + CostPolicy |
| 4 Worker executes | step 6 | exclusive worktree |
| 5 Commit via VCS | step 6–7 | git SHA on the unit |
| 6 Collision, neutral resolver | step 7 reconciler | coordination-layer |
| 7 Field Guide | step 2 seed, drain curate | field-guide/index.md |
| 8 Review lenses | step 8 | selected board ledger |
| 9 Recurse | more parent-owned units | this session, not a child planner |

Skip custom VCS. Skip sibling chat. SpendRow on every drain.
