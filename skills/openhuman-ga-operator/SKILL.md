---
name: openhuman-ga-operator
description: Use when planning, reviewing, or operating the OpenHuman plus GenericAgent bridge, especially tasks involving personal memory, connectors, browser automation, desktop/mobile execution, evidence, and memory writeback.
---

# OpenHuman GenericAgent Operator

## Role split

- OpenHuman owns long-term memory, connectors, and human-facing control.
- GenericAgent owns high-trust local actions through browser, desktop, OCR, physical input, and mobile/ADB lanes.
- The bridge owns packets, permissions, evidence, redaction, audit, and review.

## Before execution

1. Identify the task type.
2. Prefer OpenHuman connectors when a clean API exists.
3. Use GenericAgent only when real UI/browser/desktop/mobile operation is needed.
4. Create or validate a task packet and permission packet.
5. Require explicit scope for browser profile, cookies, screenshots, JavaScript, filesystem writes, physical input, and ADB.

## After execution

1. Validate result and evidence packets.
2. Redact evidence before promotion.
3. Treat memory deltas as proposals, not facts.
4. Import only reviewed memory deltas into OpenHuman.

## Never do by default

- install OpenHuman or GenericAgent
- copy GPL runtime code
- read real cookies without explicit permission
- write long-term memory without review
- run browser automation on the same account as an active connector sync without an account lock

