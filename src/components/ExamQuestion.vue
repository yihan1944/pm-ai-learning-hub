<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ question: string; answer: string }>()
const revealed = ref(false)
</script>

<template>
  <div class="card exam-card" :class="{ revealed }" @click="revealed = !revealed">
    <div class="question-row">
      <span class="q-icon">Q</span>
      <p>{{ question }}</p>
      <span class="toggle-icon">{{ revealed ? '−' : '+' }}</span>
    </div>
    <div v-show="revealed" class="answer">
      <div class="prose-compact" v-html="answer"></div>
    </div>
  </div>
</template>

<style scoped>
.exam-card {
  padding: 0;
  overflow: hidden;
  cursor: pointer;
  transition: border-color var(--dur) var(--ease);
}

.exam-card:hover {
  border-color: var(--color-border-strong);
}

.exam-card.revealed {
  border-color: var(--color-border-strong);
}

.question-row {
  display: flex;
  align-items: flex-start;
  gap: var(--space-3);
  padding: var(--space-4);
}

.q-icon {
  background: var(--color-primary);
  color: #fff;
  width: 24px;
  height: 24px;
  border-radius: var(--radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: var(--text-xs);
  font-weight: 700;
  flex-shrink: 0;
}

.question-row p {
  flex: 1;
  font-size: var(--text-md);
  line-height: 1.6;
}

.toggle-icon {
  color: var(--color-text-muted);
  font-size: var(--text-lg);
  line-height: 1.2;
  flex-shrink: 0;
  transition: color var(--dur) var(--ease);
}

.exam-card:hover .toggle-icon {
  color: var(--color-text);
}

.answer {
  padding: var(--space-4);
  padding-left: calc(var(--space-4) + 24px + var(--space-3));
  border-top: 1px solid var(--color-border);
  color: var(--color-text-secondary);
}
</style>
