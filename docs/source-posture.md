# Source Posture

## OpenHuman

- Source: https://github.com/tinyhumansai/openhuman
- Role here: peer runtime and product-pattern source
- License posture: GPL-3.0 runtime code is not copied into this repository
- Trust posture: high-trust personal memory, OAuth, desktop, and connector surface

## GenericAgent

- Source: https://github.com/lsdefine/GenericAgent
- Role here: peer runtime and local operator action plane
- License posture: MIT is compatible with adapters, but runtime import is still avoided until needed
- Trust posture: high-trust browser, desktop, mobile/ADB, OCR, physical input, and scheduler surface

## Bridge repository

- Role here: contracts, packet validation, permission boundaries, evidence, review, and examples
- License posture: MIT for bridge-owned content
- Runtime posture: no default installer, no copied peer-runtime code, no secrets

