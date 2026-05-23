# Research: AI Learning Hub Frontend

**Date**: 2026-05-21

## Decision 1: Frontend Framework

**Decision**: Vue 3 + Vite

**Rationale**: Vue 3 with Composition API is lightweight, has excellent developer experience, and Vite provides fast HMR for development. Vue Router for client-side navigation, single-file components (.vue) keep template/script/style co-located. Build output is static HTML/CSS/JS — no server runtime needed.

**Alternatives considered**:
- **Vanilla HTML/CSS/JS**: Too much boilerplate for routing, state management, and component reuse across 8+ pages.
- **React**: Heavier ecosystem, JSX syntax less suited for this content-heavy site.
- **11ty (Eleventy)**: Good SSG but adds a Node.js build step and separate templating language.
- **Hugo**: Fast but requires Go installation and Hugo templating knowledge.

## Decision 2: Markdown Rendering

**Decision**: Pre-process markdown to HTML at build time using a Python script (Python 3.11 already available)

**Rationale**: Client-side markdown rendering (e.g., marked.js) would mean shipping raw markdown to the browser and parsing on every page load. Pre-processing at build time means the browser receives ready-to-render HTML, which is faster and works without JS.

**Alternatives considered**:
- **marked.js (client-side)**: Adds ~40KB JS bundle, parsing on every load.
- **Remark (Node.js)**: Requires Node.js toolchain.
- **Python-Markdown**: Already have Python 3.11, zero additional dependencies.

## Decision 3: Search Implementation

**Decision**: Client-side full-text search using a pre-built JSON index

**Rationale**: Content volume is small (~50 items). A JSON index file generated at build time can be loaded once and searched instantly in the browser. No server needed.

**Alternatives considered**:
- **Algolia/MeiliSearch**: Requires external service — violates Principle II (Static-Site).
- **Lunr.js**: Good client-side search library but adds 8KB dependency. Can implement simpler approach.
- **Simple filter**: Just filter titles/tags — too limited for Chinese content search.

## Decision 4: CSS Approach

**Decision**: Vue scoped styles + CSS custom properties for theming, no UI framework

**Rationale**: Vue SFC `<style scoped>` provides component-level style isolation out of the box. CSS custom properties for global theming (colors, spacing). Mobile-first responsive design using CSS Grid and Flexbox.

**Alternatives considered**:
- **Tailwind CSS**: Adds build complexity and class-name noise in templates.
- **Bootstrap / Element Plus**: Heavy, not needed for this simple layout.
- **UnoCSS**: Fast but still adds tooling complexity.

## Decision 5: Data Structure

**Decision**: Content as JSON files imported by Vue components at build time

**Rationale**: A Python build script reads all markdown files, extracts metadata (title, year, category, arXiv ID), converts content to HTML, and outputs JSON files under `src/data/`. Vue components import these JSON files directly — Vite handles JSON imports natively. For paper detail pages, Vue Router loads content dynamically from the JSON data.

**Build pipeline**: `markdown files → Python build script → JSON files in src/data/ → Vite builds Vue app → dist/`
