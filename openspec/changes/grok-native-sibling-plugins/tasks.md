## 1. Tests first

- [x] 1.1 Fail then pass. Marketplace lists pstack url+sha plus local `./agent-compatibility` and `./cli-for-agent`. No `plugins/` dir. No `pstack/` dir. `grok plugin validate` on both siblings. No leftover Cursor tokens (`model: fast`, `readonly:`, `Task`, `AskQuestion`).
- [x] 1.2 Run the new tests and confirm they fail.

## 2. Plugins

- [x] 2.1 Port `cli-for-agent` as skills-only grok plugin. `plugin.json` 14-field subset. No hooks.
- [x] 2.2 Port `agent-compatibility` with four agents and parent-fanout skill. HARNESS.md spawn map. `npx` scanner. No hooks.
- [x] 2.3 Write `adr/0002-grok-native-sibling-plugins.md`. Update marketplace.json, README, SPEC, main spec.

## 3. Prove

- [x] 3.1 `python3 tests/test_marketplace.py` and `grok plugin validate` on both plugin dirs.
- [x] 3.2 `openspec validate grok-native-sibling-plugins --type change --strict`.
