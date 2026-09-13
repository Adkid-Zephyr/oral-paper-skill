#!/usr/bin/env python3
"""Build bounded, non-overlapping synthesis packets from completed cards."""
from pathlib import Path
import argparse
import json

from distill_abstracts import BASE, save


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--batch-size", type=int, default=48)
    p.add_argument("--cycles", nargs="+", help="Prepare only complete conference strata, e.g. iclr-2025 iclr-2026")
    args = p.parse_args()
    corpus = [json.loads(x) for x in (BASE / "corpus/index.jsonl").read_text().splitlines()]
    all_eligible = {x["entry_id"] for x in corpus if x["status"] == "ok"}
    eligible = {x["entry_id"] for x in corpus if x["status"] == "ok" and (not args.cycles or f"{x['venue'].lower()}-{x['year']}" in args.cycles)}
    cards = {}
    for file in (BASE / "cards").glob("*.json"):
        card = json.loads(file.read_text())
        if card["identity"]["paper_id"] in eligible:
            cards[card["identity"]["paper_id"]] = card
    if set(cards) != eligible:
        raise RuntimeError(f"Require exact full coverage before synthesis: missing={len(eligible-set(cards))}, extra={len(set(cards)-eligible)}")
    folders = BASE / "runs/synthesis-inputs"
    folders.mkdir(parents=True, exist_ok=True)
    batches = []
    for venue, year in sorted({(r["venue"], r["year"]) for r in corpus}):
        ids = sorted(pid for pid, c in cards.items() if c["identity"]["venue"] == venue and c["identity"]["year"] == year)
        for start in range(0, len(ids), args.batch_size):
            selected = ids[start:start+args.batch_size]
            bid = f"{venue.lower()}-{year}-{start // args.batch_size + 1:02d}"
            packet = {"batch_id": bid, "scope": "abstract-only extracted evidence, not full-paper audit", "cards": [
                {"identity": cards[pid]["identity"], "extraction": cards[pid]["extraction"]} for pid in selected]}
            output = folders / f"{bid}.json"
            if output.exists() and json.loads(output.read_text()) != packet:
                raise RuntimeError(f"Packet changed: {output}; preserve prior synthesis before regenerating")
            save(output, packet)
            batches.append({"batch_id": bid, "paper_ids": selected, "input_file": str(output.relative_to(BASE)), "count": len(selected)})
    assert sum(b["count"] for b in batches) == len(eligible)
    manifest = BASE / "synthesis_batches.json"
    previous = json.loads(manifest.read_text())["batches"] if manifest.exists() else []
    merged = {b["batch_id"]: b for b in previous}
    merged.update({b["batch_id"]: b for b in batches})
    merged = [merged[k] for k in sorted(merged)]
    save(manifest, {"eligible": len(all_eligible), "prepared_papers": sum(b["count"] for b in merged), "batches": merged})
    print(json.dumps({"new_prepared_papers": len(eligible), "total_prepared_papers": sum(b["count"] for b in merged), "total_batches": len(merged)}))


if __name__ == "__main__":
    main()
