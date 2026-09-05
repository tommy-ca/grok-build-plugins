---
name: coordination-layer
description: >
  Interface over git worktrees, the selected-board frontier, ledger, and a reconciler.
  Use for /coordination-layer or when a long-horizon drain must record collisions.
  Does not implement a custom VCS.
disable-model-invocation: true
---

# Coordination layer

An interface. The git adapter is in scope. A custom VCS is not.

Builds on worktrees, the selected unit board, babysit, stacker rules, **principle-separate-before-serializing-shared-state**.

## Interface

```
record(event: commit | conflict | handoff | merge | megafile | ossify)
detectCollisions(path) -> Collision[]
resolve(collision) -> ReconcilerRole task
blockCommit(path, reason)
```

Git adapter:

- worktree per worker exclusive write target (`spawn_subagent` `isolation: worktree`)
- selected-board frontier is the lock token for stack topology
- selected-board ledger keyed by pr+sha is the verification lock
- one stacker per stack may run gt or rebase
- workers never rebase

## Drain hooks

1. On handoff: `record(handoff)`. Write `long-horizon/<id>/handoffs/<task>.md` per `references/handoff-contract.md`.
2. On merge conflict or DesignDoc fork: spawn reconciler `pstack:poteto-agent`. Impartial. Conflicts and design docs only.
3. On megafile (file over the loc threshold, default 800 loc touched by at least 3 live units): `blockCommit`, spawn a decompose worker, do not let new writers in. See **megafile-gate**.
4. On ossification: license one focused patch. See **ossify-break**.

## Invariants

- No third source of truth. Orch store is canonical when bun or node exists. HostStore is canonical when they do not. Overlay extras are not a third board.
- Reconciler may edit conflicts and `long-horizon/<id>/design-docs/` only.
- Custom VCS stays an unimplementable adapter slot.
