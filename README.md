# OpenHuman GenericAgent Bridge

This repository is a bridge layer for combining two different runtime roles:

- **OpenHuman** as the personal AI OS, memory surface, connector surface, and human-facing control plane.
- **GenericAgent** as the high-trust local operator runtime for browser, desktop, mobile/ADB, OCR, physical input, and Web SOP execution.

The repository does **not** vendor OpenHuman or GenericAgent runtime code. It defines contracts, safety boundaries, handoff folders, adapter skeletons, evaluation checklists, and a reusable skill for operating the combination.

## Core model

```text
OpenHuman  -> task/context/permission packet -> GenericAgent
GenericAgent -> result/evidence/memory-delta packet -> OpenHuman
Human review gates sensitive memory writes and connector actions.
```

## Repository posture

- No installer is executed by this repository.
- No browser extension, MCP server, OAuth connector, desktop app, ADB tool, or GenericAgent runtime is installed by default.
- OpenHuman is treated as a peer runtime and pattern source. Its GPL-3.0 runtime code is not copied here.
- GenericAgent is treated as a peer runtime and high-trust action plane. Its MIT license is friendlier, but its browser/desktop/mobile permissions still require explicit trial contracts.

## Directory map

| Path | Purpose |
|---|---|
| `contracts/` | JSON packet schemas for handoff and review |
| `handoff/` | Local file bridge folders; runtime outputs are ignored by git |
| `adapters/` | Adapter skeletons, not installed implementations |
| `skills/` | Reusable agent skill for this integration pattern |
| `mcp/` | Future MCP bridge contract notes |
| `evals/` | Safety and quality evaluation checklists |
| `examples/` | Safe example packets with fake data only |
| `security/` | Permission, redaction, browser profile, audit, and cleanup policies |
| `scripts/` | Dependency-free validation and redaction helpers |

## Quick validation

Validate all bundled example packets:

```bash
python scripts/validate_packet.py --all-examples
```

Run the redaction helper on a text artifact:

```bash
python scripts/redact_evidence.py input.txt output.txt
```

## Integration phases

1. **Pattern-only**: keep contracts and documentation only.
2. **File handoff**: exchange JSON packets through `handoff/`.
3. **Adapter trial**: add project-local exporters/runners/importers.
4. **MCP or ACP bridge**: expose a typed local bridge only after file handoff is reliable and auditable.
5. **Connector and memory sync**: enable only after human review and rollback paths are proven.

## Non-goals

- This is not an OpenHuman fork.
- This is not a GenericAgent fork.
- This is not a one-click installer.
- This is not a place for real cookies, OAuth tokens, browser profiles, or personal logs.

