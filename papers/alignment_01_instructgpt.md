# Training Language Models to Follow Instructions with Human Feedback (InstructGPT)

> 将 RLHF 扩展到 GPT-3，ChatGPT 的技术蓝图

## 基本信息

| 项目 | 内容 |
|------|------|
| 作者 | Ouyang et al. (OpenAI) |
| 年份 | 2022 |
| 会议/期刊 | NeurIPS 2022 |
| arXiv | https://arxiv.org/abs/2203.02155 |
| 阅读日期 | |

## 核心问题

大模型生成的内容不一定符合用户意图，如何让模型"听话"？

## 方法/架构

- **三步走**: SFT → 训练奖励模型 → PPO 强化学习
- **SFT**: 用人工标注的指令-回复对微调
- **奖励模型**: 从人类偏好比较中学习打分
- **PPO**: 用 RL 优化模型，使其输出高奖励内容

## 关键结果

- 1.3B 参数的 RLHF 模型比 175B 的 GPT-3 更受人类偏好
- 奠定了 ChatGPT 的技术基础

## 对我的启发

<!-- 这篇论文对我理解 AI/做产品有什么启发？ -->

原来是这么回事啊

1、首先用问答对来进行训练
2、用奖励模型来调优
3、用RL来规范输出高奖励的内容


## 相关论文

- Deep Reinforcement Learning from Human Preferences (Christiano et al., 2017)
- DPO (Rafailov et al., 2023) — 简化版对齐

## 评分

- 重要性: ⭐⭐⭐⭐⭐
- 可读性: ⭐⭐⭐⭐
- 实践价值: ⭐⭐⭐⭐⭐
