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
  <div class="card stage-card">
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
        <span class="cbx" :class="{ checked: isCompleted(item.id) }"></span>
        <span class="item-text">{{ item.text }}</span>
      </li>
    </ul>
  </div>
</template>

<style scoped>
.stage-card {
  padding: 0;
  overflow: hidden;
}

.stage-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: var(--space-4) var(--space-5);
  cursor: pointer;
  user-select: none;
  transition: background var(--dur) var(--ease);
}

.stage-header:hover {
  background: var(--color-surface-sunken);
}

.stage-header h3 {
  font-size: var(--text-base);
  font-weight: 600;
}

.progress-text {
  font-size: var(--text-xs);
  color: var(--color-text-muted);
  margin-top: 2px;
}

.expand-icon {
  transition: transform var(--dur) var(--ease);
  color: var(--color-text-muted);
  font-size: var(--text-sm);
}

.expand-icon.expanded {
  transform: rotate(90deg);
}

.progress-bar {
  height: 4px;
  background: var(--color-surface-sunken);
}

.progress-fill {
  height: 100%;
  background: var(--color-primary);
  border-radius: 0 2px 2px 0;
  transition: width 0.3s var(--ease);
}

.items {
  list-style: none;
  padding: var(--space-2) var(--space-5) var(--space-4);
}

.items li {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: 6px 0;
  cursor: pointer;
  font-size: var(--text-md);
}

/* CSS 复选框（替代 ☐/☑ 字符，跨平台渲染一致） */
.cbx {
  flex-shrink: 0;
  width: 15px;
  height: 15px;
  border: 1.5px solid var(--color-border-strong);
  border-radius: 4px;
  position: relative;
  transition: background var(--dur) var(--ease), border-color var(--dur) var(--ease);
}

.cbx.checked {
  background: var(--color-primary);
  border-color: var(--color-primary);
}

.cbx.checked::after {
  content: '';
  position: absolute;
  left: 4px;
  top: 1px;
  width: 4px;
  height: 8px;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.items li.done .item-text {
  color: var(--color-text-muted);
  text-decoration: line-through;
  text-decoration-color: var(--color-border-strong);
}
</style>
