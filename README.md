# PM AI Learning Hub

AI 产品经理学习资源站，汇集学术论文笔记、学习路径、术语表、面试题库、产品案例和 Agent 资源。

🔗 访问地址：[ai.viewe.cn](https://ai.viewe.cn)

## 功能模块

| 模块 | 说明 |
|------|------|
| 📚 学术论文 | 按类别整理的 AI 论文笔记（基础、大语言模型、对齐、多模态） |
| 🗺️ 学习路径 | 10 阶段 AI 学习规划，支持进度追踪 |
| 📖 术语表 | AI 领域核心概念速查 |
| 📝 面试题库 | AI 产品经理面试题与答案 |
| 🛍️ 产品案例 | 个人项目与产品展示 |
| 🤖 Agent 资源 | AI Agent 相关资源（建设中） |

## 技术栈

- **前端**：Vue 3 + TypeScript + Vue Router + Vite
- **内容**：Markdown 文件 + Python 构建脚本
- **样式**：原生 CSS + CSS Variables（支持暗色主题）
- **部署**：GitHub Pages → ai.viewe.cn

## 本地开发

```bash
# 1. 安装依赖
npm install
pip install markdown

# 2. 生成内容数据
python build.py

# 3. 启动开发服务器
npm run dev

# 4. 构建生产版本
npm run build
```

## 项目结构

```
├── papers/          # 学术论文笔记 (Markdown)
├── knowledge/       # 学习路径与术语表
├── exam/            # 面试题库
├── products/        # 产品目录
├── agents/          # Agent 资源
├── src/             # Vue 应用源码
│   ├── components/  # 组件
│   ├── views/       # 页面视图
│   ├── composables/ # 组合式函数
│   ├── data/        # 构建生成的 JSON (gitignore)
│   └── types/       # TypeScript 类型定义
├── build.py         # 内容构建脚本
└── .github/workflows/deploy.yml  # CI/CD 配置
```

## 内容更新

1. 在对应目录添加/编辑 Markdown 文件
2. 运行 `python build.py` 重新生成数据
3. 提交并推送到 `master` 分支
4. GitHub Actions 自动构建部署

## License

MIT
