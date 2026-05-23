# PM AI System Constitution

## Core Principles

### I. Content-First
All features MUST serve the core learning content (papers, knowledge, agents, AI products). The frontend is a presentation layer for existing markdown/PDF content — it MUST NOT introduce a database or backend server. Content lives in files, not in a system.

### II. Static-Site Architecture
The project MUST be a static site (HTML/CSS/JS or static-site generator). No server-side runtime, no database, no authentication. Deployable to GitHub Pages, Vercel, or any static host. Content updates happen via git commits.

### III. Progressive Disclosure
Information architecture MUST follow progressive disclosure: overview first, details on demand. Users should be able to browse at three levels: (1) category overview, (2) item list, (3) item detail. Never dump all content on one page.

### IV. Mobile-Responsive
All pages MUST be fully usable on mobile devices (320px+). The learning experience should work on phones — users read papers and study on commutes.

### V. Content Parity
Every piece of content that exists in the markdown files MUST be accessible through the frontend. No content left behind. If a new paper or knowledge entry is added to the repo, it MUST appear in the site after rebuild.

### VI. Simplicity
Use Vue 3 as the single frontend framework with Vite as the build tool. No additional UI frameworks (no Element Plus, Ant Design, etc.) — use plain CSS or a minimal utility library. The project should be understandable by a solo developer in under 30 minutes.

## Content Structure

The site MUST organize content into these sections:
- **Papers**:论文笔记，按类别分组（基础架构、大语言模型、对齐与安全、多模态）
- **Knowledge**: 学习路线图 + 术语表
- **Agents**: Agent 框架、设计模式、项目实践
- **AI Products**: 产品案例、产品思维、Prompt 工程
- **Exam**: 面试题库

## Development Workflow

- All content changes go through markdown file edits
- Frontend changes MUST preserve content accuracy
- New features MUST be independently testable via local preview
- No external API calls — everything is self-contained

## Governance

This constitution governs all development decisions for the PM AI System frontend.
Amendments require documentation of the change, rationale, and impact assessment.
Version: 1.1.0 | Ratified: 2026-05-21 | Last Amended: 2026-05-21
