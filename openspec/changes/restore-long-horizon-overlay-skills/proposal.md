## Why

The 1.0.0 sibling collapsed zip overlay policy into one skill. Arena picked that for interface depth. The operator audited against zip `pstack-long-horizon-swarm-0.1.1` and rejected the collapse. Zip overlay skills are loadable gates. The shipped tree has no `field-guide`, `planner-worker-split`, `review-lenses`, `coordination-layer`, `megafile-gate`, `ossify-break`, or `openspec-intent-flow`. Those are the overlay. Cursor and Grok-chat harness stay out.

Do not amend archived `add-long-horizon-swarm-plugin`.

## What Changes

- Restore grok-native ports of the seven overlay skills plus glossary, REQUIRES, handoff, OpenSpec binding, standing-order extras.
- Rewrite the entry playbook as the zip 10-step TaskTree, calling those skills by name, with Grok Build spawn and HostStore.
- Bump `long-horizon-swarm` to `1.1.0-long-horizon-swarm.0`.
- Tests lock the skill set. They keep banning `orch init`, `chatroom_send`, `.cursor-plugin`, and the grok-adapter skill.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: overlay sibling ships the zip overlay skill set as grok-native files. Still no agents, hooks, commands, MCP, Cursor pack, or Grok-chat adapter.

## Impact

`long-horizon-swarm/`, marketplace version row, `tests/test_marketplace.py`, `tests/test_release.py`, README, SPEC, living spec. Not `tommy-ca/pstack`.
