<script setup lang="ts">
import knowledge from '../data/knowledge.json'
import LearningStage from '../components/LearningStage.vue'
</script>

<template>
  <div class="knowledge">
    <div class="page-header">
      <h1>学习路线</h1>
      <p class="subtitle">从 AI 认知到产品落地的 {{ knowledge.stages.length }} 阶段学习路径</p>
    </div>

    <section class="stages">
      <LearningStage
        v-for="stage in knowledge.stages"
        :key="stage.id"
        :stage="stage"
      />
    </section>

    <section class="glossary">
      <div class="section-header">
        <h2>术语表</h2>
        <div class="line"></div>
      </div>
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

.stages {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 3rem;
}

.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.section-header h2 {
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  white-space: nowrap;
}

.section-header .line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.08), transparent);
}

.term-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 10px;
}

.term-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  padding: 14px 18px;
  transition: all 0.25s;
}

.term-card:hover {
  border-color: var(--color-border-hover);
  background: var(--color-surface-hover);
}

.term-card dt {
  font-weight: 600;
  font-size: 0.95rem;
  margin-bottom: 0.3em;
  color: #818cf8;
}

.term-card dd {
  font-size: 0.88rem;
  color: var(--color-text-secondary);
  line-height: 1.5;
}
</style>
