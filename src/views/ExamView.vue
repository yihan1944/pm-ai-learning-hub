<script setup lang="ts">
import { computed } from 'vue'
import PageHeader from '../components/PageHeader.vue'
import SectionHeader from '../components/SectionHeader.vue'
import ExamQuestion from '../components/ExamQuestion.vue'
import exam from '../data/exam.json'

const grouped = computed(() => {
  const map: Record<string, typeof exam> = {}
  for (const q of exam) {
    if (!map[q.category]) map[q.category] = []
    map[q.category].push(q)
  }
  return map
})

const categoryNames: Record<string, string> = {
  '做AI产品-面试题': '做 AI 产品',
  '用AI做产品-面试题': '用 AI 做产品',
}
</script>

<template>
  <div class="exam">
    <PageHeader title="面试题库" subtitle="AI 产品经理岗位面试题，点击展开答题方向" />

    <section v-for="(items, cat) in grouped" :key="cat" class="category-section">
      <SectionHeader :title="categoryNames[cat] || cat" />
      <div class="question-list">
        <ExamQuestion
          v-for="q in items"
          :key="q.id"
          :question="q.question"
          :answer="q.answer"
        />
      </div>
    </section>
  </div>
</template>

<style scoped>
.category-section {
  margin-bottom: var(--space-6);
}

.question-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}
</style>
