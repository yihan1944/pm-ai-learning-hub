<script setup lang="ts">
import agentsData from '../data/agents.json'
import type { AgentResource } from '../types'

const agents = agentsData as AgentResource[]
</script>

<template>
  <div class="agents">
    <h1>Agent 资源</h1>
    <p class="subtitle">Agent 框架、设计模式和项目实践</p>

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
.subtitle {
  color: var(--color-text-muted);
  margin-bottom: 2rem;
}

.empty {
  text-align: center;
  padding: 3rem 0;
  color: var(--color-text-muted);
}

.agent-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
}

.agent-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 1.25rem;
}

.agent-type {
  font-size: 0.75rem;
  text-transform: uppercase;
  color: var(--color-accent);
  font-weight: 600;
}

.agent-card h3 {
  font-size: 1.05rem;
  margin: 0.3em 0;
}

.agent-card p {
  font-size: 0.9rem;
  color: var(--color-text-muted);
}
</style>
