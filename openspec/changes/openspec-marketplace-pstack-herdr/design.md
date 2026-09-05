## Context

Probe S7 LAG: `openspec validate --all --strict` passes on tip, but marketplace OpenSpec text lacks `pstack-herdr` while SPEC.md and marketplace.json already list it. Arena A2 locked **EXTEND** `grok-build-marketplace` only — same pattern as archived `2026-09-05-add-long-horizon-swarm-plugin`. PR #5 already shipped skills/mdc; this change is OpenSpec follow-through, not a remint.

In-force ADRs 0001–0006 constrain: catalog is an index; siblings at root; SemVer `MAJOR.MINOR.PATCH-<name>.N`; no nested `pstack/`.

## Goals / Non-Goals

**Goals:** OpenSpec lists `./pstack-herdr`. OpenSpec carries an overlay requirement that mirrors tip SPEC (local path; arena/I1/prove-it local; implement after Act-on; anti N×agy). Validate `--strict` PASS for this change.

**Non-Goals:** Companion `pstack-herdr` capability. Editing tip product plugin files this wave (already shipped). C1 README/operator-docs. Release-test expected-set edit (owned by `fix-release-test-herdr-set`). Inventing LIVE herdr kinds. Claiming apply-done for #5.

## Decisions

1. **Extend marketplace only.** One ADDED overlay requirement + MODIFIED catalog-list and cursor-layout sibling prose. No new `openspec/specs/pstack-herdr/`.
2. **Mirror SPEC, do not remint philosophy.** Overlay scenarios stay at catalog/router contract level already in SPEC.md + shipped mdc. Do not paste full skill trees into OpenSpec.
3. **Anti N×agy + local arena/I1 as MUST.** Encode as scenarios so archive merge cannot drop the harden invariants.
4. **Soft-after release-test fix.** Prefer apply after `fix-release-test-herdr-set` is green; propose may proceed in parallel.
5. **No new ADR.** ADR 0002 already admits another sibling; herdr is that shape.

## Risks / Trade-offs

- [SPEC ahead of OpenSpec until apply/archive] -> Propose-only this wave; archive after Todd-go apply.
- [Overlap with #1 version GIVENs] -> #1 owns version/identity GIVEN updates; this change owns catalog-list + overlay + cursor-layout prose to avoid dual MODIFIED of the same requirement headers.
- [Pending herdr kinds] -> Scenarios say “ready” kinds only; do not name `claude`/`codex` as live.

## Migration Plan

After Todd-go: apply OpenSpec delta (merge into main `openspec/specs/grok-build-marketplace/spec.md` via archive flow). Re-run `openspec validate --all --strict`. No marketplace.json edit required (already lists herdr). No tag move.

## Open Questions

None that block propose. C1 remains Consider/Defer unless Horizon/Todd promote.
