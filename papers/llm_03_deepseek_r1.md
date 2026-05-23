# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL

> 用 RL 激发 LLM 推理能力，对标 OpenAI o1，发表于 Nature

## 基本信息

| 项目 | 内容 |
|------|------|
| 作者 | DeepSeek-AI |
| 年份 | 2025 |
| 会议/期刊 | Nature volume 645, pages 633-638 |
| arXiv | https://arxiv.org/abs/2501.12948 |
| 阅读日期 | |

## 核心问题

如何让 LLM 具备真正的推理能力（思维链），而不是简单的模式匹配？

## 方法/架构

- **DeepSeek-R1-Zero**: 纯 RL 训练，无需 SFT 数据，模型自发学会推理
- **GRPO (Group Relative Policy Optimization)**: 无需 critic 模型的高效 RL
- **两阶段训练**: 先用推理数据 SFT，再用 RL 强化推理能力
- **蒸馏**: 将推理能力蒸馏到小模型 (1.5B-70B)

## 关键结果

- 在数学、代码、推理任务上匹配 OpenAI o1
- R1-Zero 证明纯 RL 可以自发涌现推理能力
- 完全开源，蒸馏模型性能优秀

## 对我的启发

<!-- 这篇论文对我理解 AI/做产品有什么启发？ -->

## 相关论文

- DeepSeek-V3 (2412.19437)
- DeepSeekMath (2402.03300) — GRPO 算法来源
- InstructGPT (Ouyang et al., 2022) — RLHF 对比

## 评分

- 重要性: ⭐⭐⭐⭐⭐
- 可读性: ⭐⭐⭐⭐
- 实践价值: ⭐⭐⭐⭐⭐
