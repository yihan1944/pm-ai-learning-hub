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

const typeColors: Record<string, string> = {
  paper: 'purple',
  knowledge: 'blue',
  agent: 'green',
  product: 'cyan',
  exam: 'rose',
}
</script>

<template>
  <div class="search-page">
    <div class="page-header">
      <h1>搜索</h1>
      <p class="subtitle">在所有内容中搜索</p>
    </div>

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
        <div class="result-header">
          <span class="result-type" :class="typeColors[item.type]">{{ typeLabels[item.type] || item.type }}</span>
          <span class="result-cat">{{ item.category }}</span>
        </div>
        <h3>{{ item.title }}</h3>
        <p>{{ item.text.slice(0, 120) }}...</p>
      </router-link>
    </div>
  </div>
</template>

<style scoped>
.page-header {
  margin-bottom: 2rem;
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

.search-box {
  position: relative;
  margin-bottom: 1.5rem;
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
  padding: 14px 16px 14px 44px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  color: var(--color-text);
  font-size: 1rem;
  outline: none;
  transition: all 0.25s;
}

.search-box input:focus {
  border-color: var(--color-primary);
  box-shadow: 0 0 0 3px rgba(201, 87, 62, 0.1);
}

.search-box input::placeholder {
  color: var(--color-text-muted);
}

.empty {
  text-align: center;
  padding: 3rem 0;
  color: var(--color-text-muted);
}

.results {
  margin-top: 1.5rem;
}

.results-count {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  margin-bottom: 12px;
}

.result-card {
  display: block;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 16px 20px;
  margin-bottom: 8px;
  transition: all 0.25s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  color: var(--color-text);
  text-decoration: none;
}

.result-card:hover {
  border-color: var(--color-border-hover);
  background: var(--color-surface-hover);
  transform: translateX(4px);
  color: var(--color-text);
}

.result-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 6px;
}

.result-type {
  font-size: 0.7rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}

.result-type.blue { background: rgba(0, 0, 0, 0.06); color: var(--color-text-secondary); }
.result-type.purple { background: rgba(0, 0, 0, 0.06); color: var(--color-text-secondary); }
.result-type.cyan { background: rgba(0, 0, 0, 0.06); color: var(--color-text-secondary); }
.result-type.green { background: rgba(0, 0, 0, 0.06); color: var(--color-text-secondary); }
.result-type.rose { background: rgba(0, 0, 0, 0.06); color: var(--color-text-secondary); }

.result-cat {
  font-size: 0.75rem;
  color: var(--color-text-muted);
}

.result-card h3 {
  font-size: 0.95rem;
  font-weight: 600;
  margin-bottom: 4px;
}

.result-card p {
  font-size: 0.85rem;
  color: var(--color-text-secondary);
  line-height: 1.5;
}
</style>
