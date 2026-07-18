<script setup lang="ts">
import { ref, watch } from 'vue'
import PageHeader from '../components/PageHeader.vue'
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
    <PageHeader title="搜索" subtitle="在所有内容中搜索" />

    <div class="search-box">
      <svg class="search-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
      </svg>
      <input
        v-model="query"
        type="text"
        placeholder="输入关键词..."
        autofocus
      />
    </div>

    <div v-if="query && results.length === 0" class="empty">
      没有找到匹配「{{ query }}」的结果
    </div>

    <div v-if="results.length > 0" class="results">
      <p class="results-count">找到 {{ results.length }} 条结果</p>
      <router-link
        v-for="item in results"
        :key="item.id"
        :to="item.route"
        class="card card-link result-card"
      >
        <div class="result-header">
          <span class="tag">{{ typeLabels[item.type] || item.type }}</span>
          <span class="result-cat">{{ item.category }}</span>
        </div>
        <h3>{{ item.title }}</h3>
        <p>{{ item.text.slice(0, 120) }}...</p>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.search-box {
  position: relative;
  margin-bottom: var(--space-5);
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--color-text-muted);
  pointer-events: none;
}

.search-box input {
  width: 100%;
  padding: 12px 16px 12px 44px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  color: var(--color-text);
  font-size: var(--text-base);
  outline: none;
  transition: border-color var(--dur) var(--ease), box-shadow var(--dur) var(--ease);
}

.search-box input:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px var(--color-primary-subtle);
}

.search-box input::placeholder {
  color: var(--color-text-muted);
}

.results-count {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-bottom: var(--space-3);
}

.result-card {
  padding: var(--space-4);
  margin-bottom: var(--space-2);
}

.result-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-bottom: var(--space-2);
}

.result-cat {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}

.result-card h3 {
  font-size: var(--text-md);
  font-weight: 600;
  margin-bottom: var(--space-1);
}

.result-card p {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  line-height: 1.6;
}
</style>
