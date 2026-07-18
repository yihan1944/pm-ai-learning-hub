<script setup lang="ts">
import PageHeader from '../components/PageHeader.vue'
import SectionHeader from '../components/SectionHeader.vue'
import LearningStage from '../components/LearningStage.vue'
import knowledge from '../data/knowledge.json'
</script>

<template>
  <div class="knowledge">
    <PageHeader
      title="学习路线"
      :subtitle="`从 AI 认知到产品落地的 ${knowledge.stages.length} 阶段学习路径`"
    />

    <section class="stages">
      <LearningStage
        v-for="stage in knowledge.stages"
        :key="stage.id"
        :stage="stage"
      />
    </section>

    <section class="glossary">
      <SectionHeader title="术语表" />
      <div class="term-list">
        <div v-for="term in knowledge.glossary" :key="term.term" class="card term-card">
          <dt>{{ term.term }}</dt>
          <dd>{{ term.definition }}</dd>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.stages {
  display: flex;
  flex-direction: column;
  gap: var(--space-3);
  margin-bottom: var(--space-7);
}

.term-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: var(--space-3);
}

.term-card {
  padding: var(--space-4) var(--space-5);
}

.term-card dt {
  font-weight: 600;
  font-size: var(--text-md);
  margin-bottom: var(--space-1);
  color: var(--color-primary);
}

.term-card dd {
  font-size: var(--text-sm);
  color: var(--color-text-secondary);
  line-height: 1.6;
}
</style>
