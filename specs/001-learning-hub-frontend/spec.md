# Feature Specification: AI Learning Hub Frontend

**Feature Branch**: `001-learning-hub-frontend`

**Created**: 2026-05-21

**Status**: Draft

**Input**: User description: "给这个AI学习项目做一个前端页面"

## User Scenarios & Testing

### User Story 1 - Browse Learning Content (Priority: P1)

As an AI learner, I want to visit a homepage that shows all available learning categories (Papers, Knowledge, Agents, AI Products, Exam), so that I can quickly understand what content is available and navigate to what interests me.

**Why this priority**: The homepage is the entry point — without it, users cannot discover or access any content.

**Independent Test**: Open the site in a browser, verify all 5 categories are displayed with clear labels and descriptions, click each category to navigate to its section.

**Acceptance Scenarios**:

1. **Given** the user opens the site root URL, **When** the page loads, **Then** all 5 content categories are displayed with names, descriptions, and item counts.
2. **Given** the user clicks a category card, **When** the navigation completes, **Then** the user sees the list of items in that category.

---

### User Story 2 - Read Paper Notes (Priority: P1)

As an AI learner, I want to browse and read论文笔记 organized by category (基础架构、大语言模型、对齐与安全、多模态), so that I can study papers efficiently without opening raw markdown files.

**Why this priority**: Papers are the core learning asset — the primary value proposition of this project.

**Independent Test**: Navigate to Papers section, see papers grouped by category, click a paper to read its full notes with rendered markdown.

**Acceptance Scenarios**:

1. **Given** the user is on the Papers page, **When** the page loads, **Then** papers are grouped by category with title, year, and arXiv link displayed.
2. **Given** the user clicks a paper title, **When** the detail page loads, **Then** the full论文笔记 is rendered with proper markdown formatting (headings, tables, lists).
3. **Given** the user is reading a paper note, **When** they click the arXiv link, **Then** the original paper opens in a new tab.

---

### User Story 3 - Follow Learning Path (Priority: P2)

As an AI learner, I want to see the学习路线图 with checkboxes showing my progress, so that I can track what I've learned and what's next.

**Why this priority**: The learning path provides structured guidance — it turns a collection of resources into a curriculum.

**Independent Test**: Navigate to Knowledge section, see the 5-stage learning path with all items listed, check/uncheck items to track progress.

**Acceptance Scenarios**:

1. **Given** the user opens the Learning Path page, **When** the page loads, **Then** all 5 stages are displayed with their items and current completion status.
2. **Given** the user checks a learning item, **When** the checkbox is toggled, **Then** the progress is saved locally and persists on refresh.

---

### User Story 4 - Search Content (Priority: P2)

As an AI learner, I want to search across all content (papers, knowledge, agents, products, exam), so that I can quickly find specific topics without browsing through categories.

**Why this priority**: As content grows, search becomes essential for usability.

**Independent Test**: Type a keyword in the search bar, see matching results from all categories, click a result to navigate to the content.

**Acceptance Scenarios**:

1. **Given** the user types "Transformer" in the search bar, **When** results appear, **Then** matching papers, knowledge entries, and other content are displayed with category labels.
2. **Given** the user clicks a search result, **When** navigation completes, **Then** the user is taken to the specific content item.

---

### User Story 5 - Review Exam Questions (Priority: P3)

As an AI learner, I want to browse面试题 by category and reveal answers on demand, so that I can test my knowledge.

**Why this priority**: Exam content is supplementary — useful for interview prep but not core learning.

**Independent Test**: Navigate to Exam section, see question list, click to reveal answers.

**Acceptance Scenarios**:

1. **Given** the user opens the Exam page, **When** the page loads, **Then** questions are listed with answers hidden by default.
2. **Given** the user clicks a question, **When** the answer is toggled, **Then** the answer text is revealed inline.

---

### Edge Cases

- What happens when a markdown file has complex formatting (LaTeX, code blocks, images)? The renderer MUST handle common markdown extensions gracefully.
- What happens when content files are missing or malformed? The site MUST show a user-friendly error message rather than crashing.
- What happens on very large screens (>2560px)? Content MUST remain readable with appropriate max-width constraints.
- What happens when a user has JavaScript disabled? Core content SHOULD still be accessible (progressive enhancement).

## Requirements

### Functional Requirements

- **FR-001**: System MUST display all 5 content categories on the homepage with names, descriptions, and item counts.
- **FR-002**: System MUST render markdown content (论文笔记、术语表、面试题等) with proper formatting including headings, tables, lists, code blocks, and links.
- **FR-003**: System MUST organize papers by category (基础架构、大语言模型、对齐与安全、多模态) with year and arXiv metadata.
- **FR-004**: System MUST provide a learning path view with 5 stages and trackable checkbox progress stored in localStorage.
- **FR-005**: System MUST provide keyword search across all content categories.
- **FR-006**: System MUST be fully responsive from 320px mobile to 2560px+ desktop.
- **FR-007**: System MUST load the homepage in under 3 seconds on a standard broadband connection.
- **FR-008**: System MUST handle PDF files by providing download/view links (not inline rendering).
- **FR-009**: System MUST support deep linking — every content item MUST have a shareable URL.
- **FR-010**: System MUST display a navigation header persistent across all pages with links to each category.

### Key Entities

- **Paper**: 论文笔记 — title, year, arXiv ID, category, markdown content
- **LearningStage**: 学习阶段 — name, description, list of learning items with completion status
- **GlossaryTerm**: 术语 — term name, definition
- **ExamQuestion**: 面试题 — question text, answer text, category
- **AgentResource**: Agent 资源 — title, type (framework/pattern/project), description

## Success Criteria

### Measurable Outcomes

- **SC-001**: Users can navigate from homepage to any content item in 2 clicks or fewer.
- **SC-002**: All 10论文笔记 are accessible and readable through the frontend.
- **SC-003**: Learning path progress persists across browser sessions.
- **SC-004**: Search returns relevant results within 1 second for the current content volume.
- **SC-005**: Pages render correctly on Chrome, Firefox, Safari, and Edge (latest 2 versions).
- **SC-006**: Mobile users can read content comfortably without horizontal scrolling.

## Assumptions

- Content will be pre-processed at build time (markdown → HTML) rather than rendered client-side from raw files.
- The site will be a single-page application or static site — no backend server required.
- Learning path progress uses localStorage — no user accounts or cloud sync needed for v1.
- PDF files remain as static assets with download links — no embedded PDF viewer needed.
- All content is in Chinese — no i18n needed for v1.
- The current markdown content is authoritative — no content editing UI needed.
