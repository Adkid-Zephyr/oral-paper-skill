#!/usr/bin/env python3
"""Apply explicitly source-reviewed field corrections with a retained edit trail."""
import argparse
import json
from pathlib import Path
import re

from distill_abstracts import BASE, digest, now, save, source_errors, units


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("corrections", type=Path)
    args = p.parse_args()
    changes = json.loads(args.corrections.read_text())["corrections"]
    sources = {r["entry_id"]: r for r in map(json.loads, (BASE / "corpus/manifest.jsonl").read_text().splitlines())}
    changed = set()
    for change in changes:
        file = BASE / "cards" / (change["paper_id"] + ".json")
        card = json.loads(file.read_text())
        field = [int(x) if x.isdigit() else x for x in re.findall(r"[^.\[\]]+", change["field"])]
        parent = card["extraction"]
        for key in field[:-1]:
            parent = parent[key]
        old = parent[field[-1]]
        if old == change["value"]:
            continue
        review_path = BASE / change["review"]
        if not review_path.exists():
            raise RuntimeError(f"Missing source review: {review_path}")
        parent[field[-1]] = change["value"]
        errors = source_errors(card["extraction"], change["paper_id"], units(sources[change["paper_id"]]["abstract"]))
        if errors:
            raise RuntimeError(errors)
        card.setdefault("editorial_revisions", []).append({"field": change["field"], "before": old,
            "after": change["value"], "review_file": change["review"],
            "review_sha256": digest(review_path.read_text()), "applied_at": now(),
            "note": "Source-reviewed correction; initial generated response remains in local run logs."})
        save(file, card)
        changed.add(change["paper_id"])
    print(json.dumps({"corrected_cards": len(changed), "specified_changes": len(changes)}))


if __name__ == "__main__":
    main()
