# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

PM AI Learning Hub — a Vue 3 + TypeScript static site for an AI Product Manager's learning resources (academic papers, learning paths, glossary, interview questions, product case studies, agent resources). Content is in Chinese. Deployed to `ai.viewe.cn` via GitHub Pages.

## Build & Development

The project has a **two-phase build pipeline**:

1. **Content build**: `python build.py` — converts Markdown files in `papers/`, `knowledge/`, `exam/`, `products/` into JSON in `src/data/` (gitignored). Also copies PDFs to `public/pdf/`.
2. **App build**: `npm run build` — type-checks with `vue-tsc`, then bundles with Vite.

**You must run `python build.py` before the frontend will work** — `src/data/` is gitignored and does not exist in a fresh clone.

| Command | Purpose |
|---------|---------|
| `python build.py` | Generate JSON data from Markdown content |
| `npm run dev` | Start Vite dev server |
| `npm run build` | Type-check + production build |
| `npm run preview` | Preview production build locally |

There are no test or lint scripts configured.

Python dependency: `pip install markdown` (used by build.py).

## Architecture

**Static site, no backend.** All content is imported as JSON modules at build time — no API calls, no runtime data fetching.

```
Markdown files → build.py → JSON (src/data/) → Vue components (static imports)
```

**Key directories:**
- `papers/` — Academic paper notes in Markdown, organized by category (foundation, LLM, alignment, multimodal)
- `knowledge/` — Learning path stages + glossary
- `exam/` — Interview Q&A in Markdown
- `products/` — Product catalog
- `agents/` — Agent resources (placeholder content)
- `src/` — Vue 3 SPA source

**Frontend stack:** Vue 3 Composition API (`<script setup lang="ts">`), Vue Router (hash-based), `marked` for markdown rendering, plain scoped CSS with custom properties (no UI framework). Dark theme defined via CSS variables in `src/assets/style.css`.

**Key composables:**
- `useProgress.ts` — Learning progress tracking via `localStorage`
- `useSearch.ts` — Client-side search against pre-built JSON index

**Routing:** Hash-based (`createWebHashHistory`), 8 routes, all lazy-loaded. Routes: `/`, `/papers`, `/papers/:id`, `/knowledge`, `/agents`, `/products`, `/exam`, `/search`.

**Vite config note:** `base` is conditional — `/` for custom domain builds (`CUSTOM_DOMAIN` env var), `/pm-ai-learning-hub/` for GitHub Pages.

## Content Model (TypeScript interfaces in `src/types/index.ts`)

- `Paper` — id, title, category, date, summary, tags, contentHtml, pdfUrl
- `LearningStage` — id, title, description, items (with completed state)
- `GlossaryTerm` — term, definition
- `ExamQuestion` — id, category, question, answer
- `AgentResource` — id, category, title, description, url
- `SearchItem` — id, type, title, content, url

## Project Principles (from constitution)

These govern all development decisions:

1. **Content-First** — Frontend is a presentation layer for markdown/PDF content. No database, no backend.
2. **Static-Site Architecture** — Deployable to any static host. Content updates via git commits.
3. **Progressive Disclosure** — Three levels: category overview → item list → item detail.
4. **Mobile-Responsive** — Must work on 320px+ screens.
5. **Content Parity** — Every piece of content in markdown must be accessible through the frontend after rebuild.
6. **Simplicity** — No additional UI frameworks. Plain CSS only. Solo-developer comprehensible in under 30 minutes.

## Deployment

GitHub Actions (`.github/workflows/deploy.yml`): on push to `master`, runs `python build.py` → `npm run build` → deploys `dist/` to GitHub Pages. Custom domain: `ai.viewe.cn` (CNAME file).
