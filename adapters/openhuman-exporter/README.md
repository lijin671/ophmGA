# OpenHuman Exporter Adapter

This adapter will export bounded task and context packets from OpenHuman.

Current posture: skeleton only.

Expected inputs:

- user-approved task goal
- selected memory excerpts
- connector freshness summary
- account or profile scope

Expected outputs:

- `task_packet.json`
- optional `context_packet.json`
- optional `permission_packet.json`

Do not export raw OAuth tokens, cookies, full memory stores, or full private logs.

