<script setup lang="ts">
import { computed } from 'vue'
import PageHeader from '../components/PageHeader.vue'
import SectionHeader from '../components/SectionHeader.vue'
import papers from '../data/papers.json'

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
    <PageHeader title="论文笔记" subtitle="经典 AI 论文阅读笔记" />

    <section v-for="(items, cat) in grouped" :key="cat" class="category-section">
      <SectionHeader :title="cat" />
      <div class="paper-list">
        <router-link
          v-for="paper in items"
          :key="paper.id"
          :to="`/papers/${paper.id}`"
          class="card paper-row"
        >
          <div class="paper-info">
            <span class="tag">{{ paper.year }}</span>
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
.category-section {
  margin-bottom: var(--space-6);
}

.paper-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.paper-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius);
  color: inherit;
  transition:
    border-color var(--dur) var(--ease),
    transform var(--dur) var(--ease),
    background var(--dur) var(--ease);
}

.paper-row:hover {
  color: inherit;
  border-color: var(--color-border-strong);
  transform: translateX(2px);
}

.paper-info {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  min-width: 0;
}

.paper-row h3 {
  font-size: var(--text-md);
  font-weight: 500;
}

.arxiv-link {
  font-size: var(--text-xs);
  padding: 2px 10px;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  color: var(--color-text-muted);
  flex-shrink: 0;
  transition: color var(--dur) var(--ease), border-color var(--dur) var(--ease);
}

.arxiv-link:hover {
  color: var(--color-primary);
  border-color: var(--color-primary);
}
</style>
