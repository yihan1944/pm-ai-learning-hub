# Language Models are Few-Shot Learners (GPT-3)

> 175B 参数模型展示上下文学习能力，引爆现代 LLM 竞赛

## 基本信息

| 项目 | 内容 |
|------|------|
| 作者 | Brown et al. (OpenAI) |
| 年份 | 2020 |
| 会议/期刊 | NeurIPS 2020 |
| arXiv | https://arxiv.org/abs/2005.14165 |
| 阅读日期 | |

## 核心问题

语言模型规模扩大后，是否能不微调就完成各种任务？

## 方法/架构

- **175B 参数**，96 层 Transformer decoder
- **In-Context Learning**: 在 prompt 中给几个示例，模型就能完成任务
- **无需微调**: 零样本/少样本即可完成翻译、问答、推理等

## 关键结果

- 在多项 NLP 基准上达到 SOTA
- 发现了规模带来的涌现能力（emergent abilities）

## 对我的启发

<!-- 这篇论文对我理解 AI/做产品有什么启发？ -->

## 相关论文

- Scaling Laws (Kaplan et al., 2020)
- InstructGPT (Ouyang et al., 2022)

## 评分

- 重要性: ⭐⭐⭐⭐⭐
- 可读性: ⭐⭐⭐⭐
- 实践价值: ⭐⭐⭐⭐⭐
