# MCP Server Contract

## Required properties

- local-only by default
- explicit auth token when network exposed
- per-tool permission checks
- JSON schema validation for every packet
- audit log for every submission and import
- no automatic install of peer runtimes
- no raw secret return values

## Tool sketch

| Tool | Input | Output | Notes |
|---|---|---|---|
| `validate_packet` | packet path, schema path | validation report | dependency-free validation first |
| `submit_task` | task packet path | task id | only writes into handoff folder |
| `collect_result` | task id | result packet path | no memory import |
| `review_memory_delta` | delta path, decision | reviewed delta | human or approved policy decision |
| `import_result` | reviewed result path | import report | OpenHuman-side adapter owns final write |

