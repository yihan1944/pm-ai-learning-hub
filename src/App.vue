<script setup lang="ts">
import NavBar from './components/NavBar.vue'
</script>

<template>
  <NavBar />
  <main class="container" style="padding-top: calc(var(--nav-height) + 1.5rem); padding-bottom: 3rem;">
    <router-view />
  </main>

  <footer class="site-footer">
    <p>诚意正心，缘起性空</p>
    <p class="footer-contact">
      联系方式：yihan1912@gmail.com
      <span class="footer-divider">|</span>
      公众号：<a href="https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MjU1NTk0OQ==&action=getalbum&album_id=4448591694527234049" target="_blank" rel="noopener">猿人码头</a>
    </p>
  </footer>
</template>

<style scoped>
.site-footer {
  text-align: center;
  padding: 2rem 1rem;
  color: var(--color-text-muted);
  font-size: 0.85rem;
  line-height: 1.8;
  opacity: 0.6;
  border-top: 1px solid var(--color-border);
  margin-top: 2rem;
}

.footer-contact {
  font-size: 0.8rem;
  margin-top: 0.25rem;
}

.footer-divider {
  margin: 0 0.5em;
  opacity: 0.4;
}

.site-footer a {
  color: var(--color-primary);
  text-decoration: none;
  transition: opacity 0.2s;
}

.site-footer a:hover {
  opacity: 0.8;
  text-decoration: underline;
}
</style>
