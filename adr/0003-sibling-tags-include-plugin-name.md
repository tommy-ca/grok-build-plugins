# Sibling git tags include the plugin name

- Status: accepted
- Date: 2026-08-31

## Context

This catalog is one git repository. `grok plugin tag` names the tag `v` plus `plugin.json` version. Local siblings used to share `1.0.0-grokbuild.0`, so they would fight over `v1.0.0-grokbuild.0`. pstack is a remote sha pin and is tagged in tommy-ca/pstack, not here. The catalog root is not a plugin.

## Decision

Local sibling versions MUST be `MAJOR.MINOR.PATCH-<plugin-name>.N`. Those strings MUST be unique in this repo. `scripts/release.sh` tags only local marketplace rows. It MUST NOT tag pstack. It MUST NOT add a catalog-root `plugin.json`.

## Consequences

Independent sibling bumps cannot collide. Tags point at catalog HEAD. GitHub Releases for siblings use `--latest=false` so they do not steal Latest from each other. Marketplace `plugins[].version` must match `plugin.json`.
