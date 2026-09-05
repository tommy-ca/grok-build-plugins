---
name: ossify-break
description: License an intentional core break so agents do not ossify around untouchable files. Use when the tree avoids a core module.
disable-model-invocation: true
---

# Ossify break

Agents learn to avoid core files because they collide. That freezes a bad shape.

1. Planner decides the core patch is required and writes the reason in the DesignDoc under `long-horizon/<id>/design-docs/<conceptKey>.md` or OpenSpec `design.md`.
2. One worker patches the core and names the new invariant in that DesignDoc. Prefer making the invariant unrepresentable instead of leaving a comment **no-comments** would strip.
3. A compile or typecheck wave is the propagator. Failures become parent-owned units.
4. This is **outcome-oriented-execution** plus **migrate-callers-then-delete-legacy-apis**. It is not a license to break the spec.
