## Context

ADR 0002 already allows sibling folders at catalog root. Zip 0.1.1 is a Cursor pack plus a Grok-chat adapter (`chatroom_send`, `/home/workdir`, `orch init`). Live pstack already owns Orchestrate, swarm, arena, interrogate, and host-owned durable state (pstack ADR 0006). Arena picked the collapsed tommy-mode shape over an eight-skill tree. Judge totals 12 vs 10.

## Goals / Non-Goals

**Goals:** Ship `long-horizon-swarm` as a skills-only grok plugin in this catalog. Overlay on Orchestrate. Keep pstack a remote pin.

**Non-Goals:** Copying poteto-mode, arena, interrogate, or swarm. Overlay agents. Hooks. `commands/`. Editing `tommy-ca/pstack`. A second orch board. Nested planner spawn. Grok-chat adapter.

## Decisions

1. **Catalog sibling named `long-horizon-swarm`.** Not `pstack-long-horizon-swarm`. Slash, skill, and plugin share one kebab. Version `1.0.0-long-horizon-swarm.0`.
2. **One skill plus one playbook.** Overlay gates live in the playbook. Spec-as-root, planner vs worker, Field Guide, stacked review, megafile, ossify. Pass-through zip skills are deleted.
3. **Grok Build spawn.** Parent uses `spawn_subagent` with `pstack:<role>`. Depth 1. Recurse is more parent-owned units. Planner is this session.
4. **Three stores.** HostStore is Orchestrate durable-state by name. Overlay extras live at `long-horizon/<id>/` in the target repo (Field Guide, spend.tsv). OpenSpec change folder is the spec pipeline. Extras are not the board.
5. **No new ADR.** ADR 0002 covers siblings.
6. **UPSTREAM** records zip `pstack-long-horizon-swarm-0.1.1.zip` sha256 `becdfa7f0cd3a0d3550fb2301da61ffb64e333188e04c66ce67cc7f9e7b4056b`.

## Risks / Trade-offs

- [User must invoke `/long-horizon-swarm`] -> Do not paste a trigger into pstack. Optionality stays.
- [Single-family Grok seats] -> Stacked review records `family: same-degraded`. Interrogate alone still fails the two-lens bar.
- [Archive vs Field Guide] -> Extras stay under `long-horizon/<id>/`, not inside the OpenSpec change folder.

## Migration Plan

Install pstack, then `long-horizon-swarm --trust`, enable both from a host shell, start a new session. Invoke `/long-horizon-swarm`.

## Open Questions

None that block apply. A later pstack trigger bullet is out of scope.
