#!/usr/bin/env python3
"""Build the Groove Scope Studio catalogue from canonical measurement records."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional, Tuple

ROOT = Path(__file__).resolve().parents[1]
MEASUREMENTS = ROOT / "measurements"
DOCS = ROOT / "docs"
STUDIO = DOCS / "groove-scope" / "studio"
POLICY_PATH = ROOT / "data" / "studio" / "reference-library-policy.json"
CATALOG_PATH = STUDIO / "catalog.json"

UNKNOWN_STATES = {"not_recorded", "not_confirmed", "unknown", "not_applicable"}
INDEX_FIELDS = {
    "cartridges": "cartridge",
    "turntables": "turntable",
    "tonearms": "tonearm",
    "phono_stages": "phono_stage",
}

METRIC_SPECS = (
    ("playback_rpm", "Playback speed", ("playback_rpm", "value"), "RPM"),
    ("playback_speed_error_percent", "Speed error", ("playback_speed_error_percent", "value"), "%"),
    ("din_shaped_wow_flutter_percent", "DIN W&F", ("din_shaped_wow_flutter_percent", "value"), "%"),
    ("channel_balance_db", "Channel balance", ("channel_balance_db", "value"), "dB"),
    ("average_channel_separation_db", "Average separation", ("crosstalk_1khz_db", "average_separation"), "dB"),
    ("crosstalk_left_to_right_db", "L→R crosstalk", ("crosstalk_1khz_db", "left_to_right"), "dB"),
    ("crosstalk_right_to_left_db", "R→L crosstalk", ("crosstalk_1khz_db", "right_to_left"), "dB"),
    ("thd_left_percent", "THD left", ("thd_percent", "left"), "%"),
    ("thd_right_percent", "THD right", ("thd_percent", "right"), "%"),
)


class StudioCatalogError(ValueError):
    """Raised when a canonical record cannot safely enter the Studio feed."""


def read_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise StudioCatalogError(f"Cannot read {path.relative_to(ROOT)}: {exc}") from exc


def canonical_records() -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    seen: set[str] = set()
    for path in sorted(MEASUREMENTS.glob("GS-*/measurement.json")):
        record = read_json(path)
        measurement_id = record.get("measurement_id")
        if not isinstance(measurement_id, str) or not measurement_id:
            raise StudioCatalogError(f"{path.relative_to(ROOT)} has no measurement_id")
        if measurement_id in seen:
            raise StudioCatalogError(f"Duplicate measurement_id: {measurement_id}")
        if path.parent.name != measurement_id:
            raise StudioCatalogError(
                f"Folder {path.parent.name} does not match measurement_id {measurement_id}"
            )
        seen.add(measurement_id)
        records.append((path, record))
    if not records:
        raise StudioCatalogError("No canonical measurement records found")
    return records


def state_and_value(value: Any) -> Tuple[str, Optional[Any]]:
    if value is None:
        return "not_recorded", None
    if isinstance(value, str) and value.strip().lower() in UNKNOWN_STATES:
        return value.strip().lower(), None
    return "recorded", value


def component(value: Any, *, unit: Optional[str] = None) -> dict[str, Any]:
    state, recorded = state_and_value(value)
    item: dict[str, Any] = {"state": state, "value": recorded}
    if unit is not None:
        item["unit"] = unit
    return item


def named_component(kind: str, value: Any) -> dict[str, Any]:
    state, recorded = state_and_value(value)
    return {
        "kind": kind,
        "state": state,
        "display_name": recorded,
        # Manufacturer/model are intentionally null until canonical records expose them.
        "manufacturer": None,
        "model": None,
    }


def audio_interface_component(setup: dict[str, Any]) -> dict[str, Any]:
    reported_state, reported = state_and_value(setup.get("audio_interface_reported_label"))
    model_state, model = state_and_value(setup.get("audio_interface_full_model"))
    display_name = model if model is not None else reported
    state = model_state if model is None else "recorded"
    if display_name is None:
        state = reported_state if reported_state != "recorded" else model_state
    return {
        "kind": "audio_interface",
        "state": state,
        "display_name": display_name,
        "reported_label": reported,
        "confirmed_model": model,
    }


def result_at(results: dict[str, Any], path: tuple[str, str]) -> Tuple[Optional[Any], Optional[str]]:
    group = results.get(path[0])
    if not isinstance(group, dict):
        return None, None
    return group.get(path[1]), group.get("classification")


def headline_metrics(results: dict[str, Any]) -> list[dict[str, Any]]:
    metrics: list[dict[str, Any]] = []
    for identifier, label, path, unit in METRIC_SPECS:
        value, classification = result_at(results, path)
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            continue
        metrics.append(
            {
                "identifier": identifier,
                "display_label": label,
                "value": value,
                "unit": unit,
                "classification": classification,
            }
        )
    return metrics


def measurement_date(record: dict[str, Any]) -> Optional[str]:
    value = record.get("measurement_datetime_local")
    return value[:10] if isinstance(value, str) and len(value) >= 10 else None


def system_title(setup: dict[str, Any]) -> str:
    values = []
    for key in ("turntable", "tonearm", "cartridge"):
        state, value = state_and_value(setup.get(key))
        if state == "recorded" and value is not None:
            values.append(str(value))
    return " / ".join(values) or "Measured analogue playback system"


def slug_text(value: str) -> str:
    return "-".join(
        "".join(character.lower() if character.isalnum() else " " for character in value).split()
    )


def format_status(status: str) -> str:
    return status.replace("_", " ").title()


def ensure_card_image(hero: Path, destination: Path) -> None:
    if destination.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    magick = shutil.which("magick") or shutil.which("convert")
    if magick:
        subprocess.run(
            [magick, str(hero), "-resize", "1200x675^", "-gravity", "center", "-extent", "1200x675", "-quality", "88", str(destination)],
            check=True,
        )
        return
    sips = shutil.which("sips")
    if sips:
        with tempfile.TemporaryDirectory() as temporary:
            intermediate = Path(temporary) / "crop.png"
            subprocess.run(
                [sips, "--setProperty", "format", "png", "--cropToHeightWidth", "1350", "2400", str(hero), "--out", str(intermediate)],
                check=True,
                stdout=subprocess.DEVNULL,
            )
            subprocess.run(
                [sips, "--resampleHeightWidth", "675", "1200", "--setProperty", "format", "jpeg", "--setProperty", "formatOptions", "88", str(intermediate), "--out", str(destination)],
                check=True,
                stdout=subprocess.DEVNULL,
            )
        return
    raise StudioCatalogError(
        f"Card image is missing for {hero}; install ImageMagick or generate it on macOS with sips"
    )


def image_record(measurement_id: str, base_url: str, *, generate_images: bool) -> dict[str, Any]:
    hero = DOCS / "groove-scope" / "assets" / measurement_id / "web" / "hero-2400.webp"
    if not hero.is_file():
        raise StudioCatalogError(
            f"Missing processed hero image: {hero.relative_to(ROOT)}"
        )
    card = STUDIO / "images" / f"{measurement_id}-card-1200.jpg"
    if generate_images:
        ensure_card_image(hero, card)
    elif not card.is_file():
        raise StudioCatalogError(f"Missing Studio card image: {card.relative_to(ROOT)}")
    return {
        "card": {
            "url": f"{base_url}/groove-scope/studio/images/{measurement_id}-card-1200.jpg",
            "width": 1200,
            "height": 675,
        },
        "hero": {
            "url": f"{base_url}/groove-scope/assets/{measurement_id}/web/hero-2400.webp",
            "width": 2400,
            "height": 1800,
        },
    }


def studio_measurement(record: dict[str, Any], base_url: str, *, generate_images: bool) -> dict[str, Any]:
    measurement_id = record["measurement_id"]
    setup = record.get("setup") if isinstance(record.get("setup"), dict) else {}
    results = record.get("results") if isinstance(record.get("results"), dict) else {}
    interpretation = record.get("interpretation") if isinstance(record.get("interpretation"), dict) else {}
    status = record.get("publication_status", "draft")
    phono = named_component("phono_stage", setup.get("phono_stage"))
    components = {
        "turntable": named_component("turntable", setup.get("turntable")),
        "tonearm": named_component("tonearm", setup.get("tonearm")),
        "cartridge": named_component("cartridge", setup.get("cartridge")),
        "stylus": named_component("stylus", setup.get("stylus")),
        "phono_stage": phono,
        "audio_interface": audio_interface_component(setup),
        "tracking_force": component(setup.get("vertical_tracking_force_g"), unit="g"),
        "cartridge_loading": component(setup.get("cartridge_loading")),
        "phono_gain": component(setup.get("phono_gain_db"), unit="dB"),
        "test_record": named_component("test_record", setup.get("test_record")),
        "test_record_track": component(setup.get("test_record_track")),
        "nominal_test_tone": component(setup.get("nominal_test_tone_hz"), unit="Hz"),
        "turntable_support": component(setup.get("turntable_support")),
    }
    searchable = [
        measurement_id,
        record.get("measurement_type"),
        *(item.get("display_name") for item in components.values() if isinstance(item, dict)),
        components["test_record"].get("display_name"),
    ]
    title = system_title(setup)
    images = image_record(measurement_id, base_url, generate_images=generate_images)
    return {
        "measurement_id": measurement_id,
        "publication_status": status,
        "status_label": format_status(status),
        "measurement_date": measurement_date(record),
        "publication_date": record.get("date_published"),
        "measurement_type": record.get("measurement_type"),
        "title": record.get("title"),
        "short_display_title": title,
        "system_title": title,
        "summary": interpretation.get("summary"),
        "hero_image_url": images["hero"]["url"],
        "card_image_url": images["card"]["url"],
        "images": images,
        "measurement_url": f"{base_url}/groove-scope/measurements/{measurement_id}.html",
        "technical_record_url": f"https://github.com/directsoundrecords/groove-scope-measurements/tree/main/measurements/{measurement_id}",
        "canonical_json_url": f"https://raw.githubusercontent.com/directsoundrecords/groove-scope-measurements/main/measurements/{measurement_id}/measurement.json",
        "components": components,
        "headline_metrics": headline_metrics(results),
        "search_text": " ".join(str(value) for value in searchable if value).strip(),
    }


def component_indexes(measurements: Iterable[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    indexes: dict[str, list[dict[str, Any]]] = {}
    for plural, singular in INDEX_FIELDS.items():
        grouped: dict[str, dict[str, Any]] = {}
        for measurement in measurements:
            item = measurement["components"][singular]
            name = item.get("display_name") if item.get("state") == "recorded" else None
            if not name:
                continue
            key = str(name).casefold()
            entry = grouped.setdefault(
                key,
                {
                    "identifier": slug_text(str(name)),
                    "display_name": name,
                    "manufacturer": item.get("manufacturer"),
                    "model": item.get("model"),
                    "measurement_count": 0,
                    "measurement_ids": [],
                },
            )
            entry["measurement_ids"].append(measurement["measurement_id"])
            entry["measurement_count"] += 1
        indexes[plural] = sorted(grouped.values(), key=lambda entry: entry["display_name"].casefold())
    return indexes


def generated_at() -> str:
    source_date_epoch = os.environ.get("SOURCE_DATE_EPOCH")
    instant = (
        datetime.fromtimestamp(int(source_date_epoch), tz=timezone.utc)
        if source_date_epoch
        else datetime.now(tz=timezone.utc)
    )
    return instant.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_catalog(*, generate_images: bool = True) -> dict[str, Any]:
    policy = read_json(POLICY_PATH)
    included_statuses = policy.get("included_statuses")
    if not isinstance(included_statuses, list) or not included_statuses:
        raise StudioCatalogError("Studio policy must include at least one publication status")
    base_url = str(policy.get("base_url", "")).rstrip("/")
    if not base_url.startswith("https://"):
        raise StudioCatalogError("Studio base_url must use HTTPS")

    source_records = canonical_records()
    visible_records = [
        record for _, record in source_records if record.get("publication_status") in included_statuses
    ]
    measurements = [
        studio_measurement(record, base_url, generate_images=generate_images)
        for record in visible_records
    ]
    measurements.sort(
        key=lambda item: (item.get("measurement_date") or "", item["measurement_id"]),
        reverse=True,
    )
    digest_input = "\n".join(
        json.dumps(record, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        for _, record in source_records
    )
    catalogue_version = hashlib.sha256(digest_input.encode("utf-8")).hexdigest()[:16]
    return {
        "schema_version": policy["catalog_schema_version"],
        "catalogue_version": catalogue_version,
        "generated_at": generated_at(),
        "catalogue_url": f"{base_url}{policy['catalog_path']}",
        "status_policy": {
            "included_statuses": included_statuses,
            "excluded_statuses": [
                status for status in ("superseded", "withdrawn") if status not in included_statuses
            ],
        },
        "measurement_count": len(measurements),
        "latest_measurement_id": measurements[0]["measurement_id"] if measurements else None,
        "measurements": measurements,
        "components": component_indexes(measurements),
    }


def write_catalog(catalog: dict[str, Any]) -> None:
    STUDIO.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    write_catalog(build_catalog())
    print(f"Wrote {CATALOG_PATH.relative_to(ROOT)}")
