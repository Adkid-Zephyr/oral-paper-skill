#!/usr/bin/env python3
"""Prepare local, source-complete review packets; never publishes full abstracts."""
from pathlib import Path
import argparse
import json
import random
import re

from distill_abstracts import BASE, units, save


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("stage", choices=["pilot", "audit", "targeted", "flagged"])
    p.add_argument("--packet-size", type=int, default=8)
    p.add_argument("--label", default="")
    p.add_argument("--select-only", action="store_true")
    p.add_argument("--cycle", help="Review one already-selected conference stratum, e.g. iclr-2025")
    p.add_argument("--limit", type=int, default=12, help="Maximum distinct papers for a flagged-source packet")
    args = p.parse_args()
    papers = {r["entry_id"]: r for r in map(json.loads, (BASE / "corpus/manifest.jsonl").read_text().splitlines())}
    pilot = json.loads((BASE / "corpus/pilot_ids.json").read_text())["entry_ids"]
    if args.stage == "pilot":
        chosen = pilot
    elif args.stage == "audit":
        sampler = random.Random(20260913)
        chosen = []
        for venue, year in sorted({(p["venue"], p["year"]) for p in papers.values()}):
            pool = sorted(k for k, r in papers.items() if r["venue"] == venue and r["year"] == year
                          and r["status"] == "ok" and k not in pilot)
            chosen.extend(sampler.sample(pool, 6))
        selection = {"seed": 20260913, "method": "six per conference-cycle stratum, uniform without replacement, excluding pilot", "entry_ids": chosen}
        selection_path = BASE / "audit_ids.json"
        if selection_path.exists() and json.loads(selection_path.read_text()) != selection:
            raise RuntimeError("Existing audit selection differs; preserve the original sample")
        save(selection_path, selection)
    elif args.stage == "targeted":
        pattern = r"\bwill\b.{0,100}\b(releas|public|availab|open.source)"
        chosen = sorted(pid for pid, paper in papers.items() if paper["status"] == "ok"
                        and re.search(pattern, paper["abstract"] or "", re.I))
        selection = {"method": "Targeted source-text scan after the ICLR2025 random audit found future-to-completed release drift; not random and not a complete semantic audit", "pattern": pattern,
                     "trigger": "reviews/audit-iclr-2025.json", "entry_ids": chosen,
                     "scope": "Check temporal qualification of promised code/model/data release, including all matching source records."}
        selection_path = BASE / "targeted_ids.json"
        if selection_path.exists() and json.loads(selection_path.read_text()) != selection:
            raise RuntimeError("Existing targeted selection differs; preserve prior records")
        save(selection_path, selection)
    else:
        if not args.label:
            raise RuntimeError("Flagged-source review needs a unique --label")
        flags = {}
        for file in sorted((BASE / "synthesis").glob("*.json")):
            if file.name.endswith(".provenance.json"):
                continue
            for flag in json.loads(file.read_text()).get("source_checks_needed", []):
                flags.setdefault(flag["paper_id"], []).append(dict(flag, synthesis_file=file.name))
        assignments_path = BASE / "flagged_assignments.json"
        assignments = json.loads(assignments_path.read_text()) if assignments_path.exists() else {}
        if args.label in assignments:
            chosen = assignments[args.label]
        else:
            assigned = {pid for ids in assignments.values() for pid in ids}
            chosen = [pid for pid in flags if pid not in assigned][:args.limit]
            if not chosen:
                print(json.dumps({"stage": "flagged", "unassigned_ready": 0}))
                return
            assignments[args.label] = chosen
            save(assignments_path, assignments)
    if args.select_only:
        print(json.dumps({"stage": args.stage, "selected": len(chosen), "extraction_outputs_inspected": False}))
        return
    if args.cycle:
        chosen = [pid for pid in chosen if f"{papers[pid]['venue'].lower()}-{papers[pid]['year']}" == args.cycle]
        if not chosen:
            raise RuntimeError(f"No selected records in cycle {args.cycle}")
    entries = []
    for pid in chosen:
        card_path = BASE / "cards" / f"{pid}.json"
        if not card_path.exists():
            raise RuntimeError(f"Card not completed: {pid}")
        entries.append({"identity": {k: papers[pid][k] for k in ("entry_id", "title", "venue", "year", "event_url")},
                        "source_units": units(papers[pid]["abstract"]),
                        "card": json.loads(card_path.read_text()),
                        "specific_flags": flags.get(pid, []) if args.stage == "flagged" else []})
    suffix = "-" + args.label if args.label else ""
    if args.cycle:
        suffix += "-" + args.cycle
    folder = BASE / "runs" / f"{args.stage}-source-review{suffix}"
    folder.mkdir(parents=True, exist_ok=True)
    for i in range(0, len(entries), args.packet_size):
        output = folder / f"packet-{i // args.packet_size + 1:02d}.json"
        packet = entries[i:i+args.packet_size]
        if output.exists() and json.loads(output.read_text()) != packet:
            raise RuntimeError(f"Existing packet differs: {output}; use a new --label to preserve evidence")
        save(output, packet)
    print(json.dumps({"stage": args.stage, "cards": len(entries), "packet_dir": str(folder)}))


if __name__ == "__main__":
    main()
