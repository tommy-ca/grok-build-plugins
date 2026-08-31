## 1. Tests first

- [x] 1.1 README and spec name `agent-compatibility:startup-review`. Tests scan HARNESS.md for Cursor leftover tokens except the never-send effort line. ADR 0001 names sibling local folders.

## 2. Apply

- [x] 2.1 Edit ADR 0001 Decision. Expand spawn-types spec. Full `spawn_subagent` on skill steps 2-4. Tighten tests.

## 3. Prove

- [x] 3.1 `python3 tests/test_marketplace.py`. `openspec validate grok-sibling-port-audit --type change --strict`.
