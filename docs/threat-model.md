# Threat Model

## Assets

- personal memory
- OAuth tokens and connector auth state
- browser cookies and logged-in sessions
- local files
- screenshots and OCR text
- execution logs
- mobile/ADB access

## Main risks

1. unreviewed long-term memory pollution
2. accidental credential capture in evidence
3. browser profile misuse
4. connector and browser automation race conditions
5. over-broad filesystem grants
6. prompt injection from pages, documents, or tool output
7. license contamination from copied runtime code

## Controls

- use packet schemas
- keep runtime outputs ignored by git
- require per-run permission packets
- redact evidence before review import
- use disposable browser profiles for trials
- copy patterns, not GPL runtime code
- record task ids and evidence references for replay

