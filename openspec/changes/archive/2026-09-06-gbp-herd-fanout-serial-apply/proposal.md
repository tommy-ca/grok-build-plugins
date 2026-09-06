## Why

Tip `e3cb0c05` ships `pstack-herdr/skills/herd-with-herdr/SKILL.md` after harden, but tip **lags** the box workflow lead at `/home/box/agent-data/workflows/herd-with-herdr/SKILL.md`. Fleet bottleneck B3: tip interactive orch defaults to single-agent `--wait` loops without an N-arm Parallel fan-out default or journal `class: serial_apply` when choosing one. Box already documents N parallel-band arms (one tree each, join on evidence) and required `serial_apply` journal. Claiming tip already patched because box leads would be dishonest. Arena A1 SPLIT puts this Act-on in P-parallel A beside `gbp-tasks-parallel-bands` (independent write target).

## What Changes

- Sync tip `pstack-herdr/skills/herd-with-herdr/SKILL.md` toward box intent: **N-arm fan-out default** when Horizon/Drove ships N parallel-band briefs; journal `class: serial_apply` when choosing a single agent (one brief | true gate | slot starved).
- Keep arena/I1/prove-it **local** on tip and box — do not route judgment panels to herdr; do not N×agy fake arena.
- Honest lag: box leads; Wave-5 sync **into** plugin sibling; do not claim tip already has fan-out at propose.
- Wave-4 = OpenSpec artefacts only — skill body land Wave-5 after Todd go.

## Capabilities

### New Capabilities

- `herd-fanout-serial-apply`: Tip herd-with-herdr Parallel fan-out default + `serial_apply` journal when single; arena/I1 stay local; honest tip-lag vs box lead; no remint harden; no pending kinds invent; no Drove caps.

### Modified Capabilities

- _(none — prefer ADDED under new capability; tip `grok-build-marketplace` pstack-herdr overlay requirement remains cite-only soft fuel)_

## Impact

OpenSpec propose artefacts only in Wave-4. Wave-5 apply (after Todd go) patches tip `pstack-herdr/skills/herd-with-herdr/SKILL.md` using box workflow as cite fuel (not skill-sync-pack as tip SoT). Merges NEW capability into tip `openspec/specs/herd-fanout-serial-apply/`. Does **not** remint harden ids. Does **not** pre-write pending herdr kinds (`claude`/`codex`) as live routes (B6 park). Does **not** invent Drove caps / LIVE_PASS. P-parallel A with `gbp-tasks-parallel-bands`. Soft-after binding cite remains separate.

## Probe Evidence Record

- Evidence label: `Static`
  - Query: Tip vs box herd-with-herdr Parallel fan-out + serial_apply
  - Path: tip `pstack-herdr/skills/herd-with-herdr/SKILL.md`; box `/home/box/agent-data/workflows/herd-with-herdr/SKILL.md`
  - Command: tip @ `e3cb0c05` — interactive orch loop present; Parallel fan-out section MISSING; serial_apply journal MISSING (S5 / B3). Box has both.
  - Result summary: Tip LAGS box; sync into plugin required.
  - Conclusion: Act-on #2 primary mint; do not claim tip already patched.

- Evidence label: `Metadata`
  - Query: Arena A1 SPLIT + I1 lock
  - Path: `arena/SYNTHESIS.md`; `i1/I1.md`; `i1/change-ids.md`
  - Result summary: A1 SPLIT; Act-on `gbp-herd-fanout-serial-apply` LOCKED P-parallel A (∥ #1).
  - Conclusion: Propose locked id; arena/I1 stay local; no mega Act-on; no remint harden.
