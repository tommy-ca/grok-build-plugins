# ADR Review Manifest

- Status: completed
- Review date: 2026-09-12

## Review Summary

ADR review completed for this change. No new durable repo-root ADR. Packaging and SemVer follow in-force catalog ADRs 0001–0006. Change-local locks: **A1** plugin id/dir `thermos`; **A2** full poteto bind (arena, interrogate, swarm/long-horizon handoff, lever VERIFY); **A3** sole NEW Act-on `thermos-grok-port` (cite-only for closed gbp #1–#14). Upstream cursor/plugins thermos is MIT source for skills/agents intent; Grok HARNESS replaces Cursor Task as sole API.

## In-Force ADRs Reviewed

- `adr/0001-catalog-is-index-not-plugin-monorepo.md` — catalog is index; do not nest pstack; thermos is sibling path or own url+sha, not a monorepo nest
- `adr/0002-grok-native-sibling-plugins.md` — grok-native siblings at catalog root (`./thermos`)
- `adr/0003-sibling-tags-include-plugin-name.md` — tag/version includes `thermos`
- `adr/0004-semver-not-calver-for-sibling-tags.md` — `MAJOR.MINOR.PATCH-thermos.N`
- `adr/0005-sibling-not-adapter-version.md` — not `-grokbuild.N`
- `adr/0006-cursor-layout-does-not-nest-pstack.md` — Cursor sibling layout does not put `pstack/` here; thermos joins grok-native siblings only

## New Durable ADRs Created

- None — no major durable architectural decision beyond applying 0001–0006 to a new sibling port.

## Arena / Act-on locks named

- **A1** thermos id / dir `thermos`
- **A2** full poteto (arena + interrogate + swarm + lever VERIFY)
- **A3** NEW Act-on `thermos-grok-port` only — no remint closed gbp leaves
