#!/usr/bin/env python3
"""Prepare selected publication examples with original abstract units for final checking."""
import json

from distill_abstracts import BASE, save, units


def main():
    result = json.loads((BASE / "final_synthesis.json").read_text())
    sources = {p["entry_id"]: p for p in map(json.loads, (BASE / "corpus/manifest.jsonl").read_text().splitlines())}
    examples = []
    for practice in result["core_practices"]:
        for example in practice["examples"]:
            pid = example["paper_id"]
            source = sources[pid]
            source_units = units(source["abstract"])
            if not example["source_ids"] or not set(example["source_ids"]) <= {u["id"] for u in source_units}:
                raise RuntimeError(f"Invalid final example locator: {pid}")
            examples.append({"practice_id": practice["id"], "practice_name": practice["name"],
                             "general_observation": practice["source_observation"], "proposed_author_action": practice["author_action"],
                             "paper_id": pid, "title": source["title"], "source_url": source["event_url"],
                             "example": example, "source_units": source_units})
    save(BASE / "runs/final-example-check-input.json", examples)
    print(json.dumps({"examples": len(examples), "distinct_papers": len({e['paper_id'] for e in examples})}))


if __name__ == "__main__":
    main()
