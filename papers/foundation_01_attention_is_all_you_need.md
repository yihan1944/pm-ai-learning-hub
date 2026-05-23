# Attention Is All You Need

> 提出 Transformer 架构，用纯自注意力替代 RNN/LSTM，奠定所有现代 LLM 的基础

## 基本信息

| 项目 | 内容 |
|------|------|
| 作者 | Vaswani et al. |
| 年份 | 2017 |
| 会议/期刊 | NeurIPS 2017 |
| arXiv | https://arxiv.org/abs/1706.03762 |
| 阅读日期 | |

## 核心问题

序列建模依赖 RNN/LSTM，无法并行计算，训练效率低。如何设计一个完全基于注意力、可并行的序列模型？

## 方法/架构

- **Self-Attention**: Q/K/V 矩阵计算序列内元素间的相关性
- **Multi-Head Attention**: 多头并行捕捉不同子空间的信息
- **Position Encoding**: 用正弦/余弦函数编码位置信息
- **Encoder-Decoder 结构**: 6 层编码器 + 6 层解码器

## 关键结果

- WMT 翻译任务 SOTA，训练时间大幅缩短
- 证明了纯注意力机制足以完成序列到序列任务

## 对我的启发

<!-- 这篇论文对我理解 AI/做产品有什么启发？ -->

1、首先这是基于文字向量化的基础上搞的
2、讲文章、等内容向量化，而且同时也记录了文字之间的关系
3、编码器和解码器 





## 相关论文

- BERT (Devlin et al., 2018) — 只用 Encoder
- GPT (Radford et al., 2018) — 只用 Decoder

## 评分

- 重要性: ⭐⭐⭐⭐⭐
- 可读性: ⭐⭐⭐⭐
- 实践价值: ⭐⭐⭐⭐⭐
