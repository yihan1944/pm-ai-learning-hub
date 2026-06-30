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
  transition: all 0.25s;
}

.exam-card:hover {
  border-color: var(--color-border-hover);
  background: var(--color-surface-hover);
}

.question-row {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 18px;
}

.q-icon {
  background: #6366f1;
  color: #fff;
  width: 26px;
  height: 26px;
  border-radius: 6px;
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
  transition: color 0.2s;
}

.exam-card:hover .toggle-icon {
  color: var(--color-text-secondary);
}

.answer {
  padding: 0 18px 14px;
  padding-left: calc(18px + 26px + 12px);
  color: var(--color-text-secondary);
  font-size: 0.9rem;
  line-height: 1.7;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
}
</style>
