---
name: field-guide
description: >
  Agent-owned stigmergy folder. Use for /field-guide, long-horizon swarm spawn
  injection, or capturing surprises for future agents. Does not replace standing orders.
disable-model-invocation: true
---

# Field Guide

A folder the agents own. `long-horizon/<id>/field-guide/index.md` is injected into every spawn. The only constraint is a line budget. Frozen weights cannot learn mid-run. The guide is how successors inherit surprises.

Builds on show-me-your-work and **principle-encode-lessons-in-structure**.
Does not replace standing orders. Standing orders are constraints. The guide is discovered fact.

## Layout

```
long-horizon/<id>/field-guide/
  index.md          injected prefix. Keep under lineBudget (default 80 lines).
  surprises.md      unexpected behavior, sharp edges
  seams.md          where modules actually join
  anti-patterns.md  things that already failed
```

HostStore is the board. This folder is extras.

## Steps

1. Create the folder if missing. Seed `index.md` with the current goal one-liner, the done predicate, and pointers to the other files. Do this before any `spawn_subagent`.
2. On every spawn, paste `index.md` at the top of the Brief after standing orders.
3. Any agent may append a fact. One fact per bullet. Evidence pointer required (SHA, path, command).
4. At each drain, a single curator (the parent) trims `index.md` to the line budget. Demote stale bullets into the topic files.
5. If the same instruction is written twice, stop. Run **encode-lessons-in-structure**. Turn it into a lint, script, or standing-order line. Delete the prose copy.

## Invariants

- One curator for `index.md`. Topic files are append-mostly.
- No secrets. No raw dumps. Pointers, not payloads (**guard-the-context-window**).
- Index is orientation, not a second spec.
