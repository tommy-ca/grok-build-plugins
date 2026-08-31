# Sibling tag identity is SemVer plus plugin name, not CalVer

- Status: accepted
- Date: 2026-08-31

## Context

ADR 0003 requires `MAJOR.MINOR.PATCH-<plugin-name>.N`. Calendar versioning was proposed as a friendlier scheme. Same-day sibling releases would collide. YYYY as a SemVer major looks like a breaking bump. GitHub already stores ship day on the Release.

## Decision

Do not migrate sibling versions to CalVer or date-only uniqueness. Keep ADR 0003. Ship day belongs in GitHub Release notes.

## Consequences

Name-in-version stays the primary key. A fourth sibling still cannot share a date stamp. GitHub Latest remains one-per-repo and is not solved by dates.
