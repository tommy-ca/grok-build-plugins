# Handoff contract

Used by overlay workers and verifiers.
Write to `long-horizon/<id>/handoffs/<task>.md`. Also push a HostStore inbox pointer at the same path.

## Worker

```
## Status
success | partial | blocked | error

## Branch
<branch> @ <sha>

## What I did
- ...

## Measurements
- <name>: <value>

## Verification
live-ui-verified | unit-test-verified | type-check-only | not-verified

## Notes
deviations, surprises, field-guide entries added

## Suggested follow-ups
- ...
```

## Verifier

```
## Verification
live-ui-verified | unit-test-verified | type-check-only | verifier-blocked | verifier-failed

## Target
<unit id or task name> @ <sha>

## Branch
<branch>

## Execution
commands and outcomes

## Findings
one line per acceptance criterion: PASS | FAIL | INCONCLUSIVE

## Notes & suggestions
```

INCONCLUSIVE is not a pass. A new SHA voids the ledger row.
