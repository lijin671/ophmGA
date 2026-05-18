#!/usr/bin/env python3
"""Dependency-free shallow packet validator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = {
    "task": REPO_ROOT / "contracts" / "task_packet.schema.json",
    "context": REPO_ROOT / "contracts" / "context_packet.schema.json",
    "permission": REPO_ROOT / "contracts" / "permission_packet.schema.json",
    "result": REPO_ROOT / "contracts" / "result_packet.schema.json",
    "evidence": REPO_ROOT / "contracts" / "evidence_packet.schema.json",
    "memory_delta": REPO_ROOT / "contracts" / "memory_delta.schema.json",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def type_name(value: Any) -> str:
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, dict):
        return "object"
    if isinstance(value, list):
        return "array"
    if isinstance(value, str):
        return "string"
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return "number"
    if value is None:
        return "null"
    return type(value).__name__


def validate(packet: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in schema.get("required", []):
        if field not in packet:
            errors.append(f"missing required field: {field}")

    for field, rules in schema.get("properties", {}).items():
        if field not in packet:
            continue
        expected = rules.get("type")
        actual = type_name(packet[field])
        if expected and actual != expected:
            errors.append(f"field {field} expected {expected}, got {actual}")
        enum = rules.get("enum")
        if enum and packet[field] not in enum:
            errors.append(f"field {field} expected one of {enum}, got {packet[field]!r}")
    return errors


def schema_for_packet(packet: dict[str, Any]) -> Path:
    packet_type = packet.get("packet_type")
    if packet_type not in CONTRACTS:
        raise ValueError(f"unknown packet_type: {packet_type!r}")
    return CONTRACTS[packet_type]


def validate_file(packet_path: Path, schema_path: Path | None = None) -> list[str]:
    packet = load_json(packet_path)
    if not isinstance(packet, dict):
        return ["packet root must be an object"]
    schema = load_json(schema_path or schema_for_packet(packet))
    return validate(packet, schema)


def example_files() -> list[Path]:
    return sorted((REPO_ROOT / "examples").glob("**/*.json"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate bridge packet JSON files.")
    parser.add_argument("packet", nargs="?", help="Packet JSON file")
    parser.add_argument("schema", nargs="?", help="Optional schema JSON file")
    parser.add_argument("--all-examples", action="store_true", help="Validate all example JSON packets")
    args = parser.parse_args()

    targets: list[tuple[Path, Path | None]] = []
    if args.all_examples:
        targets.extend((path, None) for path in example_files())
    elif args.packet:
        targets.append((Path(args.packet), Path(args.schema) if args.schema else None))
    else:
        parser.error("provide a packet file or --all-examples")

    failed = False
    for packet_path, schema_path in targets:
        errors = validate_file(packet_path, schema_path)
        if errors:
            failed = True
            print(f"FAIL {packet_path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {packet_path}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

