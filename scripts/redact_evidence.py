#!/usr/bin/env python3
"""Redact common secrets from text evidence files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


PATTERNS = [
    (re.compile(r"(?i)(bearer\s+)[a-z0-9._\-]{16,}"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(api[_-]?key\s*[:=]\s*)[a-z0-9._\-]{12,}"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(token\s*[:=]\s*)[a-z0-9._\-]{12,}"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(cookie\s*[:=]\s*)[^\n;]+"), r"\1[REDACTED]"),
    (re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"), "[EMAIL_REDACTED]"),
    (re.compile(r"(?<!\d)(?:\+?\d[\d .-]{8,}\d)(?!\d)"), "[PHONE_REDACTED]"),
]


def redact(text: str) -> str:
    for pattern, replacement in PATTERNS:
        text = pattern.sub(replacement, text)
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description="Redact text evidence.")
    parser.add_argument("input", help="Input text file")
    parser.add_argument("output", help="Output text file")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    text = input_path.read_text(encoding="utf-8", errors="replace")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(redact(text), encoding="utf-8")
    print(f"redacted {input_path} -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

