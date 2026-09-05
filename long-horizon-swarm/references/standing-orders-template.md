# Standing orders template

Paste into `long-horizon/<id>/preferences.md` before the first spawn. Numbered. Verbatim in every brief.

1. Planners never write product code. Briefs are the product.
2. Workers never edit plan, HostStore, or design docs they do not own.
3. Every spawn reads field-guide/index.md and stays under its line budget.
4. One writer per worktree. Shared mutable files are split first.
5. Every design decision has one conceptKey and one design-docs/<conceptKey>.md owner.
6. Code that embodies a decision cites that design doc.
7. Verification uses the real artifact. Self-report is not a verdict.
8. Verifier model family differs from the worker when a second slug exists. Else family: same-degraded.
9. Megafile threshold is 800 lines of owned code. Cross it and stop; spawn decompose.
10. Ossify-break is allowed as one focused patch that names the new contract in the DesignDoc.
11. Irreversible actions (force-push to shared branches, deploys, data deletion) still pause.
12. No weaker-model fallback. A missing lane is a dropout.
13. Brief.ACCEPTANCE is GIVEN/WHEN/THEN copied from the capability spec scenarios.
14. If openspec/changes/<id>/ exists, do not spawn workers until tasks.md exists.
15. Recurse is parent-owned units. Children do not call spawn_subagent.
