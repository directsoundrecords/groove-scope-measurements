#!/usr/bin/env python3
"""Validate the generated Groove Scope Studio application-facing catalogue."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from studio_catalog import CATALOG_PATH, DOCS, INDEX_FIELDS, ROOT, component_indexes, read_json

EXPECTED_SCHEMA_VERSION = "1.0.0"
REQUIRED_MEASUREMENT_FIELDS = {
    "measurement_id",
    "publication_status",
    "status_label",
    "measurement_date",
    "publication_date",
    "measurement_type",
    "title",
    "short_display_title",
    "summary",
    "hero_image_url",
    "card_image_url",
    "images",
    "measurement_url",
    "technical_record_url",
    "components",
    "headline_metrics",
}


def local_docs_path(url: str) -> Optional[Path]:
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "measurements.directsoundrecords.com":
        return None
    return DOCS / parsed.path.lstrip("/")


def validate_catalog(catalog: dict) -> list[str]:
    errors: list[str] = []
    if catalog.get("schema_version") != EXPECTED_SCHEMA_VERSION:
        errors.append(f"schema_version must be {EXPECTED_SCHEMA_VERSION}")
    if not isinstance(catalog.get("catalogue_version"), str) or not catalog["catalogue_version"]:
        errors.append("catalogue_version is required")
    if not isinstance(catalog.get("generated_at"), str) or not catalog["generated_at"].endswith("Z"):
        errors.append("generated_at must be a UTC ISO-8601 timestamp")

    measurements = catalog.get("measurements")
    if not isinstance(measurements, list):
        return errors + ["measurements must be an array"]
    if catalog.get("measurement_count") != len(measurements):
        errors.append("measurement_count does not match measurements length")

    policy = catalog.get("status_policy")
    included = policy.get("included_statuses", []) if isinstance(policy, dict) else []
    if not included:
        errors.append("status_policy.included_statuses must not be empty")

    seen: set[str] = set()
    for index, measurement in enumerate(measurements):
        prefix = f"measurements[{index}]"
        if not isinstance(measurement, dict):
            errors.append(f"{prefix} must be an object")
            continue
        missing = REQUIRED_MEASUREMENT_FIELDS - measurement.keys()
        if missing:
            errors.append(f"{prefix} missing: {', '.join(sorted(missing))}")
        measurement_id = measurement.get("measurement_id")
        if measurement_id in seen:
            errors.append(f"duplicate measurement_id: {measurement_id}")
        if isinstance(measurement_id, str):
            seen.add(measurement_id)
        if measurement.get("publication_status") not in included:
            errors.append(f"{prefix} violates status visibility policy")

        for key in ("measurement_url", "technical_record_url", "canonical_json_url"):
            url = measurement.get(key)
            if not isinstance(url, str) or urlparse(url).scheme != "https":
                errors.append(f"{prefix}.{key} must be an absolute HTTPS URL")
        measurement_path = local_docs_path(measurement.get("measurement_url", ""))
        if measurement_path is None or not measurement_path.is_file():
            errors.append(f"{prefix}.measurement_url does not resolve to a generated page")

        images = measurement.get("images")
        if not isinstance(images, dict):
            errors.append(f"{prefix}.images must be an object")
        else:
            for role in ("card", "hero"):
                image = images.get(role)
                if not isinstance(image, dict):
                    errors.append(f"{prefix}.images.{role} must be an object")
                    continue
                path = local_docs_path(image.get("url", ""))
                if path is None or not path.is_file():
                    errors.append(f"{prefix}.images.{role}.url does not resolve to an image")
                if not isinstance(image.get("width"), int) or not isinstance(image.get("height"), int):
                    errors.append(f"{prefix}.images.{role} dimensions must be integers")
            if measurement.get("hero_image_url") != images.get("hero", {}).get("url"):
                errors.append(f"{prefix}.hero_image_url must match images.hero.url")
            if measurement.get("card_image_url") != images.get("card", {}).get("url"):
                errors.append(f"{prefix}.card_image_url must match images.card.url")

        components = measurement.get("components")
        if not isinstance(components, dict):
            errors.append(f"{prefix}.components must be an object")
        else:
            for singular in INDEX_FIELDS.values():
                if singular not in components:
                    errors.append(f"{prefix}.components.{singular} is required")

        metrics = measurement.get("headline_metrics")
        if not isinstance(metrics, list):
            errors.append(f"{prefix}.headline_metrics must be an array")
        else:
            identifiers: set[str] = set()
            for metric_index, metric in enumerate(metrics):
                metric_prefix = f"{prefix}.headline_metrics[{metric_index}]"
                identifier = metric.get("identifier") if isinstance(metric, dict) else None
                value = metric.get("value") if isinstance(metric, dict) else None
                if not isinstance(identifier, str) or not identifier:
                    errors.append(f"{metric_prefix}.identifier is required")
                elif identifier in identifiers:
                    errors.append(f"{metric_prefix}.identifier is duplicated")
                else:
                    identifiers.add(identifier)
                if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                    errors.append(f"{metric_prefix}.value must be a finite number")

    expected_indexes = component_indexes(measurements)
    if catalog.get("components") != expected_indexes:
        errors.append("component indexes do not match the visible measurement records")
    latest = measurements[0]["measurement_id"] if measurements else None
    if catalog.get("latest_measurement_id") != latest:
        errors.append("latest_measurement_id does not match catalogue ordering")
    return errors


def main() -> int:
    try:
        catalog = read_json(CATALOG_PATH)
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL {CATALOG_PATH.relative_to(ROOT)}\n  - {exc}")
        return 1
    errors = validate_catalog(catalog)
    if errors:
        print(f"FAIL {CATALOG_PATH.relative_to(ROOT)}")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        f"PASS {CATALOG_PATH.relative_to(ROOT)} "
        f"({catalog['measurement_count']} measurement(s), schema {catalog['schema_version']})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
