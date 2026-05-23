# LLaMA: Open and Efficient Foundation Language Models

> 证明小而精的开源模型（7B-65B）可匹敌大闭源模型，引爆开源 LLM 生态

## 基本信息

| 项目 | 内容 |
|------|------|
| 作者 | Touvron et al. (Meta AI) |
| 年份 | 2023 |
| 会议/期刊 | arXiv |
| arXiv | https://arxiv.org/abs/2302.13971 |
| 阅读日期 | |

## 核心问题

闭源大模型成本高昂，能否用更少参数、更多数据训练出同等性能的开源模型？

## 方法/架构

- 遵循 Chinchilla optimal: 更多数据 + 更少参数
- 7B / 13B / 33B / 65B 四种规格
- 训练数据 1T-1.4T token
- RMSNorm、SwiGLU、RoPE 等架构改进

## 关键结果

- LLaMA-13B 性能匹敌 GPT-3 (175B)
- LLaMA-65B 匹敌 Chinchilla-70B 和 PaLM-540B
- 开源后引爆整个社区: Alpaca、Vicuna 等衍生模型

## 对我的启发

<!--  -->

## 相关论文

- Chinchilla (Hoffmann et al., 2022)
- LLaMA 2 (Touvron et al., 2023)

## 评分

- 重要性: ⭐⭐⭐⭐⭐
- 可读性: ⭐⭐⭐⭐
- 实践价值: ⭐⭐⭐⭐⭐
