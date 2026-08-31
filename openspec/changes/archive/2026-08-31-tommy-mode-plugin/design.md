## Context

ADR 0002 already allows sibling folders at catalog root. `tommy-mode` is a personal overlay on `/poteto-mode`. Putting it in pstack would recouple products.

## Goals / Non-Goals

**Goals:** Ship `tommy-mode` as a skills-only grok plugin in this catalog. Keep pstack a remote pin.

**Non-Goals:** Copying poteto-mode playbooks. Agents. Hooks. `commands/`. Editing `tommy-ca/pstack`.

## Decisions

1. **Catalog sibling, not pstack pack.** Same layout as `cli-for-agent`.
2. **One skill.** `skills/tommy-mode/SKILL.md` with `disable-model-invocation: true`.
3. **No new ADR.** ADR 0002 covers siblings.

## Risks / Trade-offs

- [User copy at `~/.grok/skills/tommy-mode`] -> Plugin is source of truth after install. Remove the user copy after enable so skill order does not double-load.

## Migration Plan

Install `tommy-mode --trust`, enable with `grok --sandbox off`, start a new session. Delete `~/.grok/skills/tommy-mode` after the plugin loads.

## Open Questions

None.
