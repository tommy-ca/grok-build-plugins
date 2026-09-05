## Task graph

```
1.tests-red --> 2.overlay-skills
1.tests-red --> 3.playbook-tasktree
2.overlay-skills --> 4.refs-glossary
3.playbook-tasktree --> 4.refs-glossary
4.refs-glossary --> 5.version-docs
5.version-docs --> 6.prove
```

## 1. Tests red

- [x] 1.1 Fail then pass. Tests expect overlay skill dirs `field-guide`, `planner-worker-split`, `review-lenses`, `coordination-layer`, `megafile-gate`, `ossify-break`, `openspec-intent-flow`, and `long-horizon-swarm`. Version `1.1.0-long-horizon-swarm.0`. Playbook names ten steps and `openspec-intent-flow`. Still no grok-adapter or `chatroom_send`. `orch init` may appear only as Codex compatibility, not as a Grok step.

## 2. Overlay skills

- [x] 2.1 Port the seven zip overlay skills grok-native. Top-level `disable-model-invocation: true`. Extras path `long-horizon/<id>/`. HostStore is the board. No Cursor metadata. No Grok-chat spawn.

## 3. Playbook TaskTree

- [x] 3.1 Rewrite `playbooks/long-horizon-swarm.md` as ten numbered steps plus OpenSpec gates. Call overlay skills by name. `spawn_subagent` `pstack:<role>`. Recurse is parent-owned units. Seed Field Guide before spawn.

## 4. Refs and glossary

- [x] 4.1 Add `GLOSSARY.md`, `docs/REQUIRES.md`, `references/handoff-contract.md`, `references/openspec-binding.md`, `references/standing-orders-template.md`. No banned leftover strings.

## 5. Version and docs

- [x] 5.1 `plugin.json` and marketplace version `1.1.0-long-horizon-swarm.0`. README lists overlay skills. SPEC and living spec match the change delta.

## 6. Prove

- [x] 6.1 `python3 tests/test_release.py`. Overlay `test_marketplace` functions. `grok plugin validate ./long-horizon-swarm`. `openspec validate restore-long-horizon-overlay-skills --type change --strict`.

## 7. Orch bind

- [x] 7.1 Update HARNESS and REQUIRES. Grok HostStore. pstack `scripts/orch/orch.ts` is Codex (`orch init`). Overlay playbook does not run that CLI. Tests drop a global ban on the substring `orch init`. Living spec and SPEC match.

## 8. Arena HostStore pick

- [x] 8.1 Playbook step 2 probes bun then node. `orch init` when either exists. Skip orch on Grok chat (no bun, no node). Overlay ships no `scripts/orch`.
