<script setup lang="ts">
import { ref } from 'vue'
import { useProgress } from '../composables/useProgress'
import type { LearningStage as StageType } from '../types'

const props = defineProps<{ stage: StageType }>()
const { toggle, isCompleted } = useProgress()
const expanded = ref(true)

function completedCount() {
  return props.stage.items.filter(i => isCompleted(i.id)).length
}
</script>

<template>
  <div class="stage-card">
    <div class="stage-header" @click="expanded = !expanded">
      <div>
        <h3>{{ stage.name }}</h3>
        <span class="progress-text">{{ completedCount() }} / {{ stage.items.length }} 完成</span>
      </div>
      <span class="expand-icon" :class="{ expanded }">▸</span>
    </div>

    <div class="progress-bar">
      <div
        class="progress-fill"
        :style="{ width: `${stage.items.length ? (completedCount() / stage.items.length) * 100 : 0}%` }"
      ></div>
    </div>

    <ul v-show="expanded" class="items">
      <li
        v-for="item in stage.items"
        :key="item.id"
        :class="{ done: isCompleted(item.id) }"
        @click="toggle(item.id)"
      >
        <span class="checkbox">{{ isCompleted(item.id) ? '☑' : '☐' }}</span>
        <span>{{ item.text }}</span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.stage-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  overflow: hidden;
}

.stage-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 1.25rem;
  cursor: pointer;
  user-select: none;
}

.stage-header h3 {
  font-size: 1.05rem;
}

.progress-text {
  font-size: 0.8rem;
  color: var(--color-text-muted);
}

.expand-icon {
  transition: transform 0.2s;
  color: var(--color-text-muted);
}

.expand-icon.expanded {
  transform: rotate(90deg);
}

.progress-bar {
  height: 3px;
  background: var(--color-border);
}

.progress-fill {
  height: 100%;
  background: var(--color-success);
  transition: width 0.3s;
}

.items {
  list-style: none;
  padding: 0.5rem 1.25rem 1rem;
}

.items li {
  display: flex;
  align-items: center;
  gap: 0.6em;
  padding: 0.4em 0;
  cursor: pointer;
  font-size: 0.95rem;
  transition: color 0.2s;
}

.items li.done {
  color: var(--color-text-muted);
  text-decoration: line-through;
}

.checkbox {
  flex-shrink: 0;
  font-size: 1.1rem;
}
</style>
