# Cursor sibling layout does not put pstack in this catalog

- Status: accepted
- Date: 2026-08-31

## Context

cursor/plugins is a marketplace of sibling plugin folders plus a root `.cursor-plugin/marketplace.json`. This catalog already uses that shape for grok-native ports (`agent-compatibility/`, `cli-for-agent/`, `tommy-mode/`). pstack is a remote url+sha pin because grok installs `tommy-ca/pstack` as a repo-root plugin, xAI Official already publishes bare `pstack`, and pstack also hosts Claude and Codex adapters. Adding `pstack/` here would match Cursor topology and would reverse ADR 0001 and ADR 0002. `grok plugin tag` would then tag catalog HEAD for pstack. Marketplace add would clone a 400-file tree instead of a pin.

## Decision

Do not add `pstack/` at the catalog root. Do not nest `plugins/pstack`. Keep pstack as url+sha. Documented install stays `tommy-ca/pstack --trust`. `owner/repo#subdir` is not the pstack default. Cursor layout in this repo means grok-native ports as root siblings only.

## Consequences

Two git remotes stay. Operator workspaces can hold both clones. Extracting siblings remains a later option for tag-namespace hygiene. Nesting pstack is not that option.
