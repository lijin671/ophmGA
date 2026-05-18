# Connector Policy

## Default rule

Use typed connectors before browser automation.

```text
clean API / connector available -> OpenHuman connector
no connector or UI-only workflow -> GenericAgent action plane
```

## Account locking

The same account should not be manipulated by OpenHuman connectors and GenericAgent browser automation at the same time unless a lock owner is named.

Required lock fields: account alias, owner runtime, start time, allowed action scope, and release condition.

## Connector freshness

OpenHuman should expose connector freshness, auth expiry, and sync failures. GenericAgent should not assume connector state is fresh unless it is included in the context packet.

