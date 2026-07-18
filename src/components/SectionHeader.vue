<script setup lang="ts">
defineProps<{
  title: string
}>()
</script>

<template>
  <div class="section-header">
    <h2>{{ title }}</h2>
    <div class="line"></div>
  </div>
</template>

<style scoped>
.section-header {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  margin-bottom: var(--space-5);
}

h2 {
  font-size: var(--text-xl);
  font-weight: 700;
  letter-spacing: -0.02em;
  flex-shrink: 0;
}

.line {
  flex: 1;
  height: 1px;
  background: var(--color-border);
}
</style>
