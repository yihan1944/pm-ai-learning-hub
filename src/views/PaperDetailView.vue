<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import papers from '../data/papers.json'

const route = useRoute()

const paper = computed(() =>
  papers.find(p => p.id === route.params.id)
)
</script>

<template>
  <div class="paper-detail" v-if="paper">
    <nav class="breadcrumb">
      <router-link to="/papers">论文笔记</router-link>
      <span>/</span>
      <span>{{ paper.categoryName }}</span>
    </nav>

    <header class="paper-header">
      <h1>{{ paper.title }}</h1>
      <div class="paper-meta">
        <span class="paper-year">{{ paper.year }}</span>
        <a
          v-if="paper.arxivId"
          :href="`https://arxiv.org/abs/${paper.arxivId}`"
          target="_blank"
          rel="noopener"
          class="btn"
        >arXiv: {{ paper.arxivId }}</a>
      </div>
    </header>

    <article class="prose" v-html="paper.contentHtml"></article>
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
  font-size: 0.9rem;
  color: var(--color-text-muted);
  margin-bottom: 1.5rem;
}

.breadcrumb a {
  color: var(--color-primary);
}

.paper-header {
  margin-bottom: 2rem;
}

.paper-header h1 {
  font-size: 1.6rem;
  margin-bottom: 0.75rem;
}

.paper-meta {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.paper-year {
  background: var(--color-surface);
  padding: 0.2em 0.6em;
  border-radius: 4px;
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.not-found {
  text-align: center;
  padding: 3rem 0;
}

.not-found h2 {
  margin-bottom: 1rem;
}
</style>
