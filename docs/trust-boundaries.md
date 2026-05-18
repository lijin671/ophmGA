# Trust Boundaries

## High-trust surfaces

Treat these as separate permission grants:

- browser profile selection
- cookie read/write
- page JavaScript or CDP execution
- screenshots and OCR
- file upload/download
- filesystem write paths
- keyboard and mouse input
- ADB/mobile control
- OAuth connector access
- long-term memory writeback

## Default deny

Every packet should grant the minimum capability needed for the current task. Omitted permissions are denied.

## Evidence handling

Evidence may contain secrets, personal data, or session state. Store runtime evidence under ignored `handoff/` paths and run redaction before promotion into reviewed artifacts.

