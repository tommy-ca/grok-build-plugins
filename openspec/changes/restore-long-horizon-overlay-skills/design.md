## Context

Archived `add-long-horizon-swarm-plugin` shipped a one-skill collapse. Zip 0.1.1 has nine skills. Seven of them are overlay gates. Two are harness (`long-horizon-swarm-grok-adapter`, Cursor rules). The operator asked to restore zip overlay content as grok-native files. pstack ADR 0006 still forbids a second orch board.

## Goals / Non-Goals

**Goals:** Ship the zip overlay skill set under `long-horizon-swarm/skills/`. Entry playbook is the zip 10-step TaskTree bound to `spawn_subagent` and HostStore. OpenSpec intent flow is a skill. Version `1.1.0-long-horizon-swarm.0`.

**Non-Goals:** Cursor `.cursor-plugin`. Grok-chat adapter. Invoking pstack `scripts/orch/orch.ts` on Grok. Nested planner spawn. Patching pstack ADR 0008. New catalog ADR.

## Decisions

1. **Restore seven overlay skills.** Port from `/tmp/lhs-import/pstack-long-horizon-swarm/skills/` with top-level `disable-model-invocation: true`. Drop nested `metadata.cursor`.
2. **Keep HARNESS.md.** Do not restore `GROK-CHAT.md` or `references/grok-bindings.md`.
3. **Extras stay under `long-horizon/<id>/`.** Field Guide, spend.tsv, handoffs, design-docs. HostStore remains the board. Rewrite zip `orchestrate/<slug>/` and orch board filenames out of shipped files.
4. **Playbook is ten steps plus OpenSpec gates.** Step 4 is Feature throughput. Recurse is parent-owned units. Call overlay skills by name.
5. **No new ADR.** ADR 0002 still covers the sibling.

## Risks / Trade-offs

- [Eight inspectable skill names] -> Operator asked for zip overlay modules. Tests lock the set so collapse cannot silently return.
- [pstack ships `scripts/orch` with `orch init`] -> Grok playbooks still must not invoke it (pstack ADR 0008). Overlay HARNESS and REQUIRES name it as Codex compatibility. Zip Cursor `orch init` stays out of the Grok step list.
- [Grok-chat leftover] -> Keep banning `chatroom_send`. Do not treat `orch init` as the same class of leftover.

## Migration Plan

Bump plugin and marketplace versions together. Operators reinstall or pull the sibling. New session after enable.

## Open Questions

None that block apply.
