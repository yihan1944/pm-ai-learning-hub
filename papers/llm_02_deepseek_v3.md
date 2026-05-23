# DeepSeek-V3 Technical Report

> 671B MoE 模型，$5.5M 训练成本达到前沿性能，DeepSeek 的里程碑之作

## 基本信息

| 项目 | 内容 |
|------|------|
| 作者 | DeepSeek-AI |
| 年份 | 2024 |
| 会议/期刊 | arXiv |
| arXiv | https://arxiv.org/abs/2412.19437 |
| 阅读日期 | |

## 核心问题

如何在有限算力预算下训练出与 GPT-4 级别匹敌的大模型？

## 方法/架构

- **671B 总参数，37B 激活** — MoE 架构
- **MLA (Multi-head Latent Attention)** — 低秩压缩 KV Cache
- **DeepSeekMoE** — 细粒度专家 + 共享专家
- **辅助损失自由负载均衡** — 无需额外损失项
- **Multi-Token Prediction** — 多 token 预测训练目标
- FP8 混合精度训练，2048 H800 GPU

## 关键结果

- 训练成本仅 $5.5M，远低于同等水平闭源模型
- 在多项基准上匹敌 GPT-4o 和 Claude 3.5 Sonnet
- 开源，震动整个 AI 行业

## 对我的启发

<!-- 这篇论文对我理解 AI/做产品有什么启发？ -->

## 相关论文

- DeepSeek-V2 (2405.04434)
- DeepSeekMoE (2401.06066)
- DeepSeek-R1 (2501.12948)

## 评分

- 重要性: ⭐⭐⭐⭐⭐
- 可读性: ⭐⭐⭐⭐
- 实践价值: ⭐⭐⭐⭐⭐
