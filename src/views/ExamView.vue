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
    <div class="page-header">
      <h1>面试题库</h1>
      <p class="subtitle">AI 产品经理岗位面试题，点击展开答题方向</p>
    </div>

    <section v-for="(items, cat) in grouped" :key="cat" class="category-section">
      <div class="section-header">
        <h2>{{ categoryNames[cat] || cat }}</h2>
        <div class="line"></div>
      </div>
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

.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
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

.category-section {
  margin-bottom: 2.5rem;
}

.question-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
</style>
