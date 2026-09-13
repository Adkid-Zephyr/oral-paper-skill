#!/usr/bin/env python3
"""Check durable extraction evidence; never equates these checks with user benefit."""
import argparse
from collections import Counter
import json

import jsonschema
from distill_abstracts import BASE, digest, now, save, source_errors, units


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--allow-partial", action="store_true")
    args = p.parse_args()
    corpus = [json.loads(x) for x in (BASE / "corpus/manifest.jsonl").read_text().splitlines()]
    sources = {r["entry_id"]: r for r in corpus if r["status"] == "ok"}
    schema = json.loads((BASE / "extraction.schema.json").read_text())
    cards = {}
    errors = []
    counts = Counter()
    normalizations, corrections = 0, 0
    for path in (BASE / "cards").glob("*.json"):
        try:
            card = json.loads(path.read_text())
            pid = card["identity"]["paper_id"]
            if pid in cards or pid not in sources:
                raise ValueError("Duplicate or ineligible identity")
            source = sources[pid]
            source_units = units(source["abstract"])
            jsonschema.validate(card["extraction"], schema)
            issues = source_errors(card["extraction"], pid, source_units)
            if issues:
                raise ValueError(issues)
            if card["provenance"]["abstract_sha256"] != digest(source["abstract"]):
                raise ValueError("Abstract hash mismatch")
            if card["source_units"] != [{"id": u["id"], "sha256": digest(u["text"])} for u in source_units]:
                raise ValueError("Source unit/hash mismatch")
            if card["identity"]["title"] != source["title"] or card["identity"]["source_url"] != source["event_url"]:
                raise ValueError("Title or source URL mismatch")
            cards[pid] = card
            counts[f"{source['venue']}-{source['year']}"] += 1
            normalizations += bool(card["provenance"].get("normalizations"))
            corrections += bool(card.get("editorial_revisions"))
        except (ValueError, KeyError, jsonschema.ValidationError) as exc:
            errors.append({"file": path.name, "error": str(exc)[:500]})
    missing = sorted(set(sources) - set(cards))
    ledger = [json.loads(x) for x in (BASE / "call_ledger.jsonl").read_text().splitlines()]
    known_usage, missing_usage = Counter(), Counter()
    for row in ledger:
        usage = row.get("usage") or {}
        for key in ("input_tokens", "cached_input_tokens", "output_tokens", "reasoning_output_tokens"):
            if key in usage:
                known_usage[key] += usage[key]
            else:
                missing_usage[key] += 1
    report = {"checked_at": now(), "scope": "Packaging, source identity/hash and locator consistency, not semantic truth or user benefit",
              "indexed_records": len(corpus), "excluded_nonpaper_events": sum(r["status"] == "excluded_nonpaper_event" for r in corpus),
              "eligible_abstracts": len(sources), "valid_cards": len(cards), "missing_ids": missing,
              "counts_by_cycle": dict(sorted(counts.items())), "errors": errors,
              "cards_with_null_normalization": normalizations, "cards_with_source_review_corrections": corrections,
              "extraction_call_records": len(ledger), "first_outcomes": dict(Counter(r["status"] for r in ledger)),
              "known_extraction_token_totals": dict(known_usage), "missing_usage_field_call_counts": dict(missing_usage),
              "status": "FAIL" if errors else "PARTIAL" if missing else "PASS"}
    save(BASE / "verification.json", report)
    print(json.dumps({k: report[k] for k in ("status", "indexed_records", "eligible_abstracts", "valid_cards", "counts_by_cycle", "errors")}))
    return 1 if errors or (missing and not args.allow_partial) else 0


if __name__ == "__main__":
    main()
