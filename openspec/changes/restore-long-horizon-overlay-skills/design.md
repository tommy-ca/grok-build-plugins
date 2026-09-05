## Context

Archived `add-long-horizon-swarm-plugin` shipped a one-skill collapse. Zip 0.1.1 has nine skills. Seven of them are overlay gates. Two are harness (`long-horizon-swarm-grok-adapter`, Cursor rules). The operator asked to restore zip overlay content as grok-native files. pstack ADR 0006 still forbids a second orch board.

## Goals / Non-Goals

**Goals:** Ship the zip overlay skill set under `long-horizon-swarm/skills/`. Entry playbook is the zip 10-step TaskTree bound to `spawn_subagent` and HostStore. OpenSpec intent flow is a skill. Version `1.1.0-long-horizon-swarm.0`.

**Non-Goals:** Cursor `.cursor-plugin`. Grok-chat adapter. Nested planner spawn. Patching pstack ADR 0008 in tommy-ca/pstack. New catalog ADR. This overlay may run orch when bun or node exists.

## Decisions

1. **Restore seven overlay skills.** Port from `/tmp/lhs-import/pstack-long-horizon-swarm/skills/` with top-level `disable-model-invocation: true`. Drop nested `metadata.cursor`.
2. **Keep HARNESS.md.** Do not restore `GROK-CHAT.md` or `references/grok-bindings.md`.
3. **Extras stay under `long-horizon/<id>/`.** Field Guide, spend.tsv, handoffs, design-docs. When bun or node exists, `orch init --store long-horizon/<id>` is the unit board. When neither exists, HostStore is the board.
4. **Playbook is ten steps plus OpenSpec gates.** Step 4 is Feature throughput. Recurse is parent-owned units. Call overlay skills by name.
5. **No new ADR.** ADR 0002 still covers the sibling.

## Risks / Trade-offs

- [Eight inspectable skill names] -> Operator asked for zip overlay modules. Tests lock the set so collapse cannot silently return.
- [pstack ships `scripts/orch` with `orch init`] -> Overlay runs it when bun or node is on PATH. Skip only when both are missing (Grok chat). pstack ADR 0008 still forbids Grok core playbooks from using orch. This overlay is the optional exception with a runtime probe.
- [Grok-chat leftover] -> Keep banning `chatroom_send`. Do not treat `orch init` as the same class of leftover.

## Migration Plan

Bump plugin and marketplace versions together. Operators reinstall or pull the sibling. New session after enable.

## Open Questions

None that block apply.
