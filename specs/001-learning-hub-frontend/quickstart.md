# Quickstart: AI Learning Hub Frontend (Vue 3)

## Prerequisites

- Node.js 18+
- Python 3.11+
- A modern web browser

## Setup

```bash
# 1. Scaffold Vue project (if not already done)
npm create vite@latest . -- --template vue-ts
npm install vue-router

# 2. Generate content data from markdown
python build.py

# 3. Start dev server
npm run dev
```

Open http://localhost:5173 in your browser.

## Build for Production

```bash
# 1. Regenerate content data
python build.py

# 2. Build static site
npm run build
```

Output in `dist/` — ready to deploy to any static host.

## Deploy

The `dist/` directory is a self-contained static site:

- **GitHub Pages**: Push `dist/` contents to `gh-pages` branch
- **Vercel**: Connect repo, framework preset "Vite", output dir `dist`
- **Netlify**: Build command `npm run build`, publish directory `dist`

## Project Structure

```
src/
├── App.vue              # Root component (NavBar + router-view)
├── main.ts              # Entry point
├── router/index.ts      # Vue Router config
├── views/               # Page components (7 pages)
├── components/          # Reusable components
├── composables/         # useSearch, useProgress
├── data/                # Generated JSON (from build.py)
├── types/index.ts       # TypeScript interfaces
└── assets/style.css     # Global styles

public/
└── pdf/                 # Static PDF files

dist/                    # Vite build output
```
