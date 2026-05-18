# Quickstart

This repository is a bridge contract, not an installer. Use it to move tasks
between OpenHuman and GenericAgent through validated packets.

## 0. Validate the repository examples

```bash
python scripts/validate_packet.py --all-examples
```

## 1. Pick a task packet

Start with a safe example:

```text
examples/simple-research-task/task_packet.json
examples/browser-operation-task/task_packet.json
examples/connector-assisted-task/task_packet.json
```

Copy or adapt it into:

```text
handoff/openhuman-to-ga/task_packet.json
```

Runtime handoff files are ignored by git by default.

## 2. Validate the task packet

```bash
python scripts/validate_packet.py handoff/openhuman-to-ga/task_packet.json
```

Do not send an invalid packet to a runtime.

## 3. Execute through GenericAgent

For the current bridge version, GenericAgent execution is manual or adapter-led:

1. open the validated task packet
2. confirm the permission scope
3. run GenericAgent in the matching disposable/local runtime profile
4. write outputs back under `handoff/ga-to-openhuman/`

Expected outputs:

```text
handoff/ga-to-openhuman/result_packet.json
handoff/ga-to-openhuman/evidence/
handoff/ga-to-openhuman/memory_delta.json
```

## 4. Validate the result and memory delta

```bash
python scripts/validate_packet.py handoff/ga-to-openhuman/result_packet.json
python scripts/validate_packet.py handoff/ga-to-openhuman/memory_delta.json
```

## 5. Redact evidence before review

For text evidence:

```bash
python scripts/redact_evidence.py raw.txt redacted.txt
```

Screenshots and binary artifacts require manual review.

## 6. Review before OpenHuman import

Only move reviewed outputs into:

```text
handoff/reviewed/
```

OpenHuman should import reviewed result summaries and approved memory deltas
only. Raw evidence should remain ignored or be deleted after review.

## Safe first run

Use this order:

1. `simple-research-task`: no browser, no network, no memory writeback.
2. `browser-operation-task`: disposable browser profile, no cookies, local/test pages only.
3. `memory-update-task`: fake memory delta, manual review only.
4. connector/account trials only after the first three pass.

