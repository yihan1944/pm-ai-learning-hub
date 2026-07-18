#!/usr/bin/env python3
"""Build script: converts markdown content to JSON for Vue frontend."""

import json
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "src" / "data"
PDF_SRC = ROOT / "papers" / "pdf"
PDF_DST = ROOT / "public" / "pdf"

CATEGORY_MAP = {
    "foundation": "基础架构",
    "llm": "大语言模型",
    "alignment": "对齐与安全",
    "multimodal": "多模态",
}


def parse_paper(filepath: Path) -> dict:
    """Parse a paper markdown file."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.strip().split("\n")

    # Title: first # heading
    title = ""
    for line in lines:
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
            break

    # Extract year from table
    year = 0
    m = re.search(r"\|\s*年份\s*\|\s*(\d{4})\s*\|", text)
    if m:
        year = int(m.group(1))

    # Extract arXiv ID
    arxiv_id = ""
    m = re.search(r"arxiv\.org/abs/(\d+\.\d+)", text)
    if m:
        arxiv_id = m.group(1)

    # Determine category from filename prefix
    stem = filepath.stem
    category = "foundation"
    for prefix in CATEGORY_MAP:
        if stem.startswith(prefix):
            category = prefix
            break

    # Convert markdown to HTML (simple approach: use markdown content as-is)
    content_html = markdown_to_html(text)
    # Drop the leading <h1> (the detail page header already renders the title)
    content_html = re.sub(r"^\s*<h1>.*?</h1>\s*", "", content_html, flags=re.S)

    return {
        "id": stem,
        "title": title,
        "year": year,
        "arxivId": arxiv_id,
        "category": category,
        "categoryName": CATEGORY_MAP[category],
        "contentHtml": content_html,
        "filePath": str(filepath.relative_to(ROOT)),
    }


def markdown_to_html(text: str) -> str:
    """Convert markdown to HTML using Python-Markdown."""
    try:
        import markdown
        md = markdown.Markdown(extensions=["tables", "fenced_code"])
        return md.convert(text)
    except ImportError:
        # Fallback: return text with basic escaping
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def parse_learning_path(filepath: Path) -> list:
    """Parse learning-path.md into stages."""
    text = filepath.read_text(encoding="utf-8")
    stages = []
    current_stage = None
    item_id = 0

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("## ") and not line.startswith("## 横向") and not line.startswith("## 项目"):
            if current_stage:
                stages.append(current_stage)
            name = line.lstrip("# ").strip()
            order = len(stages) + 1
            current_stage = {
                "id": f"stage-{order}",
                "name": name,
                "order": order,
                "items": [],
            }
        elif line.startswith("## 横向") or line.startswith("## 项目"):
            if current_stage:
                stages.append(current_stage)
            name = line.lstrip("# ").strip()
            order = len(stages) + 1
            current_stage = {
                "id": f"horizontal-{order}",
                "name": name,
                "order": order,
                "items": [],
            }
        elif (line.startswith("- [ ] ") or line.startswith("* [ ] ")) and current_stage:
            item_id += 1
            text_content = line.lstrip("- * ").lstrip("[ ] ").strip()
            current_stage["items"].append({
                "id": f"item-{item_id}",
                "text": text_content,
                "completed": False,
            })

    if current_stage:
        stages.append(current_stage)

    return stages


def parse_glossary(filepath: Path) -> list:
    """Parse glossary.md table into terms."""
    text = filepath.read_text(encoding="utf-8")
    terms = []
    in_table = False

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("| 术语"):
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")]
            # parts: ['', term, english, definition, '']
            if len(parts) >= 4:
                term = parts[1]
                definition = parts[3]
                if term and definition:
                    terms.append({"term": term, "definition": definition})
        elif in_table and not line.startswith("|"):
            in_table = False

    return terms


def normalize_answer_md(text: str) -> str:
    """Insert blank lines so labels and list blocks parse as separate blocks.

    Collected answer lines contain no blank lines, which would make
    Python-Markdown glue the labels and the list into a single paragraph.
    Fenced code blocks are dedented to column 0 because the fenced_code
    extension only recognizes fences at line start.
    """
    lines = text.split("\n")
    out = []
    prev_list = False
    in_fence = False
    fence_indent = 0
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            if in_fence:
                in_fence = False
                prev_list = False
            else:
                in_fence = True
                fence_indent = len(line) - len(line.lstrip())
            out.append(line.lstrip())
            continue
        if in_fence:
            prefix = " " * fence_indent
            out.append(line[len(prefix):] if line.startswith(prefix) else line.lstrip())
            continue
        is_list = stripped.startswith("- ")
        if out and stripped and not (is_list and prev_list):
            out.append("")
        out.append(line)
        prev_list = is_list
    return "\n".join(out)


def render_answer(lines: list) -> str:
    """Render collected answer markdown lines to HTML."""
    return markdown_to_html(normalize_answer_md("\n".join(lines).strip()))


def parse_exam(filepath: Path) -> list:
    """Parse exam markdown into questions."""
    text = filepath.read_text(encoding="utf-8")
    questions = []
    current_q = None
    current_answer_lines = []
    q_id = 0
    in_fence = False

    # Determine category from filename
    stem = filepath.stem
    category = stem

    for line in text.split("\n"):
        stripped = line.strip()

        # Match ### N. question
        m = re.match(r"^###\s+\d+\.\s+(.+)", stripped)
        if m:
            # Save previous question
            if current_q:
                current_q["answer"] = render_answer(current_answer_lines)
                questions.append(current_q)

            q_id += 1
            current_q = {
                "id": f"q-{category}-{q_id}",
                "question": m.group(1).strip(),
                "answer": "",
                "category": category,
            }
            current_answer_lines = []
            in_fence = False
            continue

        # Collect answer lines (after **答题方向**: or **考察点**:)
        if current_q:
            if stripped.startswith("```"):
                in_fence = not in_fence
                if current_answer_lines:
                    current_answer_lines.append(line.rstrip())
            elif not in_fence and (
                stripped.startswith("**答题方向**") or stripped.startswith("**考察点**")
            ):
                current_answer_lines.append(stripped)
            elif current_answer_lines and (stripped or in_fence):
                # Skip section headers, horizontal rules, and blockquotes
                # that belong to the document structure, not the answer
                if (
                    stripped.startswith("## ")
                    or stripped.startswith("---")
                    or stripped.startswith("> ")
                ):
                    continue
                current_answer_lines.append(line.rstrip())

    # Save last question
    if current_q:
        current_q["answer"] = render_answer(current_answer_lines)
        questions.append(current_q)

    return questions


def build_search_index(papers, knowledge_data, exam_data):
    """Build search index from all content."""
    index = []

    for p in papers:
        # Extract plain text from HTML for search
        plain = re.sub(r"<[^>]+>", "", p["contentHtml"])[:300]
        index.append({
            "id": p["id"],
            "title": p["title"],
            "category": p["categoryName"],
            "type": "paper",
            "text": plain,
            "route": f"/papers/{p['id']}",
        })

    for stage in knowledge_data.get("stages", []):
        for item in stage["items"]:
            index.append({
                "id": item["id"],
                "title": item["text"],
                "category": "学习路线",
                "type": "knowledge",
                "text": item["text"],
                "route": "/knowledge",
            })

    for term in knowledge_data.get("glossary", []):
        index.append({
            "id": f"glossary-{term['term']}",
            "title": term["term"],
            "category": "术语表",
            "type": "knowledge",
            "text": f"{term['term']} - {term['definition']}",
            "route": "/knowledge",
        })

    for q in exam_data:
        index.append({
            "id": q["id"],
            "title": q["question"][:60],
            "category": "面试题",
            "type": "exam",
            "text": q["question"],
            "route": "/exam",
        })

    return index


def main():
    print("Building content data...")

    # Ensure output directory
    OUT.mkdir(parents=True, exist_ok=True)

    # 1. Parse papers
    papers_dir = ROOT / "papers"
    papers = []
    for f in sorted(papers_dir.glob("*.md")):
        if f.name.startswith("_") or f.name == "README.md":
            continue
        papers.append(parse_paper(f))
    (OUT / "papers.json").write_text(
        json.dumps(papers, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  Papers: {len(papers)}")

    # 2. Parse knowledge
    stages = parse_learning_path(ROOT / "knowledge" / "learning-path.md")
    glossary = parse_glossary(ROOT / "knowledge" / "glossary.md")
    knowledge = {"stages": stages, "glossary": glossary}
    (OUT / "knowledge.json").write_text(
        json.dumps(knowledge, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  Knowledge: {len(stages)} stages, {len(glossary)} terms")

    # 3. Parse exam
    exam = []
    exam_dir = ROOT / "exam"
    for f in sorted(exam_dir.glob("*.md")):
        exam.extend(parse_exam(f))
    (OUT / "exam.json").write_text(
        json.dumps(exam, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  Exam: {len(exam)} questions")

    # 4. Agents (placeholder - directory empty)
    agents = []
    (OUT / "agents.json").write_text(
        json.dumps(agents, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  Agents: {len(agents)} (empty)")

    # 5. Products
    products_file = ROOT / "products" / "products.json"
    if products_file.exists():
        products = json.loads(products_file.read_text(encoding="utf-8"))
    else:
        products = []
    (OUT / "products.json").write_text(
        json.dumps(products, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  Products: {len(products)}")

    # 6. Search index
    search_index = build_search_index(papers, knowledge, exam)
    (OUT / "search-index.json").write_text(
        json.dumps(search_index, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"  Search index: {len(search_index)} items")

    # 7. Copy PDFs
    if PDF_SRC.exists():
        PDF_DST.mkdir(parents=True, exist_ok=True)
        count = 0
        for pdf in PDF_SRC.glob("*.pdf"):
            shutil.copy2(pdf, PDF_DST / pdf.name)
            count += 1
        print(f"  PDFs: {count} copied")

    print("Done!")


if __name__ == "__main__":
    main()
