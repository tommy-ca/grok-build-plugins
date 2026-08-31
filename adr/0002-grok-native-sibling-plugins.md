# Grok-native sibling plugins live in this catalog

- Status: accepted
- Date: 2026-08-31
- Supersedes: ADR 0001 "v1 stays pstack only"

## Context

ADR 0001 kept this repo as a remote index and forbade nesting pstack. Grok marketplaces may list local plugin folders (`"./name"`) or remote `url` plus sha. Cursor uses sibling plugin dirs at repo root. The grok docs example uses `./plugins/gdrive`. Nesting pstack as `plugins/pstack` remains a footgun.

Two grok-native ports earned a place. `agent-compatibility` and `cli-for-agent`. They are not pstack. They should not live in tommy-ca/pstack.

## Decision

Keep pstack as a pinned remote `url` plus sha. Add grok-native plugins as sibling folders at the catalog root (`agent-compatibility/`, `cli-for-agent/`). List them with local sources. Do not create a `plugins/` nest. Do not copy `cursor/plugins`. Do not add `pstack/` here.

## Consequences

Marketplace add can install the siblings from this repo. pstack install stays `tommy-ca/pstack --trust`. Tests forbid a `plugins/` directory and a `pstack/` plugin folder.
