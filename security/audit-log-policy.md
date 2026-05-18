# Audit Log Policy

Every runtime task should produce an audit summary with:

- task id
- runtime name and version if known
- start and end time
- permission packet path
- key actions
- artifacts written
- memory deltas proposed
- cleanup status

Audit logs may contain sensitive information and should stay in ignored handoff folders unless redacted.

