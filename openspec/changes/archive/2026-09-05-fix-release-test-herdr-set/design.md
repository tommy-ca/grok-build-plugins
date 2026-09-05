## Context

Tip `c079068` already lists `pstack-herdr` in `.grok-plugin/marketplace.json` and ships `pstack-herdr/plugin.json` (`0.1.0-pstack-herdr.0`). Probe `test_local_versions_are_unique_and_named` fails because the expected set omits `pstack-herdr`. In-force ADRs 0001–0006 already allow another grok-native sibling; this change is follow-through, not a new architecture.

## Goals / Non-Goals

**Goals:** Make `python3 tests/test_release.py` PASS by including `pstack-herdr` in the expected local set. Keep OpenSpec version-scenario GIVENs honest with that five-name set.

**Non-Goals:** Reminting herdr skills/mdc. Extending marketplace OpenSpec catalog-list / overlay requirement (owned by `openspec-marketplace-pstack-herdr`). C1 README install / operator-docs. Inventing `grok` CLI on the review box. Pending `claude`/`codex` herdr kinds.

## Decisions

1. **Smallest Static fix.** Edit only the expected-set assertion in `tests/test_release.py` (plus matching OpenSpec GIVEN lists under version/identity requirements). Do not rewrite release script or workflow tests.
2. **Expected set is explicit.** Keep the hardcoded frozenset style already used for the four siblings; add `"pstack-herdr"`. Do not invent a dynamic derive-from-marketplace helper this wave.
3. **No new ADR.** ADR 0002 already covers sibling folders; ADR 0003–0005 cover SemVer namespace rules that herdr already satisfies (`0.1.0-pstack-herdr.0`).
4. **Soft-before OpenSpec marketplace delta.** Prefer apply order: this change → `openspec-marketplace-pstack-herdr`. Propose drafts may land in parallel.

## Risks / Trade-offs

- [OpenSpec catalog-list still names four locals until #2] -> Acceptable under A1 SPLIT; lever green is the done bar here.
- [Hardcoded set drifts again on next sibling] -> Later wave may derive from marketplace; out of scope.

## Migration Plan

Apply on a branch from tip. Run `python3 tests/test_release.py`. Validate this change `--strict`. STOP for Todd-go before merge/archive. No tag move.

## Open Questions

None that block propose. C1 remains Consider/Defer.
