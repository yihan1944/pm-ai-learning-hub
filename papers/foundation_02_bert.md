# BERT: Pre-training of Deep Bidirectional Transformers

> 用掩码语言模型预训练双向 Transformer，开创"预训练+微调"范式

## 基本信息

| 项目 | 内容 |
|------|------|
| 作者 | Devlin et al. |
| 年份 | 2018 |
| 会议/期刊 | NAACL 2019 |
| arXiv | https://arxiv.org/abs/1810.04805 |
| 阅读日期 | |

## 核心问题

如何利用大量无标注文本学习通用的语言表示，并迁移到下游任务？

## 方法/架构

- **MLM (Masked Language Model)**: 随机遮盖 15% 的 token，让模型预测被遮盖的词
- **NSP (Next Sentence Prediction)**: 预测两个句子是否相邻
- **双向上下文**: 与 GPT 的单向不同，BERT 同时看左右上下文

## 关键结果

- 在 11 项 NLP 任务上全面刷新 SOTA
- BERT-Large: 340M 参数，霸榜多年

## 对我的启发

<!-- 这篇论文对我理解 AI/做产品有什么启发？ -->

## 相关论文

- Attention Is All You Need (Vaswani et al., 2017)
- GPT-1 (Radford et al., 2018)

## 评分

- 重要性: ⭐⭐⭐⭐⭐
- 可读性: ⭐⭐⭐⭐
- 实践价值: ⭐⭐⭐⭐⭐
