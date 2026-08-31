## Context

How: catalog is an index. One git tag namespace. Shared `1.0.0-grokbuild.0` collides. pstack tags live on tommy-ca/pstack.

Two architect sketches. Per-plugin `./scripts/release.sh <sibling>` is the base. Graft marketplace.json as membership, `--latest=false`, and uniqueness tests. Skip a Python registry module. Skip `--dry-run`. Optional sibling arg. No args walks every local row.

## Goals / Non-Goals

**Goals:** Unique name-in-version tags. Dual-writer Releases. Host-shell grok `--sandbox off` plus git push fallback. Workflow on main before the first tag.

**Non-Goals:** Catalog-root `plugin.json`. Tagging pstack from here. Fail-closed Actions polling. `--force`. grok on the runner. `workflow_dispatch`.

## Decisions

1. **Version is `1.0.0-<plugin-name>.0`.** Uniqueness is in the string. Independent bumps cannot collide.
2. **Membership is marketplace.json.** Local path rows are taggable. url+sha rows are not. pstack drops out as a remote pin.
3. **Public command is `./scripts/release.sh [sibling]`.** One sibling for an independent bump. No args walks all local unique rows.
4. **Copy pstack writers.** `grok --sandbox off plugin tag --push <dir>`, then `git push origin refs/tags/$tag` on `TagLocalUnpushed`, then `gh release view || gh release create --verify-tag --generate-notes --latest=false`.
5. **Actions copies that Release step.** `contents: write`. File-text `tests/test_release.py` only. Do not run `test_marketplace.py` on the runner (it needs grok and an adjacent pstack clone).
6. **ADR 0003** records the tag-namespace rule.

**Alternatives.** Never tag siblings (leaves the collision latent). One catalog-wide version (cannot use grok plugin tag without a root plugin.json). Hardcoded sibling tuple (second membership list).

## Risks / Trade-offs

- [First catalog v* lands with the first workflow] -> Push the feat that adds YAML. Then tag. Do not tag the same second GitHub first sees the workflow.
- [Three Releases steal GitHub Latest] -> `--latest=false`.
- [Tag is whole-repo HEAD] -> accepted. Git cannot tag a subtree.

## Migration Plan

Land unique versions, script, workflow, tests, docs on `main`. Then from a host shell run `./scripts/release.sh`. Confirm `gh run list --workflow=release.yml` is non-empty.

## Open Questions

None.
