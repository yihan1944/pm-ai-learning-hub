<script setup lang="ts">
import papers from '../data/papers.json'
import { computed } from 'vue'

const grouped = computed(() => {
  const map: Record<string, typeof papers> = {}
  for (const p of papers) {
    if (!map[p.categoryName]) map[p.categoryName] = []
    map[p.categoryName].push(p)
  }
  return map
})
</script>

<template>
  <div class="papers">
    <div class="page-header">
      <h1>论文笔记</h1>
      <p class="subtitle">经典 AI 论文阅读笔记</p>
    </div>

    <section v-for="(items, cat) in grouped" :key="cat" class="category-section">
      <div class="section-header">
        <h2>{{ cat }}</h2>
        <div class="line"></div>
      </div>
      <div class="paper-list">
        <router-link
          v-for="paper in items"
          :key="paper.id"
          :to="`/papers/${paper.id}`"
          class="paper-card"
        >
          <div class="paper-info">
            <span class="paper-year">{{ paper.year }}</span>
            <h3>{{ paper.title }}</h3>
          </div>
          <a
            v-if="paper.arxivId"
            :href="`https://arxiv.org/abs/${paper.arxivId}`"
            target="_blank"
            rel="noopener"
            class="arxiv-link"
            @click.stop
          >arXiv</a>
        </router-link>
      </div>
    </section>
  </div>
</template>

<style scoped>
.page-header {
  margin-bottom: 2.5rem;
}

.page-header h1 {
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 0.4rem;
}

.subtitle {
  color: var(--color-text-secondary);
  font-size: 0.95rem;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.section-header h2 {
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  white-space: nowrap;
}

.section-header .line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.08), transparent);
}

.category-section {
  margin-bottom: 2.5rem;
}

.paper-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.paper-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 14px 18px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  transition: all 0.25s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  color: var(--color-text);
}

.paper-card:hover {
  border-color: var(--color-border-hover);
  background: var(--color-surface-hover);
  transform: translateX(4px);
  color: var(--color-text);
}

.paper-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.paper-year {
  background: rgba(99, 102, 241, 0.1);
  color: #818cf8;
  padding: 0.15em 0.6em;
  border-radius: 6px;
  font-size: 0.78rem;
  font-weight: 500;
  flex-shrink: 0;
}

.paper-card h3 {
  font-size: 0.95rem;
  font-weight: 500;
}

.arxiv-link {
  font-size: 0.78rem;
  padding: 0.2em 0.7em;
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 6px;
  color: var(--color-text-muted);
  flex-shrink: 0;
  transition: all 0.2s;
}

.arxiv-link:hover {
  background: rgba(255, 255, 255, 0.06);
  color: var(--color-text);
}
</style>
