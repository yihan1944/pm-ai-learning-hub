<script setup lang="ts">
import { computed } from 'vue'
import exam from '../data/exam.json'
import ExamQuestion from '../components/ExamQuestion.vue'

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
    <h1>面试题库</h1>
    <p class="subtitle">AI 产品经理岗位面试题，点击展开答题方向</p>

    <section v-for="(items, cat) in grouped" :key="cat" class="category-section">
      <h2>{{ categoryNames[cat] || cat }}</h2>
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
.subtitle {
  color: var(--color-text-muted);
  margin-bottom: 2rem;
}

.category-section {
  margin-bottom: 2.5rem;
}

.category-section h2 {
  font-size: 1.2rem;
  margin-bottom: 0.75rem;
  padding-bottom: 0.3em;
  border-bottom: 1px solid var(--color-border);
}

.question-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
</style>
