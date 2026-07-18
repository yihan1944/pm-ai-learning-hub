<script setup lang="ts">
import PageHeader from '../components/PageHeader.vue'
import agentsData from '../data/agents.json'
import type { AgentResource } from '../types'

const agents = agentsData as AgentResource[]
</script>

<template>
  <div class="agents">
    <PageHeader title="Agent 资源" subtitle="Agent 框架、设计模式和项目实践" />

    <div v-if="agents.length === 0" class="empty">
      <p>暂无 Agent 资源，敬请期待。</p>
    </div>

    <div v-else class="agent-list">
      <div v-for="agent in agents" :key="agent.id" class="card agent-card">
        <span class="tag">{{ agent.type }}</span>
        <h3>{{ agent.title }}</h3>
        <p>{{ agent.description }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.agent-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--space-4);
}

.agent-card h3 {
  font-size: var(--text-lg);
  font-weight: 600;
  letter-spacing: -0.01em;
  margin: var(--space-2) 0;
}

.agent-card p {
  font-size: var(--text-md);
  color: var(--color-text-secondary);
  line-height: 1.6;
}
</style>
