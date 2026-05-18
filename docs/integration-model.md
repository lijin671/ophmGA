# Integration Model

## Contract-first integration

The bridge uses typed packets instead of direct object sharing. This keeps license, memory, security, and runtime boundaries visible.

## Packet families

| Packet | Producer | Consumer | Purpose |
|---|---|---|---|
| task packet | OpenHuman, Codex, operator | GenericAgent | Goal, task type, constraints |
| context packet | OpenHuman, repo tools | GenericAgent | Bounded context excerpts |
| permission packet | operator, policy engine | GenericAgent | Per-run capability grants |
| result packet | GenericAgent | OpenHuman, operator | Final status and summary |
| evidence packet | GenericAgent | reviewer | Screenshots, logs, pages, files |
| memory delta | GenericAgent | OpenHuman after review | Proposed memory updates |

## File handoff layout

```text
handoff/openhuman-to-ga/      # inbound task/context/permission packets
handoff/ga-to-openhuman/      # outbound results and evidence
handoff/reviewed/             # human-reviewed import-ready material
```

Runtime outputs are ignored by git. Example packets live under `examples/`.

## Escalation rules

Escalate from file handoff to a live bridge only when packet validation, evidence redaction, memory review, named browser profiles, and per-run grants are all working.

