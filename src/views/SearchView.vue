<script setup lang="ts">
import { ref, watch } from 'vue'
import { useSearch } from '../composables/useSearch'

const query = ref('')
const { results, search } = useSearch()

watch(query, (val) => search(val))

const typeLabels: Record<string, string> = {
  paper: '论文',
  knowledge: '知识',
  agent: 'Agent',
  product: '产品',
  exam: '面试题',
}
</script>

<template>
  <div class="search-page">
    <h1>搜索</h1>
    <p class="subtitle">在所有内容中搜索</p>

    <div class="search-box">
      <input
        v-model="query"
        type="text"
        placeholder="输入关键词..."
        autofocus
      />
    </div>

    <div v-if="query && results.length === 0" class="empty">
      没有找到匹配 "{{ query }}" 的结果
    </div>

    <div v-if="results.length > 0" class="results">
      <p class="results-count">找到 {{ results.length }} 条结果</p>
      <router-link
        v-for="item in results"
        :key="item.id"
        :to="item.route"
        class="result-card"
      >
        <span class="result-type">{{ typeLabels[item.type] || item.type }}</span>
        <span class="result-cat">{{ item.category }}</span>
        <h3>{{ item.title }}</h3>
        <p>{{ item.text.slice(0, 120) }}...</p>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.subtitle {
  color: var(--color-text-muted);
  margin-bottom: 1.5rem;
}

.search-box input {
  width: 100%;
  padding: 0.75rem 1rem;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  color: var(--color-text);
  font-size: 1rem;
  outline: none;
  transition: border-color 0.2s;
}

.search-box input:focus {
  border-color: var(--color-primary);
}

.search-box input::placeholder {
  color: var(--color-text-muted);
}

.empty {
  text-align: center;
  padding: 2rem 0;
  color: var(--color-text-muted);
}

.results {
  margin-top: 1.5rem;
}

.results-count {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  margin-bottom: 1rem;
}

.result-card {
  display: block;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 1rem;
  margin-bottom: 0.5rem;
  transition: border-color 0.2s;
  color: var(--color-text);
}

.result-card:hover {
  border-color: var(--color-primary);
  color: var(--color-text);
}

.result-type {
  font-size: 0.75rem;
  background: var(--color-primary);
  color: #fff;
  padding: 0.1em 0.5em;
  border-radius: 4px;
  margin-right: 0.5rem;
}

.result-cat {
  font-size: 0.75rem;
  color: var(--color-text-muted);
}

.result-card h3 {
  font-size: 0.95rem;
  margin: 0.4em 0 0.2em;
}

.result-card p {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  line-height: 1.4;
}
</style>
