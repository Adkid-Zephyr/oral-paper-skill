#!/usr/bin/env python3
"""Offline regression tests for corpus parsing and abstract-card validation."""

import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


collector = load("collector", ROOT / "scripts/collect_corpus.py")
distiller = load("distiller", ROOT / "scripts/distill_abstracts.py")


class NullNormalizationTests(unittest.TestCase):
    def test_only_optional_serialized_null_is_normalized(self):
        card = {
            "problem_and_gap": {"problem": {"claim": "null", "source_ids": []}, "gap": {"claim": "null", "source_ids": []}},
            "stated_novelty": {"claim": "null", "source_ids": []},
            "other": "null",
        }
        changed = distiller.normalize_nulls(card)
        self.assertEqual(len(changed), 3)
        self.assertIsNone(card["problem_and_gap"]["problem"]["claim"])
        self.assertEqual(card["other"], "null")

    def test_substantive_null_text_is_not_normalized(self):
        card = {
            "problem_and_gap": {"problem": {"claim": "null hypothesis", "source_ids": []}},
            "stated_novelty": {"claim": "null", "source_ids": ["S1"]},
        }
        self.assertEqual(distiller.normalize_nulls(card), [])
        self.assertEqual(card["problem_and_gap"]["problem"]["claim"], "null hypothesis")
        self.assertEqual(card["stated_novelty"]["claim"], "null")


class LocatorValidationTests(unittest.TestCase):
    def base(self):
        return {"paper_id": "p1", "lessons": [], "problem": {"claim": None, "source_ids": []}}

    def test_valid_null_has_no_locators(self):
        self.assertEqual(distiller.source_errors(self.base(), "p1", [{"id": "S1"}]), [])

    def test_non_null_content_requires_locators(self):
        card = self.base()
        card["problem"] = {"claim": "A real claim", "source_ids": []}
        self.assertTrue(any("lacks locators" in e for e in distiller.source_errors(card, "p1", [{"id": "S1"}])))

    def test_invented_locator_is_rejected(self):
        card = self.base()
        card["problem"] = {"claim": "A real claim", "source_ids": ["S99"]}
        self.assertTrue(any("invalid locators" in e for e in distiller.source_errors(card, "p1", [{"id": "S1"}])))


class CollectorFixtureTests(unittest.TestCase):
    def test_oral_and_workshop_fixture_and_entity_cleaning(self):
        collector.RETRIEVED_AT = "2026-01-01T00:00:00+00:00"
        fixture = """
        <div class="event-card"><span class="event-type-badge">Oral</span>
          <div id="event-101"></div>
          <h3 class="event-title"><a href="/virtual/2026/oral/101">A &amp; B</a></h3>
          <div class="event-abstract"><div class="abstract-text">Use <b>bold</b> &amp; x &lt; y.</div></div>
        </div>
        <div class="event-card"><span class="event-type-badge">Oral</span>
          <div id="event-83917"></div>
          <h3 class="event-title"><a href="/virtual/2026/workshop/54094">Oral Presentations</a></h3>
        </div>
        """
        records = collector.parse_cards(fixture, "ICML", 2026, "https://icml.cc/virtual/2026/events/oral", "a" * 64)
        self.assertEqual(len(records), 2)
        self.assertEqual(records[0]["title"], "A & B")
        self.assertEqual(records[0]["abstract"], "Use bold & x < y.")
        self.assertEqual(records[1]["status"], "excluded_nonpaper_event")
        self.assertEqual(records[1]["event_url"], "https://icml.cc/virtual/2026/workshop/54094")


if __name__ == "__main__":
    unittest.main(verbosity=2)
