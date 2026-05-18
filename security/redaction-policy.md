# Redaction Policy

Before evidence is promoted into `handoff/reviewed/`, redact:

- API keys
- OAuth tokens
- bearer tokens
- email addresses when not needed
- phone numbers when not needed
- cookies
- session ids
- personal identifiers that are not needed for replay

Keep raw artifacts only in ignored runtime folders and delete them after review when they are no longer needed.

