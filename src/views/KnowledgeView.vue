<script setup lang="ts">
import knowledge from '../data/knowledge.json'
import LearningStage from '../components/LearningStage.vue'
</script>

<template>
  <div class="knowledge">
    <h1>学习路线</h1>
    <p class="subtitle">从 AI 认知到产品落地的 {{ knowledge.stages.length }} 阶段学习路径</p>

    <section class="stages">
      <LearningStage
        v-for="stage in knowledge.stages"
        :key="stage.id"
        :stage="stage"
      />
    </section>

    <section class="glossary">
      <h2>术语表</h2>
      <div class="term-list">
        <div v-for="term in knowledge.glossary" :key="term.term" class="term-card">
          <dt>{{ term.term }}</dt>
          <dd>{{ term.definition }}</dd>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.subtitle {
  color: var(--color-text-muted);
  margin-bottom: 2rem;
}

.stages {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  margin-bottom: 3rem;
}

.glossary h2 {
  font-size: 1.25rem;
  margin-bottom: 1rem;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--color-border);
}

.term-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 0.75rem;
}

.term-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 0.75rem 1rem;
}

.term-card dt {
  font-weight: 600;
  font-size: 0.95rem;
  margin-bottom: 0.3em;
  color: var(--color-primary);
}

.term-card dd {
  font-size: 0.88rem;
  color: var(--color-text-muted);
}
</style>
