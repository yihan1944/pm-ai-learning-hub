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
    <h1>论文笔记</h1>
    <p class="subtitle">经典 AI 论文阅读笔记</p>

    <section v-for="(items, cat) in grouped" :key="cat" class="category-section">
      <h2>{{ cat }}</h2>
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
.subtitle {
  color: var(--color-text-muted);
  margin-bottom: 2rem;
}

.category-section {
  margin-bottom: 2.5rem;
}

.category-section h2 {
  font-size: 1.25rem;
  margin-bottom: 0.75rem;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--color-border);
}

.paper-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.paper-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.75rem 1rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  transition: border-color 0.2s;
  color: var(--color-text);
}

.paper-card:hover {
  border-color: var(--color-primary);
  color: var(--color-text);
}

.paper-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.paper-year {
  background: var(--color-surface-hover);
  padding: 0.15em 0.5em;
  border-radius: 4px;
  font-size: 0.8rem;
  color: var(--color-text-muted);
  flex-shrink: 0;
}

.paper-card h3 {
  font-size: 0.95rem;
  font-weight: 500;
}

.arxiv-link {
  font-size: 0.8rem;
  padding: 0.2em 0.6em;
  border: 1px solid var(--color-border);
  border-radius: 4px;
  color: var(--color-text-muted);
  flex-shrink: 0;
}

.arxiv-link:hover {
  background: var(--color-surface-hover);
  color: var(--color-text);
}
</style>
