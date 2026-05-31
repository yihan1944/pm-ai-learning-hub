<script setup lang="ts">
import { computed, ref, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { marked } from 'marked'
import papers from '../data/papers.json'

const route = useRoute()

function decodeHtml(html: string) {
  const txt = document.createElement('textarea')
  txt.innerHTML = html
  return txt.value
}

marked.setOptions({
  breaks: true,
  gfm: true,
})

const paper = computed(() => {
  const p = papers.find(p => p.id === route.params.id)
  if (!p) return null
  // Decode HTML entities then render markdown
  const decoded = decodeHtml(p.contentHtml)
  let html = marked.parse(decoded) as string
  // Add IDs to h2/h3 for TOC navigation
  let counter = 0
  html = html.replace(/<h([23])([^>]*)>(.*?)<\/h\1>/gi, (_, tag, attrs, text) => {
    const id = `section-${counter++}`
    return `<h${tag}${attrs} id="${id}">${text}</h${tag}>`
  })
  return { ...p, contentHtml: html }
})

const headings = computed(() => {
  if (!paper.value) return []
  const regex = /<h([23])[^>]*id="(section-\d+)"[^>]*>(.*?)<\/h\1>/gi
  const matches: { level: number; id: string; text: string }[] = []
  let m
  while ((m = regex.exec(paper.value.contentHtml)) !== null) {
    matches.push({ level: parseInt(m[1]), id: m[2], text: m[3] })
  }
  return matches
})

const activeId = ref('')

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          activeId.value = e.target.id
        }
      }
    },
    { rootMargin: '-80px 0px -60% 0px' }
  )
  setTimeout(() => {
    document.querySelectorAll('.prose h2[id], .prose h3[id]').forEach(el => {
      observer.observe(el)
    })
  }, 100)
  onUnmounted(() => observer.disconnect())
})

function scrollTo(id: string) {
  const el = document.getElementById(id)
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' })
}
</script>

<template>
  <div class="paper-detail" v-if="paper">
    <nav class="breadcrumb">
      <router-link to="/papers">论文笔记</router-link>
      <span class="sep">/</span>
      <span>{{ paper.categoryName }}</span>
    </nav>

    <div class="paper-layout">
      <aside class="paper-sidebar" v-if="headings.length > 0">
        <nav class="toc">
          <div class="toc-title">目录</div>
          <ul>
            <li
              v-for="h in headings"
              :key="h.id"
              :class="{ active: activeId === h.id, sub: h.level === 3 }"
            >
              <a @click.prevent="scrollTo(h.id)" href="#">{{ h.text }}</a>
            </li>
          </ul>
        </nav>
      </aside>

      <div class="paper-content">
        <header class="paper-header">
          <h1>{{ paper.title }}</h1>
          <div class="paper-meta">
            <span class="meta-badge year">{{ paper.year }}</span>
            <span class="meta-badge venue">{{ paper.categoryName }}</span>
            <a
              v-if="paper.arxivId"
              :href="`https://arxiv.org/abs/${paper.arxivId}`"
              target="_blank"
              rel="noopener"
              class="meta-badge link"
            >
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
              arXiv
            </a>
          </div>
        </header>

        <article class="prose" v-html="paper.contentHtml"></article>
      </div>
    </div>
  </div>

  <div v-else class="not-found">
    <h2>论文未找到</h2>
    <router-link to="/papers">返回论文列表</router-link>
  </div>
</template>

<style scoped>
.breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.88rem;
  color: var(--color-text-muted);
  margin-bottom: 1.5rem;
}

.breadcrumb a {
  color: var(--color-primary);
}

.sep {
  opacity: 0.4;
}

.paper-layout {
  display: flex;
  gap: 2.5rem;
  align-items: flex-start;
}

/* Sidebar TOC */
.paper-sidebar {
  position: sticky;
  top: calc(var(--nav-height) + 1.5rem);
  width: 200px;
  flex-shrink: 0;
}

.toc {
  font-size: 0.82rem;
}

.toc-title {
  font-weight: 600;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.75rem;
  font-size: 0.72rem;
}

.toc ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc li {
  margin-bottom: 0.3rem;
}

.toc li a {
  display: block;
  padding: 0.3em 0.6em;
  border-radius: 6px;
  color: var(--color-text-muted);
  text-decoration: none;
  transition: background 0.15s, color 0.15s;
  line-height: 1.4;
}

.toc li a:hover {
  background: rgba(255, 255, 255, 0.04);
  color: var(--color-text);
}

.toc li.active a {
  background: rgba(99, 102, 241, 0.1);
  color: var(--color-primary-hover);
}

.toc li.sub a {
  padding-left: 1.2em;
  font-size: 0.78rem;
}

/* Content */
.paper-content {
  flex: 1;
  min-width: 0;
  max-width: 800px;
}

.paper-header {
  margin-bottom: 2rem;
}

.paper-header h1 {
  font-size: 1.5rem;
  font-weight: 700;
  line-height: 1.4;
  margin-bottom: 0.75rem;
}

.paper-meta {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.meta-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.3em;
  padding: 0.25em 0.7em;
  border-radius: 99px;
  font-size: 0.8rem;
  font-weight: 500;
}

.meta-badge.year {
  background: rgba(99, 102, 241, 0.12);
  color: var(--color-primary-hover);
}

.meta-badge.venue {
  background: rgba(148, 163, 184, 0.1);
  color: var(--color-text-muted);
}

.meta-badge.link {
  background: rgba(255, 255, 255, 0.06);
  color: var(--color-text-muted);
  text-decoration: none;
  transition: background 0.15s, color 0.15s;
}

.meta-badge.link:hover {
  background: rgba(255, 255, 255, 0.1);
  color: var(--color-text);
}

.not-found {
  text-align: center;
  padding: 3rem 0;
}

.not-found h2 {
  margin-bottom: 1rem;
}

@media (max-width: 900px) {
  .paper-sidebar {
    display: none;
  }
}

/* Prose overrides for paper detail */
.paper-content :deep(.prose) {
  font-size: 0.95rem;
  line-height: 1.8;
}

.paper-content :deep(.prose h2) {
  font-size: 1.2rem;
  margin-top: 2.5em;
  padding-bottom: 0.4em;
  border-bottom: 1px solid var(--color-border);
  color: var(--color-text);
}

.paper-content :deep(.prose h3) {
  font-size: 1.05rem;
  margin-top: 1.8em;
}

.paper-content :deep(.prose blockquote) {
  background: rgba(99, 102, 241, 0.06);
  border-left: 3px solid var(--color-primary);
  padding: 0.8em 1em;
  border-radius: 0 8px 8px 0;
  margin: 1.2em 0;
  color: var(--color-text-muted);
  font-style: normal;
}

.paper-content :deep(.prose table) {
  font-size: 0.88rem;
}

.paper-content :deep(.prose th) {
  background: rgba(99, 102, 241, 0.08);
}

.paper-content :deep(.prose ul) {
  padding-left: 0;
  list-style: none;
}

.paper-content :deep(.prose ul li) {
  position: relative;
  padding-left: 1.2em;
}

.paper-content :deep(.prose ul li::before) {
  content: '';
  position: absolute;
  left: 0;
  top: 0.65em;
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: var(--color-primary);
  opacity: 0.5;
}

.paper-content :deep(.prose strong) {
  color: var(--color-text);
  font-weight: 600;
}

.paper-content :deep(.prose code) {
  background: rgba(99, 102, 241, 0.1);
  color: var(--color-primary-hover);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-size: 0.88em;
}
</style>
