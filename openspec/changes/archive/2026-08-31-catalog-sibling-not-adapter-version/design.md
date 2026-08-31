## Context

How: catalog is an index (ADR 0001). Three local plugins, one git tag namespace. `grok plugin tag` cannot tag a subtree. Shared `1.0.0-grokbuild.0` collided (`9195505` forked to name-in-version). pstack is url+sha and is tagged in tommy-ca/pstack. Its marketplace version string is a display copy of that grammar, not a catalog tag.

Investigation: ADR 0003/0004 lock the sibling grammar and reject CalVer. They do not say "must not copy pstack's grokbuild token onto locals." Copying it back is the original collision.

## Goals / Non-Goals

**Goals:** Spec and tests forbid grokbuild on local sibling versions. Name the marketplace pstack row as display-only.

**Non-Goals:** Retag. Version bump. Catalog-root plugin.json. Tagging pstack from this repo. Clearing GitHub Latest.

## Decisions

Keep `MAJOR.MINOR.PATCH-<plugin-name>.N` on locals. Forbid `-grokbuild.N` on those folders. Marketplace pstack version may stay `0.14.5-grokbuild.4`.

## Risks / Trade-offs

Two grammars in one marketplace.json. The url+sha row is a pin, not a sibling. Mixing them is the membership model.

## Migration Plan

Land spec and tests. Do not retag `v1.0.0-<name>.0`.

## Open Questions

None.
