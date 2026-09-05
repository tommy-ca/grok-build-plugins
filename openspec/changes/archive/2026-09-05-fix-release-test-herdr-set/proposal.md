## Why

PR #5 shipped `pstack-herdr` as a local marketplace sibling, but `tests/test_release.py` still hard-codes the pre-herdr four-name expected set. The tip release lever is product-red while the catalog already lists `./pstack-herdr`.

## What Changes

- Expand `tests/test_release.py` expected local sibling set to include `pstack-herdr`.
- Align OpenSpec marketplace version-uniqueness scenarios so GIVEN local plugin lists include `pstack-herdr` (same five-name contract the release lever asserts).
- No remint of PR #5 plugin body. No README/operator-docs (C1 deferred). No invent of pending herdr kinds.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: release-test and version-uniqueness scenarios expect five local siblings including `pstack-herdr`.

## Impact

`tests/test_release.py` (apply). OpenSpec delta under this change. Soft-before `openspec-marketplace-pstack-herdr` preferred for apply so the lever is green first. Not `tommy-ca/pstack`. Not C1.
