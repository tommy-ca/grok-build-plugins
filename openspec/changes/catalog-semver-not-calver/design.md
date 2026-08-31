## Context

ADR 0003 already requires name-in-version. Investigation rejected CalVer: same-day collision, YYYY-as-major confusion, GitHub Latest theft would get worse. SemVer build metadata `+date` is ignored for precedence.

## Goals / Non-Goals

**Goals:** Spec and tests forbid date-as-key.

**Non-Goals:** Retag. Version bump. Clearing GitHub Latest.

## Decisions

Keep `1.0.0-<plugin-name>.N`. Date stays on the Release.

## Risks / Trade-offs

Hyphen is SemVer prerelease, not “unstable.” That is the cost of stuffing a package name into `grok plugin tag`’s one-namespace format.

## Migration Plan

Land spec and tests. Do not retag `v1.0.0-<name>.0`.

## Open Questions

None.
