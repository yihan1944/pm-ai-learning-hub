<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ question: string; answer: string }>()
const revealed = ref(false)
</script>

<template>
  <div class="exam-card" :class="{ revealed }" @click="revealed = !revealed">
    <div class="question-row">
      <span class="q-icon">Q</span>
      <p>{{ question }}</p>
      <span class="toggle-icon">{{ revealed ? '−' : '+' }}</span>
    </div>
    <div v-show="revealed" class="answer">
      <div v-html="answer"></div>
    </div>
  </div>
</template>

<style scoped>
.exam-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius);
  overflow: hidden;
  cursor: pointer;
  transition: border-color 0.2s;
}

.exam-card:hover {
  border-color: var(--color-primary);
}

.question-row {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 1rem;
}

.q-icon {
  background: var(--color-primary);
  color: #fff;
  width: 24px;
  height: 24px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 700;
  flex-shrink: 0;
}

.question-row p {
  flex: 1;
  font-size: 0.95rem;
  line-height: 1.5;
}

.toggle-icon {
  color: var(--color-text-muted);
  font-size: 1.2rem;
  flex-shrink: 0;
}

.answer {
  padding: 0 1rem 1rem;
  padding-left: calc(1rem + 24px + 0.75rem);
  color: var(--color-text-muted);
  font-size: 0.9rem;
  line-height: 1.6;
  border-top: 1px solid var(--color-border);
}
</style>
