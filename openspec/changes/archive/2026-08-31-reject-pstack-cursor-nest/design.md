## Context

Cursor `plugins` is a marketplace. Sibling folders plus `.cursor-plugin/marketplace.json`. README's `plugins/` diagram is the GitHub repo name, not a subdirectory. Live GitHub has `pstack/` at root.

This catalog already copied that index shape for grok-native ports. pstack stays url+sha because grok installs a repo-root `plugin.json` via `tommy-ca/pstack --trust`, and xAI Official already names `pstack` from `cursor/plugins`.

Extracting siblings to their own repos would fix tag-namespace inconsistency. Nesting pstack here would make inconsistency worse and mix Claude/Codex adapters into a grok index. This change records the nest as forbidden. It does not extract.

## Goals / Non-Goals

**Goals:** Spec and docs name why Cursor layout does not mean `pstack/` in this repo.

**Non-Goals:** Adding `pstack/`. Extracting siblings. Retag. Version bump. Changing install to `#pstack`.

## Decisions

Keep ADR 0001 and 0002. Add ADR 0006 so "follow Cursor" cannot reopen the nest. Tests already fail if `pstack/` exists.

## Risks / Trade-offs

One checkout for pstack plus siblings still means two git remotes. That is cheaper than a 400-file catalog clone on every marketplace add, and cheaper than breaking `tommy-ca/pstack`.

## Migration Plan

Land spec, ADR, README, SPEC. Do not move files. Do not retag.

## Open Questions

None.
