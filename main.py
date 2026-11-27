#!/usr/bin/env python3
"""The Agent's Uh-Oh — one-word entry: Pondering.

When the agent has no idea what to do, it buys time by pondering.
This program delivers the single word as the competition entry.
"""

import hashlib
import os
import sys
from pathlib import Path

ENTRY = "Pondering"
ENTRY_SHA256 = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
MAX_CHARS = 99

def output_path() -> Path:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def write_entry(path: Path) -> None:
    data = ENTRY.encode("utf-8")
    if len(ENTRY) > MAX_CHARS or len(ENTRY.split()) != 1:
        raise SystemExit("gate failed: entry must be one word of at most 99 characters")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    back = path.read_bytes()
    if back != data or hashlib.sha256(back).hexdigest() != ENTRY_SHA256:
        raise SystemExit("verification failed: written bytes differ from entry")
    print(f"wrote {path} ({len(back)} bytes, sha256 {ENTRY_SHA256})")


def main() -> int:
    write_entry(output_path())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
