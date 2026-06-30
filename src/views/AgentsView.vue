<script setup lang="ts">
import agentsData from '../data/agents.json'
import type { AgentResource } from '../types'

const agents = agentsData as AgentResource[]
</script>

<template>
  <div class="agents">
    <div class="page-header">
      <h1>Agent 资源</h1>
      <p class="subtitle">Agent 框架、设计模式和项目实践</p>
    </div>

    <div v-if="agents.length === 0" class="empty">
      <p>暂无 Agent 资源，敬请期待。</p>
    </div>

    <div v-else class="agent-list">
      <div v-for="agent in agents" :key="agent.id" class="agent-card">
        <span class="agent-type">{{ agent.type }}</span>
        <h3>{{ agent.title }}</h3>
        <p>{{ agent.description }}</p>
      </div>
    </div>
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

.empty {
  text-align: center;
  padding: 3rem 0;
  color: var(--color-text-muted);
}

.agent-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
}

.agent-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 24px;
  transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  position: relative;
  overflow: hidden;
}

.agent-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--radius-lg);
  padding: 1px;
  background: linear-gradient(135deg, transparent, rgba(255, 255, 255, 0.05), transparent);
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.35s;
}

.agent-card:hover {
  background: var(--color-surface-hover);
  border-color: var(--color-border-hover);
  transform: translateY(-4px);
  box-shadow: var(--shadow-glow);
}

.agent-card:hover::before {
  opacity: 1;
}

.agent-type {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: #a78bfa;
  font-weight: 600;
  letter-spacing: 0.05em;
}

.agent-card h3 {
  font-size: 1.1rem;
  margin: 0.4em 0;
  font-weight: 600;
}

.agent-card p {
  font-size: 0.875rem;
  color: var(--color-text-secondary);
  line-height: 1.6;
}
</style>
