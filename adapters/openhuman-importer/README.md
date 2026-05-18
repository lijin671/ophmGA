# OpenHuman Importer Adapter

This adapter will import reviewed GenericAgent outputs into OpenHuman.

Current posture: skeleton only.

Import order:

1. validate result and evidence packets
2. redact evidence
3. classify memory deltas
4. require human review for sensitive updates
5. write only approved deltas into OpenHuman memory

