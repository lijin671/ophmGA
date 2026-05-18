# Packet Lifecycle

## 1. Create

OpenHuman, Codex, or the operator creates a task packet with bounded context and explicit permissions.

## 2. Validate

Run:

```bash
python scripts/validate_packet.py path/to/task_packet.json
```

## 3. Execute

GenericAgent consumes the packet only inside the named runtime scope.

## 4. Collect

GenericAgent writes result, evidence, and memory-delta packets under ignored handoff paths.

## 5. Redact

Text evidence should be redacted before review import.

## 6. Review

Sensitive memory deltas and connector outcomes require human review.

## 7. Import

OpenHuman imports reviewed outputs only. Raw runtime evidence stays ignored or is deleted.

