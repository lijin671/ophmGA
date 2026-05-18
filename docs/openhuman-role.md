# OpenHuman Role

OpenHuman is the human-facing personal AI OS layer in this integration.

## Responsibilities

- maintain long-term personal memory
- expose a visible and editable memory UI
- manage connector freshness and auth state
- hold user profile summaries and project context
- create bounded task/context packets for operator runtimes
- import reviewed results and memory deltas

## Non-responsibilities

- direct physical browser or desktop control through this bridge
- unreviewed writeback of GenericAgent conclusions
- silent sharing of OAuth tokens, cookies, or browser profiles

## Import rule

OpenHuman should import GenericAgent outputs only after schema validation, evidence redaction, sensitive-memory review, and connector/account scope recording.

