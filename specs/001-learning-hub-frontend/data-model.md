# Data Model: AI Learning Hub Frontend

**Date**: 2026-05-21

## Entities

### Paper
Represents a论文笔记 from the papers/ directory.

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier (e.g., "foundation_01") |
| title | string | Paper title (e.g., "Attention Is All You Need") |
| titleCn | string | Chinese title if available |
| year | number | Publication year |
| arxivId | string | arXiv ID (e.g., "1706.03762") |
| category | enum | "foundation" \| "llm" \| "alignment" \| "multimodal" |
| categoryName | string | Display name (e.g., "基础架构") |
| contentHtml | string | Pre-rendered HTML content |
| filePath | string | Source markdown file path |

### LearningStage
Represents a stage in the学习路线图.

| Field | Type | Description |
|-------|------|-------------|
| id | string | Stage identifier (e.g., "stage-1") |
| name | string | Stage name (e.g., "第一阶段：基础认知") |
| order | number | Display order (1-5) |
| items | LearningItem[] | List of learning items |

### LearningItem
Represents a single learning task within a stage.

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier |
| text | string | Item description |
| completed | boolean | Completion status (persisted in localStorage) |

### GlossaryTerm
Represents a术语表 entry.

| Field | Type | Description |
|-------|------|-------------|
| term | string | Term name |
| definition | string | Term definition |

### ExamQuestion
Represents a面试题.

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier |
| question | string | Question text |
| answer | string | Answer text |
| category | string | Question category |

### AgentResource
Represents an agent framework/pattern/project resource.

| Field | Type | Description |
|-------|------|-------------|
| id | string | Unique identifier |
| title | string | Resource title |
| type | enum | "framework" \| "pattern" \| "project" |
| description | string | Brief description |

## Relationships

```
Paper *--1 category (foundation | llm | alignment | multimodal)
LearningStage 1--* LearningItem
ExamQuestion *--1 category
AgentResource *--1 type
```

## Storage

- **Static data**: JSON file (`site-data.json`) generated at build time, loaded by frontend
- **User progress**: localStorage key `learning-progress` storing `{ completedItems: string[] }`
- **No database**: All content is file-based per Constitution Principle I
