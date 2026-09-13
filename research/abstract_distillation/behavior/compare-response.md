*示例性改写，基于已发表摘要，非作者认可版本（113词）：*

We introduce OLMoE, a fully open family of sparse Mixture-of-Experts language models, together with analyses of MoE training and routing. OLMoE-1B-7B contains 7 billion parameters and activates 1 billion per input token. We pretrain it on 5 trillion tokens and further adapt it into OLMoE-1B-7B-Instruct. In the reported evaluations, our models outperform available models with similar active parameter counts and surpass larger models including Llama2-13B-Chat and DeepSeekMoE-16B. Beyond model performance, we report findings on MoE training and introduce and analyze routing properties that reveal high specialization in OLMoE. We release model weights, training data, code, and logs to support further study of MoE training and routing.

最重要的两处调整：

1. **把贡献拆清楚，并说明开放材料的用途。** 将模型、训练与路由分析、开放材料分别写明，用具体内容替代笼统的“novel findings”。可借鉴 [AgentGym-RL](https://iclr.cc/virtual/2026/oral/10008786) 摘要 S3–S4、S7–S8：它分别交代框架与训练方法，帮助读者辨认贡献之间的关系。这里“支持进一步研究”是对材料用途的表述，不代表已验证下游收益；原摘要未提供具体训练发现，因此没有补写。

2. **让性能比较紧邻其条件。** 保留总参数、每 token 激活参数及预训练 token 数，将性能结论限定于所报告的评测，避免把激活参数接近理解为总成本相同。可借鉴 [daVinci-Dev](https://icml.cc/virtual/2026/oral/71032) 摘要 S4：它同时说明共同的基座与 scaffold，以及不同的训练 token 预算。OLMoE 原摘要未给出这些控制条件，不能照搬，也不能据此新增延迟或端到端效率结论。
