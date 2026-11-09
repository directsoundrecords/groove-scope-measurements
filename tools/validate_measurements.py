#!/usr/bin/env python3
"""Basic local validation for Groove Scope measurement JSON files."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MEASUREMENTS = ROOT / "measurements"

REQUIRED_TOP_LEVEL = {
    "schema_version",
    "measurement_id",
    "record_version",
    "publication_status",
    "title",
    "creator",
    "publisher",
    "software",
    "measurement_type",
    "setup",
    "results",
    "provenance",
    "license",
}


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"Invalid JSON: {exc}"]

    missing = sorted(REQUIRED_TOP_LEVEL - data.keys())
    if missing:
        errors.append(f"Missing required fields: {', '.join(missing)}")

    measurement_id = data.get("measurement_id", "")
    if path.parent.name != measurement_id:
        errors.append(
            f"Folder name {path.parent.name!r} does not match measurement_id {measurement_id!r}"
        )

    if data.get("publication_status") == "published":
        setup = data.get("setup")
        cartridge = setup.get("cartridge") if isinstance(setup, dict) else None
        if isinstance(cartridge, str) and cartridge.strip() not in {"", "not_recorded"}:
            title = data.get("title")
            if not isinstance(title, str) or (
                title != cartridge and not title.startswith(f"{cartridge} — ")
            ):
                errors.append(f"Published record title must start with its cartridge name ({cartridge})")

        software = data.get("software")
        if not isinstance(software, dict):
            errors.append("Published record requires a software object")
        else:
            for field in ("application_version", "analysis_method_version"):
                value = software.get(field)
                if not isinstance(value, str) or not value.strip():
                    errors.append(f"Published record requires a value for software.{field}")

    return errors


def main() -> int:
    files = sorted(MEASUREMENTS.glob("GS-*/measurement.json"))
    if not files:
        print("No measurement JSON files found.")
        return 1

    failed = False
    for path in files:
        errors = validate(path)
        if errors:
            failed = True
            print(f"FAIL {path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {path.relative_to(ROOT)}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
