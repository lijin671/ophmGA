# Architecture

## Purpose

This bridge keeps three roles separate:

```text
OpenHuman     = control plane + memory plane + connector plane
GenericAgent  = action plane + local operator runtime
Bridge repo   = contracts + permissions + audit + handoff + evaluation
```

The separation is intentional. OpenHuman and GenericAgent are both powerful, but they should not silently share credentials, browser profiles, personal memory, or runtime authority.

## Data flow

```text
1. OpenHuman or a planner produces a task packet.
2. The bridge validates task, context, and permission packets.
3. GenericAgent consumes only the bounded packet and named artifacts.
4. GenericAgent writes result, evidence, and proposed memory deltas.
5. The bridge validates outputs.
6. OpenHuman imports only reviewed outcomes.
```

## Control decisions

- OpenHuman owns long-term personal memory.
- GenericAgent owns live local action execution.
- The bridge owns packet contracts and auditability.
- The human operator owns sensitive approvals.

## Integration surfaces

Start with the file handoff surface. Do not jump directly to a daemon or MCP server until packet validation, evidence review, and cleanup work reliably.

Recommended order:

```text
file handoff -> adapter subprocess -> local MCP -> deeper runtime integration
```

## Runtime isolation

Each trial should declare browser profile, account scope, filesystem paths, allowed domains, screenshot policy, JavaScript/CDP permission, cookie access, physical input, ADB/mobile policy, and cleanup path.

