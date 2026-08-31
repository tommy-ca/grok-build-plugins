# Local sibling identity is plugin name, not grokbuild

- Status: accepted
- Date: 2026-08-31

## Context

ADR 0003 requires `MAJOR.MINOR.PATCH-<plugin-name>.N` because local siblings share one git tag namespace. Shared `1.0.0-grokbuild.0` collided on `v1.0.0-grokbuild.0`. pstack uses `-grokbuild.N` as adapter lineage in a single-plugin repo. Specs did not say local siblings MUST NOT copy that token. Marketplace pstack `plugins[].version` is a display copy of pstack's grammar for a url+sha pin, not a catalog tag.

## Decision

Local sibling versions MUST remain `MAJOR.MINOR.PATCH-<plugin-name>.N`. They MUST NOT use `-grokbuild.N`. Unifying with tommy-ca/pstack is forbidden. The marketplace pstack row MAY keep pstack's grokbuild version string. Existing tags MUST NOT be moved.

## Consequences

Name-in-version stays the primary key for locals. Copying pstack's grokbuild token would recreate the original collision. pstack remains tagged in tommy-ca/pstack.
