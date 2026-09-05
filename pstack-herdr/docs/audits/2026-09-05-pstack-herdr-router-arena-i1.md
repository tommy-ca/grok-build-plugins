# Arena + Interrogate audit: pstack↔herdr router (2026-09-05)

## Intent

Review the pstack→herdr agent mapper and Herd router skills against pstack plugin philosophy (arena, interrogate, poteto-mode, prove-it-works, separate-before-serializing).

## Reviewers (synthetic I1 lenses)

- **Arena lens:** Frame/Fan/Cross-judge/Pick/Graft/Verify; model diversity; separate output paths
- **Interrogate lens:** adversarial signal from model diversity; synthesize verdict; no auto-apply
- **Fleet lens:** herdr for monitor/orch of implement; Grok Bot keeps propose/merge/prove-it

## Act On

1. **Do not substitute arena/I1 with herdr.** Mapping `arena runners` / `interrogate reviewers` to `agy` (or N×agy) fakes diversity. Keep `local`. Herd is not the arena parent.
2. **`hardest tasks` must be `local`.** In pstack-models this key is judgment/instruction-following heavy; routing to workhorse agy skips the judgment model. Flip mapper.
3. **`hillclimb` → `local`.** Iterative judgment loops belong on poteto Task; only concrete implement steps after Act-on use herdr via `feature` / `openspec-apply` / `arena-implement-arm`.
4. **Add `arena-implement-arm`.** Post-Pick/Graft implement of the chosen base may route to herdr — separate from arena runner models.
5. **Swarm via herdr requires N worktrees.** Same path for N agy panes violates separate-before-serializing; skill must require one worktree (or output dir) per arm.
6. **Ordering invariant in skills:** contested design → arena (local) → Act-on → Herd apply; after apply → interrogate (local) → prove-it → eng-lead merge. Herd never owns cross-judge or I1 synthesis.
7. **Bare CLI fallback is not an arena arm.**

## Consider

- When `claude`/`codex` become registry-ready, arena *implement* fan-out across kinds may be useful for generation-bound bakeoffs — still distinct from arena *runner* model panels. Revisit with setup-pstack-herdr-agents; do not pre-write pending kinds.
- Cross-judge stays local forever (readonly judgment).

## Noted

- Interactive agy default + outside-driver are aligned with Todd orch order.
- `prove-it` / `openspec-propose` / `eng-lead-merge` already local — correct.

## Dismissed

- "Route everything through herdr for token savings" — breaks arena/I1 epistemology (model diversity) and fleet merge authority.

## Verdict

Router shape is sound with the Act-on mapper/skill patches above. Herd = implement router + herdr orch; pstack Task = judgment/arena/I1/prove-it.
