# Memory Ownership

## Ownership rule

```text
OpenHuman owns long-term personal memory.
GenericAgent owns operational/session memory.
The bridge owns proposed memory deltas and review state.
```

## Why this matters

Both systems can remember. If both write long-term memory independently, the combined system will accumulate duplicates, stale claims, and untraceable profile drift.

## Write path

GenericAgent may output `memory_delta.json` or `memory_delta.md`. OpenHuman may persist the delta only after review.

## Delta fields

Each memory delta should include proposed fact or preference, source task id, evidence artifact reference, confidence, sensitivity level, expiration or review date when applicable, and reviewer decision.

## Conflict handling

If a proposed memory delta conflicts with existing OpenHuman memory, the bridge should mark it as `conflict` and require human review.

