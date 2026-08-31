## Why

Sibling tags are SemVer with the plugin name in the prerelease so one git repo cannot collide. A later agent could replace that with CalVer or a ship date. Same-day siblings would fight over one tag again. Date is already on the GitHub Release.

## What Changes

- Specs say uniqueness is `MAJOR.MINOR.PATCH-<plugin-name>.N`, not a calendar.
- Tests reject a date-only version. No retag. No version bump.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `grok-build-marketplace`: local sibling versions stay SemVer plus plugin name. CalVer is not the tag identity.

## Impact

Live marketplace spec, ADR 0004, `tests/test_release.py`, README. Not existing tags. Not pstack’s tag namespace.
