# MCP Bridge Notes

The first implementation should use file handoff. MCP comes later.

A future MCP bridge may expose:

- `create_task_packet`
- `validate_packet`
- `submit_to_genericagent`
- `list_pending_results`
- `review_memory_delta`
- `import_reviewed_result`

Do not expose raw browser cookies, OAuth tokens, or unrestricted filesystem access through MCP tools.

