## Why

Tip SPEC.md and `.grok-plugin/marketplace.json` already include `pstack-herdr`, but OpenSpec `grok-build-marketplace` still names only four local siblings and has no overlay requirement mirroring the shipped SPEC “pstack-herdr is an optional pstack overlay” contract. Intent-driven tip is lagging the product.

## What Changes

- Extend OpenSpec `grok-build-marketplace` only: list `./pstack-herdr` beside other local siblings.
- ADDED requirement mirroring SPEC overlay MUST/WHEN: optional pstack overlay; arena / I1 / prove-it stay **local**; implement **after Act-on** via ready herdr kinds; anti N×agy fake arena.
- No companion top-level `pstack-herdr` OpenSpec capability (A2 EXTEND lock).
- No remint of PR #5 philosophy into a new ADR. No C1. No invent of pending `claude`/`codex` kinds. No grok CLI env Act-on.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: catalog lists `./pstack-herdr`; ADDED overlay requirement; sibling-layout prose includes herdr as a grok-native local port.

## Impact

`openspec/specs/grok-build-marketplace/spec.md` after archive merge. Soft-after `fix-release-test-herdr-set` preferred for apply (lever green first); propose drafts may parallel. Not `tommy-ca/pstack`. Not C1.
