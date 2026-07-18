<script setup lang="ts">
import NavBar from './components/NavBar.vue'
</script>

<template>
  <NavBar />
  <main class="container main">
    <router-view />
  </main>

  <footer class="site-footer">
    <p>Made with ✦ by <a href="https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MjU1NTk0OQ==&action=getalbum&album_id=4448591694527234049" target="_blank" rel="noopener">猿人码头</a></p>
  </footer>
</template>

<style scoped>
.main {
  padding-top: calc(var(--nav-height) + var(--space-6));
  padding-bottom: var(--space-7);
}

.site-footer {
  text-align: center;
  padding: var(--space-5) 0 var(--space-6);
  border-top: 1px solid var(--color-border);
  font-size: var(--text-xs);
  color: var(--color-text-muted);
}

.site-footer a {
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color var(--dur) var(--ease);
}

.site-footer a:hover {
  color: var(--color-primary);
}
</style>
