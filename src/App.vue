<script setup lang="ts">
import NavBar from './components/NavBar.vue'
</script>

<template>
  <NavBar />
  <main class="container" style="padding-top: var(--nav-height); padding-bottom: 3rem;">
    <router-view />
  </main>

  <footer class="site-footer">
    <p>Made with ✦ by <a href="https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MjU1NTk0OQ==&action=getalbum&album_id=4448591694527234049" target="_blank" rel="noopener">猿人码头</a></p>
  </footer>
</template>

<style scoped>
.site-footer {
  text-align: center;
  padding: 24px 0 40px;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
  font-size: 0.8rem;
  color: var(--color-text-muted);
}

.site-footer a {
  color: var(--color-text-secondary);
  text-decoration: none;
  transition: color 0.2s;
}

.site-footer a:hover {
  color: #6366f1;
}
</style>
