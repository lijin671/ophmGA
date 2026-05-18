# GenericAgent Role

GenericAgent is the high-trust local action plane in this integration.

## Responsibilities

- consume bounded task/context/permission packets
- execute approved browser, desktop, mobile/ADB, OCR, and Web SOP tasks
- write result packets and evidence artifacts
- propose memory deltas instead of directly mutating long-term memory
- record enough action history for review and replay

## Unlock expectation

GenericAgent should not be judged by cold-start behavior alone. Browser bridge, Web SOPs, vision/input lanes, layered memory, and scheduler/reflect support may materially change its capability.

## Non-responsibilities

- owning the user's long-term personal memory
- silently reading cookies or OAuth state outside a permission packet
- operating the same account/profile concurrently with OpenHuman connectors
- writing unreviewed facts into OpenHuman memory

