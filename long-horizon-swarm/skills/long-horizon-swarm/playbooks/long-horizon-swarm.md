### Long-horizon swarm

**You own the spec and the tree. You never write product code.** Overlay on Orchestrate. Use when the work is a standing program that must run for hours or days, the user steps away, or the user names long-horizon swarm / swarm economics / spec-as-root. One-session tasks stay on Autonomous run. Short fan-out stays on `/swarm`.

Copy poteto-mode `playbooks/orchestrate.md` steps into the todolist first. Then copy the gates below. A skipped gate stays listed with `skip: <reason>`.

OverlayGate is refuse or run. Parse `grok inspect --json` `.skills[].name` at this boundary. Trust OverlayRun inside the gates.

This playbook adds overlay policy. It does not replace Orchestrate drain, frontier, or land.

#### Gate Spec

OpenSpec is mandatory. `schema: intent-driven`. Artifact order is proposal, then specs and design in parallel, then adr, then tasks. Capability kebab is conceptKey. Each `#### Scenario` is one Brief.ACCEPTANCE line, copied not paraphrased. Each `tasks.md` checkbox is one parent-owned unit.

Refuse worker spawn until `adr.md` and `tasks.md` exist. Living `openspec/specs/` stays read-only during apply. Propose, then apply, then archive. No blob spec fallback. If the operator does not want OpenSpec, they wanted Orchestrate, not this overlay.

`bindOpenSpec(openspec/changes/<id>/)` yields SpecRoot. Adopt an existing change folder. Do not invent a second spec tree.

Before any `spawn_subagent`, create `long-horizon/<id>/field-guide/` if missing. Seed `index.md` with the goal one-liner, the done predicate, and pointers to surprises, seams, and anti-patterns. If `index.md` exists, adopt it. Drain curates. It does not create the first index.

#### Gate Spawn contract

Planner is this session. Workers implement. CostPolicy reads `~/.grok/pstack-models.toml`.

```
spawn_subagent
  prompt: Brief(GOAL, SCOPE, CONTEXT, ACCEPTANCE, VERIFY, TIMEBOX, FORBIDDEN, REPORT, STANDING, FIELD_GUIDE)
  description: <3-5 words>
  subagent_type: pstack:feature
  background: true
  isolation: worktree
  model: <toml key feature, or grok-4.6, omit if inherit-parent>
```

Verifier uses `pstack:independent-verifier` on a different model when one exists. Reconciler uses `pstack:poteto-agent` and writes conflicts and design only. Short coverage inside a leaf still uses `/swarm` and toml key `swarm-workers`.

ACCEPTANCE is Gherkin copied from scenarios. Inject `long-horizon/<id>/field-guide/index.md` after standing orders. Exclusive write target per unit. Missing Brief fields refuse the spawn.

Parent only. Depth 1. Recurse is parent-owned units. Children do not call `spawn_subagent`. Two live units must not share a conceptKey or exclusive path. A worker that wants to change scope writes BLOCKED and stops.

Isolation `none` only when the unit needs this machine. Do not combine `cwd` with `isolation: worktree`.

#### Gate Drain extras

Classify via Orchestrate. HostStore stays the board.

Then overlay extras under `long-horizon/<id>/` in the target repo.

```
long-horizon/<id>/
  field-guide/index.md
  field-guide/surprises.md
  field-guide/seams.md
  field-guide/anti-patterns.md
  spend.tsv
```

If `index.md` is missing at drain, that is a spawn-contract miss. Do not invent a first index here. Line budget default 80. One curator (the parent). Recurring bullets become structure, then the prose copy is deleted.

Append a SpendRow on every drain. Columns: ts, role, model, tokens, usd, agent_count, unit_id. Tokens may be unknown. Role and model are still required. Do not use a tsv units board.

Megafile default 800 loc. Worker reports ISSUES, not PASS. Parent spawns a decompose unit. The original unit does not keep growing the file.

Ossify is one licensed patch. Planner writes the reason in OpenSpec `design.md` first. One worker patches and names the new invariant. Failures become parent-owned units. Not a license to break the spec.

Design collisions spawn reconciler `pstack:poteto-agent`.

#### Gate Review stack

Pick at least two decorrelated lenses. Default merge-ready set is output-only plus codebase-only. Add live when the unit is behavioral. Add regression when blast radius is more than one module.

Interrogate is one review lens. Call pstack `/interrogate` for that view. Interrogate alone does not meet the two-lens bar. Parent fans out `pstack:independent-verifier` for output-only and codebase-only. Codebase-only walks may use `pstack:how-explorer`.

If both seats are the same family, ledger `family: same-degraded`. Synthesize Act on | Consider | Noted | Dismissed. All-clean is required to land. CI green is an input, not a verdict.

#### Gate Close

Confirm every Gherkin scenario on the real artifact. Merge deltas into `openspec/specs/`. Move the change folder to `openspec/changes/archive/`. Curate Field Guide. Encode recurring corrections into structure. Leave HostStore intact.

After a session restart, re-read the OpenSpec change folder, `long-horizon/<id>/`, and host state. In-session children are gone. Respawn from stored briefs.

**Reply:** change folder path, done predicate, tree size, spend split, landed units with verdicts, open gates, field-guide index length vs budget, archive path.

#### Extra standing-order bullets

Do not clone Orchestrate's list. Add only these.

- Inject `long-horizon/<id>/field-guide/index.md`. Keep it under the line budget.
- Spend row on every drain.
- Megafile 800. Cross it and stop.
- Ossify-break is one licensed patch plus a named invariant.
- ACCEPTANCE is Gherkin copied from scenarios.
- No worker spawn until `tasks.md` and `adr.md` exist.
- Workers write BLOCKED. They do not replan.
- Recurse is parent-owned units. Children do not call `spawn_subagent`.

#### Appendix. Article loop

Map from https://cursor.com/blog/agent-swarm-model-economics onto Orchestrate plus these gates. Not a second playbook.

| Article | Overlay | Artifact |
| --- | --- | --- |
| 1 Planner receives goal | Gate Spec | OpenSpec proposal |
| 2 Decompose into tree | Orchestrate scale plus parent-owned units | tasks.md checkboxes |
| 3 Delegate | Gate Spawn contract | Brief plus CostPolicy |
| 4 Worker executes | `spawn_subagent` `pstack:<role>` | exclusive worktree |
| 5 Commit via VCS | Orchestrate land | git SHA on the unit |
| 6 Collision, neutral resolver | Drain extras reconciler | `pstack:poteto-agent` |
| 7 Field Guide | Gate Spec seed, drain curate | `long-horizon/<id>/field-guide/` |
| 8 Review lenses | Gate Review stack | host ledger |
| 9 Recurse | more parent-owned units | this session, not a child planner |

Skip custom VCS. Skip sibling chat.
