# Evidence base and reusable Oral patterns

This reference records why the skill's guidance exists. It is not a list of phrases to copy.

## Corpus boundary

The skill was revised on 2026-09-02 using the latest completed cycles available at that date:

- ICLR 2025: 213 official Oral entries;
- ICLR 2026: 223;
- ICML 2025: 120;
- ICML 2026: 169;
- NeurIPS 2024: 72;
- NeurIPS 2025: 87.

Total: 884 official Oral entries. The analysis extracted 883 available abstracts; one ICML 2026 entry lacked an abstract in the event page. It analyzed the full abstract corpus and deep-read a stratified set of Oral/award papers across method, theory, empirical mechanism, systems, benchmark/data, and position work. It did not claim to read every paper's full PDF.

Simple lexical checks over the abstracts found that approximately 80% explicitly state a gap or contrast and approximately 80% explicitly introduce a proposed contribution. About 38% contain an easily detected quantitative result. These are approximate corpus diagnostics, not quality labels. They show that numerical SOTA is not a universal Oral template.

Official lists:

- https://iclr.cc/virtual/2025/events/oral
- https://iclr.cc/virtual/2026/events/oral
- https://icml.cc/virtual/2025/events/oral
- https://icml.cc/virtual/2026/events/oral
- https://neurips.cc/virtual/2024/events/oral
- https://neurips.cc/virtual/2025/events/oral

## What award committees explicitly valued

These are stronger signals than guessing why a paper received an Oral slot.

### ICLR

The ICLR 2025 Outstanding Paper committee named theoretical insight, practical impact, exceptional writing, and experimental rigor as ranking factors.

The ICLR 2026 committee praised:

- a strong conceptual message that could stimulate new theoretical and empirical investigation;
- a dissonant gap between training and deployment;
- exceptional experimental design and methodology;
- fresh findings in an important real-world setting;
- a principled general methodology even when empirical improvements were modest.

Sources:

- https://blog.iclr.cc/2025/04/22/announcing-the-outstanding-paper-awards-at-iclr-2025/
- https://blog.iclr.cc/2026/04/23/announcing-the-iclr-2026-outstanding-papers/

### ICML

The ICML 2026 award process explicitly used strong-accept quality, nontrivial longevity potential, and interest beyond a niche subcommunity. Its paper notes praised counter-intuitive challenges to dominant assumptions, non-obvious failure modes, and settlement of long-standing questions. Position papers were valued for important neglected issues, clear evidential support, serious treatment of alternatives, and practical calls to action.

Source:

- https://blog.icml.cc/2026/07/05/announcing-the-icml-2026-awards/

### NeurIPS

The NeurIPS 2025 selection reflections praised several different routes to impact:

- a benchmark that advances scientific understanding and addresses societal challenges rather than only technical performance;
- a simple, widely implementable change backed by extensive evidence and mechanistic analysis;
- a controlled toy model that explains a real large-model phenomenon;
- a definitive negative result against a widely accepted assumption;
- an elegant tight solution to a decades-old open problem.

Sources:

- https://blog.neurips.cc/2024/12/10/announcing-the-neurips-2024-best-paper-awards/
- https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/

## Cross-venue commonality

Across archetypes, strong papers repeatedly do four things:

1. **One irreducible claim:** They compress the work into a conceptual wager, not an inventory of contributions.
2. **Reader-visible proof:** The main theorem, figure, counterexample, table, or end-to-end result makes the wager legible early.
3. **Adversarial evidence:** The evidence targets the strongest plausible alternative, not merely a weak baseline.
4. **Lasting lesson:** The paper leaves a mechanism, principle, bound, practical rule, or new scientific object that can outlive current leaderboards.

Additional factors repeatedly named by committees are experimental rigor, exceptional clarity, practical impact, conceptual insight, broad interest, and longevity potential.

## Myths the corpus does not support

- **“Every strong paper needs a huge benchmark.”** False; theory and conceptual papers can win through tight resolution and broad implications.
- **“Every Oral is a SOTA method paper.”** False; negative findings, position papers, empirical mechanisms, and principled methods with modest gains are recognized.
- **“A flashy Figure 1 is mandatory.”** False; the universal need is an early proof carrier. For theory this may be a theorem or counterexample.
- **“More experiments always make the paper stronger.”** False; committees repeatedly praise carefully designed evidence and clear methodology, not volume alone.
- **“Copying hot topics raises acceptance odds.”** Unsupported. Topic crowding raises the burden of differentiation.
- **“Oral or award status reveals a deterministic recipe.”** False; selection is heterogeneous, expert-dependent, and partly subjective.

## Reusable precedents

- **Counter-intuitive reframe:** The Flexibility Trap; LLMs Get Lost in Multi-Turn Conversation.
- **Simple change, extensive evidence, likely adoption:** Gated Attention for LLMs.
- **Mechanism from controlled model to real systems:** Superposition Yields Robust Neural Scaling; Why Diffusion Models Don't Memorize.
- **Definitive negative finding:** Does Reinforcement Learning Really Incentivize Reasoning Capacity Beyond the Base Model?
- **Long-standing theoretical resolution:** Optimal Mistake Bounds for Transductive Online Learning; High-Accuracy Sampling for Diffusion Models.
- **Benchmark that produces scientific insight:** Artificial Hivemind; CyberGym; SWE-bench.
- **Principled method despite modest gains:** The Polar Express.
- **Deployment mismatch:** Gaia2; LLMs Get Lost in Multi-Turn Conversation.
