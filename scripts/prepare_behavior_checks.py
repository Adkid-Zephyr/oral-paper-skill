#!/usr/bin/env python3
"""Create fresh-context usage checks, without supplying intended answers."""
import json

from distill_abstracts import BASE, ROOT, save, units


def main():
    sources = {p["entry_id"]: p for p in map(json.loads, (BASE / "corpus/manifest.jsonl").read_text().splitlines())}
    final = json.loads((BASE / "final_synthesis.json").read_text())
    example_ids = {e["paper_id"] for r in final["core_practices"] for e in r["examples"]}
    originals = [{"paper_id": pid, "title": sources[pid]["title"], "source_url": sources[pid]["event_url"],
                  "source_units": units(sources[pid]["abstract"])} for pid in sorted(example_ids)]
    skill_dir = ROOT / "skills/oral-paper-skill"
    common = {"skill": (skill_dir / "SKILL.md").read_text(),
              "references": {p.name: p.read_text() for p in (skill_dir / "references").glob("*.md")},
              "original_abstract_examples": originals}
    target = sources["iclr-2025-oral-31734"]
    compare = dict(common, test_context="A usage demonstration using a real published abstract; this is not the user's manuscript and not an author-approved revision.",
        user_request="使用提供的 Oral Paper Skill 帮我把这段摘要的贡献表达写得更清楚。直接给一个不超过150个英文单词的改写，再用中文解释最重要的两处调整和可借鉴的论文做法。",
        supplied_draft={"title": target["title"], "source_url": target["event_url"], "abstract": target["abstract"]})
    learn = dict(common, test_context="Synthetic early-idea scenario for a real model-invocation behavior check; not experimental evidence.",
        user_request="使用提供的 Oral Paper Skill。我想研究按查询意图复用检索片段，减少RAG问答时延，现在只有想法，没有实验结果。用一个相关论文范例教我怎样设计第一轮对照，并给我一个小练习。中文回答，控制在500字左右。")
    save(BASE / "runs/behavior-compare-input.json", compare)
    save(BASE / "runs/behavior-learn-input.json", learn)
    print(json.dumps({"fresh_context_tasks": 2, "original_example_abstracts_supplied": len(originals), "intended_answers_supplied": False}))


if __name__ == "__main__":
    main()
