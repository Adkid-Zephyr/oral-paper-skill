#!/usr/bin/env python3
"""Collect the six official Oral event indexes.

The conference pages contain the complete event cards (including abstracts),
so the default run makes one request per source page and keeps those pages in
corpus/raw for provenance.  It deliberately does not query model APIs.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "research" / "abstract_distillation" / "corpus"

SOURCES = [
    ("ICLR", 2025, "https://iclr.cc/virtual/2025/events/oral"),
    ("ICLR", 2026, "https://iclr.cc/virtual/2026/events/oral"),
    ("ICML", 2025, "https://icml.cc/virtual/2025/events/oral"),
    ("ICML", 2026, "https://icml.cc/virtual/2026/events/oral"),
    ("NeurIPS", 2024, "https://neurips.cc/virtual/2024/events/oral"),
    ("NeurIPS", 2025, "https://neurips.cc/virtual/2025/events/oral"),
]


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "oral-corpus-research/1.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def parse_cards(text: str, venue: str, year: int, source_url: str, digest: str) -> list[dict]:
    # The card contains nested divs, so the non-greedy expression above can
    # stop early. Split at card starts and use the next card as the boundary.
    chunks = re.split(r'(?=<div class="event-card\b)', text)[1:]
    records = []
    for chunk in chunks:
        if 'event-type-badge">Oral<' not in chunk[:2500]:
            continue
        mid = re.search(r'id="event-(\d+)"', chunk)
        title = re.search(r'<h3 class="event-title">\s*<a href="([^"]+)">(.*?)</a>', chunk, re.S)
        abstract = re.search(r'<div class="abstract-text"[^>]*>\s*(.*?)\s*</div>', chunk, re.S)
        if not mid or not title:
            continue
        event_id = mid.group(1)
        event_url = urllib.parse.urljoin(source_url, title.group(1))
        abstract_text = clean(re.sub(r"<[^>]+>", " ", abstract.group(1))) if abstract else ""
        is_nonpaper = venue == "ICML" and year == 2026 and event_id == "83917"
        records.append({
            "entry_id": f"{venue.lower()}-{year}-oral-{event_id}",
            "venue": venue,
            "year": year,
            "title": clean(title.group(2)),
            "source_url": source_url,
            "event_url": event_url,
            "paper_url": None,
            "abstract": abstract_text or None,
            "retrieved_at": RETRIEVED_AT,
            "source_sha256": digest,
            "reading_level": "abstract_only" if abstract_text else None,
            "status": "excluded_nonpaper_event" if is_nonpaper else ("ok" if abstract_text else "missing_abstract"),
            "status_rationale": "Official Oral index card resolves to a Workshop/session event, not a paper record." if is_nonpaper else None,
        })
    return records


def choose_pilot(records: list[dict]) -> dict:
    """Select one record from each actual combined-text-length quartile (purposive)."""
    keywords = ("theory", "language", "vision", "reinforcement", "diffusion", "graph", "optimization")
    selected = []
    details = {}
    for venue, year, _ in SOURCES:
        group = [r for r in records if r["venue"] == venue and r["year"] == year and r["status"] == "ok"]
        group.sort(key=lambda r: (len(r["title"]) + len(r["abstract"] or ""), r["entry_id"]))
        bins = [[] for _ in range(4)]
        for index, record in enumerate(group):
            bins[min(3, index * 4 // len(group))].append(record)
        candidates, used_topics = [], set()
        for pool in bins:
            # Topic cues break ties within each length quartile; this remains
            # purposive selection and is explicitly not representative.
            def score(record):
                cues = {k for k in keywords if k in (record["title"] + " " + (record["abstract"] or "")).lower()}
                return (len(cues & used_topics), len(cues), record["entry_id"])
            chosen = sorted(pool, key=score)[0]
            candidates.append(chosen)
            used_topics.update(k for k in keywords if k in (chosen["title"] + " " + (chosen["abstract"] or "")).lower())
        candidates = sorted(candidates, key=lambda r: r["entry_id"])
        selected.extend(r["entry_id"] for r in candidates)
        details[f"{venue}-{year}"] = [r["entry_id"] for r in candidates]
    return {"selection_method": "deterministic purposive stratification: one per actual combined title/abstract character-count quartile in each cycle, with distinct topical-cue preference; not random or representative", "entry_ids": selected, "by_cycle": details}


def main() -> int:
    global RETRIEVED_AT
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", action="store_true", help="reuse existing raw source files")
    args = parser.parse_args()
    build_at = datetime.now(timezone.utc).isoformat()
    RETRIEVED_AT = build_at
    raw_dir = OUT / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    prior_times = {}
    old_manifest = OUT / "manifest.jsonl"
    if args.offline and old_manifest.exists():
        for line in old_manifest.read_text(encoding="utf-8").splitlines():
            old = json.loads(line)
            if old.get("source_sha256") and old.get("retrieved_at"):
                prior_times[old["source_sha256"]] = old["retrieved_at"]
    records = []
    source_report = []
    for venue, year, url in SOURCES:
        raw_path = raw_dir / f"{venue.lower()}-{year}-oral.html"
        try:
            data = raw_path.read_bytes() if args.offline and raw_path.exists() else fetch(url)
            raw_path.write_bytes(data)
            digest = hashlib.sha256(data).hexdigest()
            parsed = parse_cards(data.decode("utf-8", errors="replace"), venue, year, url, digest)
            for record in parsed:
                record["retrieved_at"] = prior_times.get(digest, record["retrieved_at"])
            records.extend(parsed)
            source_report.append({"venue": venue, "year": year, "url": url, "raw_file": str(raw_path.relative_to(ROOT)), "sha256": digest, "bytes": len(data), "records": len(parsed), "ok": True})
        except Exception as exc:
            source_report.append({"venue": venue, "year": year, "url": url, "raw_file": str(raw_path.relative_to(ROOT)), "records": 0, "ok": False, "error": repr(exc)})
    records.sort(key=lambda r: (r["venue"], r["year"], r["entry_id"]))
    manifest = OUT / "manifest.jsonl"
    with manifest.open("w", encoding="utf-8") as fh:
        for record in records:
            fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
    # A redistributable index: keep provenance and measurable text metadata,
    # but never duplicate full abstracts outside the local research manifest.
    public_index = OUT / "index.jsonl"
    with public_index.open("w", encoding="utf-8") as fh:
        for record in records:
            public = {k: record[k] for k in ("entry_id", "venue", "year", "title", "source_url", "event_url", "paper_url", "retrieved_at", "source_sha256", "reading_level", "status")}
            abstract = record["abstract"] or ""
            public["abstract_chars"] = len(abstract)
            public["abstract_sha256"] = hashlib.sha256(abstract.encode("utf-8")).hexdigest() if abstract else None
            fh.write(json.dumps(public, ensure_ascii=False, separators=(",", ":")) + "\n")
    normalized = {}
    for record in records:
        key = (re.sub(r"\W+", "", record["title"].lower()), re.sub(r"\s+", " ", record["abstract"] or "").strip().lower())
        normalized.setdefault(key, []).append(record["entry_id"])
    duplicates = [ids for ids in normalized.values() if len(ids) > 1]
    pilot = choose_pilot(records)
    (OUT / "pilot_ids.json").write_text(json.dumps(pilot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {"built_at": build_at, "source_report": source_report, "counts": {"total": len(records), "eligible": sum(r["status"] == "ok" for r in records), "excluded_nonpaper_event": sum(r["status"] == "excluded_nonpaper_event" for r in records), "missing_abstract": sum(r["status"] == "missing_abstract" for r in records), "failed_sources": sum(not s["ok"] for s in source_report), "duplicate_groups": len(duplicates)}, "historical_counts": {f"{v}-{y}": n for (v, y, _), n in zip(SOURCES, (213, 223, 120, 169, 72, 87))}, "duplicate_entry_ids": duplicates}
    (OUT / "collection_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary["counts"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
