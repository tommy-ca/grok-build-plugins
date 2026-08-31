# Catalog is an index, not a plugin monorepo

- Status: accepted
- Date: 2026-08-31

## Context

cursor/plugins is a 63-plugin marketplace with sibling dirs. open-pstack nests one plugin at `plugins/pstack/` so Claude/Codex can `/plugin marketplace add` then install `pstack@open-pstack`. Grok already installs a repo-root `plugin.json` via `grok plugin install tommy-ca/pstack --trust`. This catalog already lists remote `url` plus sha.

## Decision

Keep `tommy-ca/pstack` as a single-plugin repo. Do not vendor `cursor/plugins`. Do not nest pstack as `plugins/pstack/`. A later Grok-native plugin is a sibling folder with a local path, or another `plugins[]` entry with its own git `url` and sha. See ADR 0002.

## Consequences

pstack stays a remote pin. `owner/repo#subdir` remains available if a future plugin lives in a monorepo. Bare `grok plugin install pstack` can still hit the xAI Official Cursor wrap. v1-only is retired by ADR 0002.
