# pstack-herdr harness notes

- Requires `herdr` on PATH (`mise use -g herdr`) and a running herdr server for interactive orch.
- Outside-driver orch ignores upstream `HERDR_ENV=1` gate (meta orch is not inside a pane).
- Ready kinds: operator registry; example at `references/registry.example.md`.
- Does not spawn pstack arena/interrogate panels — those stay on pstack Task models.
