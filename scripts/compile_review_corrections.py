#!/usr/bin/env python3
"""Collect explicit reviewer replacement values, preserving conflicts for judgment."""
import argparse
import json
from pathlib import Path

from distill_abstracts import BASE, save


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("reviews", nargs="+", type=Path)
    p.add_argument("--output", type=Path, required=True)
    args = p.parse_args()
    result = json.loads(args.output.read_text()) if args.output.exists() else {
        "review_type": "Explicit source-review replacement values; first-pass findings remain in review files", "corrections": []}
    existing = {(x["paper_id"], x["field"]): x for x in result["corrections"]}
    added = 0
    for file in args.reviews:
        review = json.loads(file.read_text())
        for record in review["records"]:
            for finding in record.get("findings", []):
                if "replacement_value" not in finding or finding["field"].startswith("synthesis:"):
                    continue
                change = {"paper_id": record["paper_id"], "field": finding["field"],
                          "value": finding["replacement_value"], "review": str(file.resolve().relative_to(BASE))}
                key = change["paper_id"], change["field"]
                if key in existing:
                    if existing[key]["value"] != change["value"]:
                        raise RuntimeError(f"Conflicting corrections: {key}")
                    continue
                result["corrections"].append(change)
                existing[key] = change
                added += 1
    save(args.output, result)
    print(json.dumps({"added": added, "total_explicit_replacements": len(existing)}))


if __name__ == "__main__":
    main()
