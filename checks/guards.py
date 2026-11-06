"""Optimization-safe scientific guards and fresh, explicitly selected receipts."""
import argparse
import json
from pathlib import Path

class VerificationError(RuntimeError):
    def __init__(self, code):
        self.code = code
        super().__init__(code)

def require(condition, code):
    if not condition:
        raise VerificationError(code)

def write_receipt(record):
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="New receipt path; existing files are never replaced")
    args = parser.parse_args()
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        json.dump(record, handle, indent=2, allow_nan=False)
        handle.write("\n")

