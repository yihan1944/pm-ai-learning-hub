<script setup lang="ts">
import PageHeader from '../components/PageHeader.vue'
</script>

<template>
  <div>
    <PageHeader title="页面不存在" subtitle="你访问的页面走丢了，或者链接已失效" />
    <div class="empty">
      <router-link to="/" class="back-link">← 返回首页</router-link>
    </div>
  </div>
</template>

<style scoped>
.back-link {
  font-size: var(--text-md);
  font-weight: 500;
}
</style>
