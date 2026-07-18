<script setup lang="ts">
import { computed, ref, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import papers from '../data/papers.json'

const route = useRoute()

// contentHtml 已是 build.py 预渲染的 HTML，直接注入标题 id 即可
const paper = computed(() => {
  const p = papers.find(p => p.id === route.params.id)
  if (!p) return null
  let counter = 0
  const html = p.contentHtml.replace(/<h([23])([^>]*)>(.*?)<\/h\1>/gi, (_, tag, attrs, text) => {
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
    matches.push({
      level: parseInt(m[1]),
      id: m[2],
      text: m[3].replace(/<[^>]+>/g, ''),
    })
  }
  return matches
})

const activeId = ref('')

let observer: IntersectionObserver | null = null

function observeHeadings() {
  observer?.disconnect()
  observer = new IntersectionObserver(
    (entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          activeId.value = e.target.id
        }
      }
    },
    { rootMargin: '-80px 0px -60% 0px' }
  )
  document.querySelectorAll('.prose h2[id], .prose h3[id]').forEach(el => observer!.observe(el))
}

onMounted(observeHeadings)

// 同组件切换论文时，等 DOM 更新后重新收集标题
watch(paper, async () => {
  activeId.value = ''
  await nextTick()
  if (paper.value) observeHeadings()
})

onUnmounted(() => observer?.disconnect())

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
            <span class="tag tag-primary">{{ paper.year }}</span>
            <span class="tag">{{ paper.categoryName }}</span>
            <a
              v-if="paper.arxivId"
              :href="`https://arxiv.org/abs/${paper.arxivId}`"
              target="_blank"
              rel="noopener"
              class="tag meta-link"
            >
              <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
              arXiv
            </a>
          </div>
        </header>

        <article class="prose" v-html="paper.contentHtml"></article>
      </div>
    </div>
  </div>

  <div v-else class="empty">
    <p class="empty-title">论文未找到</p>
    <router-link to="/papers">← 返回论文列表</router-link>
  </div>
</template>

<style scoped>
.breadcrumb {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-bottom: var(--space-5);
}

.sep {
  opacity: 0.5;
}

.paper-layout {
  display: flex;
  gap: var(--space-7);
  align-items: flex-start;
}

/* ── 侧边目录 ── */
.paper-sidebar {
  position: sticky;
  top: calc(var(--nav-height) + var(--space-5));
  width: 220px;
  flex-shrink: 0;
}

.toc {
  font-size: var(--text-sm);
}

.toc-title {
  font-weight: 600;
  color: var(--color-text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: var(--space-3);
  font-size: var(--text-xs);
}

.toc ul {
  list-style: none;
}

.toc li {
  margin-bottom: 2px;
}

.toc li a {
  display: block;
  padding: 5px 10px;
  border-radius: var(--radius-sm);
  color: var(--color-text-muted);
  text-decoration: none;
  transition: color var(--dur) var(--ease), background var(--dur) var(--ease);
  line-height: 1.5;
}

.toc li a:hover {
  background: var(--color-surface-sunken);
  color: var(--color-text);
}

.toc li.active a {
  background: var(--color-primary-subtle);
  color: var(--color-primary);
  box-shadow: inset 2px 0 0 var(--color-primary);
}

.toc li.sub a {
  padding-left: 1.75em;
  font-size: var(--text-xs);
}

/* ── 正文 ── */
.paper-content {
  flex: 1;
  min-width: 0;
  max-width: var(--prose-width);
}

.paper-header {
  margin-bottom: var(--space-6);
}

.paper-header h1 {
  font-size: var(--text-2xl);
  font-weight: 700;
  line-height: 1.4;
  margin-bottom: var(--space-3);
  letter-spacing: -0.02em;
}

.paper-meta {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.meta-link {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  text-decoration: none;
  transition: color var(--dur) var(--ease), background var(--dur) var(--ease);
}

.meta-link:hover {
  color: var(--color-primary);
  background: var(--color-primary-subtle);
}

.empty-title {
  font-size: var(--text-lg);
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: var(--space-3);
}

@media (max-width: 900px) {
  .paper-sidebar {
    display: none;
  }
}
</style>
