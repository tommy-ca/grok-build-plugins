## Context

Grok 09-plugins.md allows local plugin folders or remote `url` plus sha. This catalog uses remote pin. ADR-0024 names `tommy-ca/pstack` as default.

## Goals / Non-Goals

**Goals:** Index-only catalog. Owner/repo install. 40-hex pin.

**Non-Goals:** Vendoring cursor/plugins. Chezmoi. team-kit. make-bot-ui.

## Decisions

### D1. Catalog, not a second pstack
### D2. Index at `.grok-plugin/marketplace.json`
### D3. v1 plugin list is pstack only
### D4. Documented install is `tommy-ca/pstack`, not bare `pstack`

## Risks / Trade-offs

- [EROFS on ~/.grok] -> marketplace add may fail. Direct owner/repo install still works.
- [xAI Official name collision] -> owner/repo is the documented default.

## Migration Plan

Install `tommy-ca/pstack`. Optionally add this marketplace.

## Open Questions

None for v1.
