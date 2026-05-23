# Tasks: AI Learning Hub Frontend (Vue 3)

**Input**: Design documents from `specs/001-learning-hub-frontend/`

**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅

**Organization**: Tasks grouped by user story for independent implementation and testing.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US5)

---

## Phase 1: Setup

**Purpose**: Vue project scaffolding + build script

- [ ] T001 Run `npm create vite@latest pm-ai-system -- --template vue-ts` to scaffold Vue 3 + TypeScript project, install dependencies (`vue`, `vue-router`)
- [ ] T002 Create `build.py` — Python build script that reads markdown from `papers/`, `knowledge/`, `agents/`, `ai-products/`, `exam/` and outputs JSON to `src/data/`
- [ ] T003 Create `src/types/index.ts` — TypeScript interfaces: `Paper`, `LearningStage`, `LearningItem`, `GlossaryTerm`, `ExamQuestion`, `AgentResource`
- [ ] T004 Create `src/assets/style.css` — global styles with CSS custom properties (colors, spacing, typography), mobile-first reset
- [ ] T005 [P] Create `src/router/index.ts` — Vue Router config with routes for all 7 pages (/, /papers, /papers/:id, /knowledge, /agents, /products, /exam, /search)
- [ ] T006 Add `src/data/` and `dist/` to `.gitignore`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build pipeline + shared components that ALL pages depend on

**⚠️ No user story work can begin until this phase is complete**

- [ ] T007 Implement markdown parser in `build.py` — extract metadata (title, year, arXiv ID, category) from markdown headers/tables, convert body to HTML using Python-Markdown
- [ ] T008 Implement JSON generators in `build.py` — output `src/data/papers.json`, `knowledge.json`, `agents.json`, `products.json`, `exam.json`, `search-index.json`
- [ ] T009 Create `src/App.vue` — root component with `<NavBar>` + `<router-view>` + `<footer>`
- [ ] T010 Create `src/components/NavBar.vue` — navigation links (Home, Papers, Knowledge, Agents, Products, Exam), mobile hamburger menu, search icon link
- [ ] T011 Implement PDF copy in `build.py` — copy `papers/pdf/` to `public/pdf/` so Vite serves them as static assets
- [ ] T012 Run `python build.py` to generate all JSON data files, verify they exist in `src/data/`

**Checkpoint**: `npm run dev` shows app shell with navigation, JSON data files generated

---

## Phase 3: User Story 1 — Browse Learning Content (Priority: P1) 🎯 MVP

**Goal**: Homepage shows all 5 categories with names, descriptions, item counts

**Independent Test**: Open localhost, see 5 category cards, click each to navigate

### Implementation

- [ ] T013 [P] [US1] Create `src/components/CategoryCard.vue` — props: title, description, count, icon, route; card with hover effect
- [ ] T014 [US1] Create `src/views/HomeView.vue` — hero section + 5 `<CategoryCard>` items, import counts from JSON data files
- [ ] T015 [US1] Style category cards in `src/assets/style.css` — responsive grid (1-col mobile, 2-col tablet, 3-col desktop), hover animations

**Checkpoint**: Homepage displays 5 category cards with real item counts, clicking navigates to category pages

---

## Phase 4: User Story 2 — Read Paper Notes (Priority: P1)

**Goal**: Papers grouped by category, click to read full rendered notes

**Independent Test**: Navigate to /papers, see papers by category, click a paper to read full content

### Implementation

- [ ] T016 [P] [US2] Create `src/components/PaperCard.vue` — props: title, year, arxivId, category; displays paper info with link to detail
- [ ] T017 [US2] Create `src/views/PapersView.vue` — import `papers.json`, group by category (基础架构、大语言模型、对齐与安全、多模态), render `<PaperCard>` list per group
- [ ] T018 [US2] Create `src/views/PaperDetailView.vue` — route param `:id`, load paper from `papers.json`, render HTML content with `v-html`, show breadcrumb + arXiv link
- [ ] T019 [US2] Style paper pages in scoped CSS — category section headers, paper card list, detail page typography (tables, code blocks, headings)

**Checkpoint**: All 10论文笔记 accessible and readable with proper formatting

---

## Phase 5: User Story 3 — Follow Learning Path (Priority: P2)

**Goal**: Learning path with 5 stages, trackable checkboxes persisted in localStorage

**Independent Test**: Open /knowledge, see 5 stages, check/uncheck items, refresh to verify persistence

### Implementation

- [ ] T020 [P] [US3] Create `src/composables/useProgress.ts` — composable for loading/saving learning progress to localStorage, reactive `completedItems` set
- [ ] T021 [P] [US3] Create `src/components/LearningStage.vue` — props: stage data; collapsible section with checkboxes, uses `useProgress` for state
- [ ] T022 [US3] Create `src/views/KnowledgeView.vue` — import `knowledge.json`, render 5 `<LearningStage>` components + glossary section below
- [ ] T023 [US3] Style knowledge page in scoped CSS — stage cards, checkbox styling, progress bar per stage, glossary definition list

**Checkpoint**: Learning path works with persistent progress, glossary is browsable

---

## Phase 6: User Story 4 — Search Content (Priority: P2)

**Goal**: Keyword search across all content categories

**Independent Test**: Type "Transformer" in search bar, see matching results from papers + knowledge

### Implementation

- [ ] T024 [P] [US4] Create `src/composables/useSearch.ts` — composable that loads `search-index.json`, provides `search(query)` function returning filtered results with category labels
- [ ] T025 [US4] Create `src/components/SearchBar.vue` — input field with debounced search, emits results or navigates to /search
- [ ] T026 [US4] Create `src/views/SearchView.vue` — displays search results as cards with category badges, empty state, link to detail pages
- [ ] T027 [US4] Integrate `<SearchBar>` into `NavBar.vue` — compact on desktop, expandable overlay on mobile

**Checkpoint**: Search returns relevant results from all categories within 1 second

---

## Phase 7: User Story 5 — Review Exam Questions (Priority: P3)

**Goal**: Exam questions with reveal-on-click answers

**Independent Test**: Open /exam, see questions, click to reveal answers

### Implementation

- [ ] T028 [P] [US5] Create `src/components/ExamQuestion.vue` — props: question, answer; click to toggle answer visibility with transition
- [ ] T029 [US5] Create `src/views/ExamView.vue` — import `exam.json`, group by source file, render `<ExamQuestion>` list
- [ ] T030 [US5] Style exam page in scoped CSS — question cards, answer reveal animation, category grouping

**Checkpoint**: Both面试题 files browsable with reveal-on-click answers

---

## Phase 8: Polish & Cross-Cutting

**Purpose**: Final refinements across all pages

- [ ] T031 [P] Add `<title>` and meta description to each view via Vue Router `meta` + `useHead` or document.title
- [ ] T032 [P] Add "Back to top" button on long pages (PaperDetail, Knowledge)
- [ ] T033 Test on Chrome, Firefox, Safari, Edge — verify layout and interactions
- [ ] T034 Test on mobile (320px, 375px, 768px) — verify responsive behavior
- [ ] T035 Run quickstart.md validation — `python build.py && npm run build` produces working dist/
- [ ] T036 [P] Add loading states and error handling for missing/malformed JSON data

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — BLOCKS all user stories
- **US1 + US2 (P1)**: Both depend on Phase 2. Can run in parallel.
- **US3 + US4 (P2)**: Both depend on Phase 2. Can run in parallel.
- **US5 (P3)**: Depends on Phase 2 only.
- **Polish (Phase 8)**: Depends on all user stories complete.

### Parallel Opportunities

```
Phase 1: T001 → T002, T003, T004, T005, T006 (parallel after T001)
Phase 2: T007 → T008 (sequential), T009, T010, T011, T012 (parallel)
Phase 3+4: T013-T015 (US1) ∥ T016-T019 (US2) — PARALLEL
Phase 5+6: T020-T023 (US3) ∥ T024-T027 (US4) — PARALLEL
Phase 7: T028-T030 (US5)
Phase 8: T031, T032, T036 (parallel), T033-T035 (sequential)
```

---

## Implementation Strategy

### MVP First (US1 + US2)

1. Complete Phase 1: Setup (Vite scaffold + build.py)
2. Complete Phase 2: Foundational (JSON pipeline + App shell)
3. Complete Phase 3: Homepage (US1)
4. Complete Phase 4: Paper Notes (US2)
5. **STOP and VALIDATE**: Homepage + paper reading works end-to-end
6. Deploy MVP — the core value (reading论文笔记) is delivered

### Incremental Delivery

1. Setup + Foundational → Build pipeline works
2. US1 + US2 → Homepage + Papers (MVP!)
3. US3 → Learning path with progress tracking
4. US4 → Search across all content
5. US5 → Exam questions
6. Polish → Production ready
