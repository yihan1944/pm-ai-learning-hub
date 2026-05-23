# Training Compute-Optimal Large Language Models (Chinchilla)

> 修正 Scaling Laws：数据应与参数同步扩展，大部分模型都训练不足

## 基本信息

| 项目 | 内容 |
|------|------|
| 作者 | Hoffmann et al. (DeepMind) |
| 年份 | 2022 |
| 会议/期刊 | NeurIPS 2022 |
| arXiv | https://arxiv.org/abs/2203.15556 |
| 阅读日期 | |

## 核心问题

Kaplan 的 Scaling Laws 建议优先扩参数，这个结论对吗？

## 方法/架构

- 在不同参数/数据组合下训练数百个模型
- 用三种独立方法估计最优 scaling 策略
- 核心修正: 计算量翻倍时，参数和数据应各翻 2 倍

## 关键结果

- 70B 参数 + 1.4T token 的 Chinchilla 匹配 280B 的 Gopher
- 大部分现有模型（包括 GPT-3）都训练不足
- 后续模型（LLaMA、DeepSeek）都遵循 Chinchilla optimal

## 对我的启发

<!--  -->

## 相关论文

- Scaling Laws (Kaplan et al., 2020)
- LLaMA (Touvron et al., 2023) — Chinchilla 思路的实践者

## 评分

- 重要性: ⭐⭐⭐⭐⭐
- 可读性: ⭐⭐⭐⭐
- 实践价值: ⭐⭐⭐⭐⭐
