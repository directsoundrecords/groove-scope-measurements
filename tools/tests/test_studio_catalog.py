from __future__ import annotations

import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from studio_catalog import build_catalog, component_indexes  # noqa: E402
from validate_studio_catalog import validate_catalog  # noqa: E402


class StudioCatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = build_catalog(generate_images=False)

    def test_catalog_is_valid(self) -> None:
        self.assertEqual(validate_catalog(self.catalog), [])

    def test_unknown_setup_values_remain_explicit(self) -> None:
        measurement = self.catalog["measurements"][0]
        self.assertEqual(measurement["components"]["stylus"]["state"], "not_recorded")
        self.assertIsNone(measurement["components"]["stylus"]["display_name"])
        self.assertEqual(measurement["components"]["audio_interface"]["state"], "not_confirmed")
        self.assertEqual(measurement["components"]["audio_interface"]["reported_label"], "EVO4")

    def test_headline_metrics_are_flexible_numeric_records(self) -> None:
        metrics = self.catalog["measurements"][0]["headline_metrics"]
        identifiers = {metric["identifier"] for metric in metrics}
        self.assertIn("playback_rpm", identifiers)
        self.assertIn("thd_left_percent", identifiers)
        self.assertTrue(all(isinstance(metric["value"], (int, float)) for metric in metrics))

    def test_component_indexes_are_derived(self) -> None:
        measurements = self.catalog["measurements"]
        self.assertEqual(self.catalog["components"], component_indexes(measurements))
        cartridge = self.catalog["components"]["cartridges"][0]
        self.assertEqual(cartridge["measurement_ids"], ["GS-2026-0003"])


if __name__ == "__main__":
    unittest.main()
