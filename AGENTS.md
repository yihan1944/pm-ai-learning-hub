# Repository Guidelines

## Project Structure & Module Organization

A **Vue 3 + TypeScript + Vite** SPA for an AI Product Manager learning hub.

- `src/views/` — Page-level Vue components (routed views)
- `src/components/` — Reusable UI components
- `src/composables/` — Vue composables (`useProgress`, `useSearch`)
- `src/data/` — Generated JSON data files (built by `build.py`; gitignored)
- `src/router/` — Vue Router configuration
- `src/types/` — TypeScript type definitions
- `papers/`, `knowledge/`, `exam/`, `products/`, `agents/` — Markdown content sources
- `build.py` — Converts Markdown content into `src/data/*.json`
- `.github/workflows/deploy.yml` — CI/CD for GitHub Pages deployment

## Build, Test, and Development Commands

```bash
npm install          # Install Node.js dependencies
pip install markdown # Install Python dependency for build.py
python build.py      # Generate JSON data from Markdown content
npm run dev          # Start Vite dev server
npm run build        # Type-check (vue-tsc) then produce production build
npm run preview      # Preview the production build locally
```

Run `python build.py` after editing any Markdown file in the content directories.

## Coding Style & Naming Conventions

- **Language**: Vue 3 Composition API with `<script setup lang="ts">`.
- **Indentation**: 2 spaces for Vue, TypeScript, CSS, and JSON.
- **Components**: PascalCase filenames (e.g., `NavBar.vue`, `PaperDetailView.vue`).
- **Composables**: camelCase with `use` prefix (e.g., `useProgress.ts`).
- **CSS**: CSS custom properties for theming; styles in `src/assets/style.css` or scoped.
- No explicit formatter configured; match existing style.

## Testing Guidelines

No automated test suite exists. Validate changes manually:

1. Run `python build.py` to regenerate data.
2. Run `npm run dev` and verify affected pages render correctly.
3. Run `npm run build` to confirm no type or build errors.

## Commit & Pull Request Guidelines

Follow **Conventional Commits** as seen in git history:

```
feat: add dream-cli product
fix: remove wide card variant
style: redesign to Anthropic-inspired warm theme
docs: add README.md
security: add CSP meta tag
```

- Use a prefix (`feat:`, `fix:`, `style:`, `docs:`, `security:`) + concise description.
- PRs should include a brief summary and reference related issues.
- The `master` branch auto-deploys via GitHub Actions on push.

## Content Workflow

1. Edit or add Markdown in the relevant directory (`papers/`, `knowledge/`, `exam/`, `products/`, `agents/`).
2. Run `python build.py` to regenerate JSON data.
3. Commit both the Markdown source and generated data changes.
4. Push to `master`; GitHub Actions handles deployment.
