<script setup lang="ts">
import { ref } from 'vue'

const menuOpen = ref(false)

const links = [
  { to: '/', label: '首页' },
  { to: '/papers', label: '论文' },
  { to: '/products', label: '产品' },
  { to: '/knowledge', label: '知识' },
  { to: '/agents', label: 'Agent' },
  { to: '/exam', label: '面试题' },
  { to: '/search', label: '搜索' },
]
</script>

<template>
  <nav class="navbar">
    <div class="navbar-inner">
      <router-link to="/" class="navbar-brand">PM AI Hub</router-link>

      <button class="menu-toggle" @click="menuOpen = !menuOpen" aria-label="菜单">
        <span :class="{ open: menuOpen }"></span>
      </button>

      <div class="navbar-links" :class="{ open: menuOpen }">
        <router-link
          v-for="link in links"
          :key="link.to"
          :to="link.to"
          @click="menuOpen = false"
        >
          {{ link.label }}
        </router-link>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: var(--nav-height);
  background: rgba(15, 23, 42, 0.75);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--color-border);
  z-index: 100;
}

.navbar-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 1rem;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-brand {
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--color-text);
  letter-spacing: -0.02em;
}

.navbar-links {
  display: flex;
  gap: 0.25rem;
}

.navbar-links a {
  padding: 0.4em 0.75em;
  border-radius: var(--radius);
  color: var(--color-text-muted);
  font-size: 0.9rem;
  transition: background 0.2s, color 0.2s;
}

.navbar-links a:hover,
.navbar-links a.router-link-exact-active {
  background: var(--color-surface-hover);
  color: var(--color-text);
}

.menu-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  width: 28px;
  height: 28px;
  position: relative;
}

.menu-toggle span,
.menu-toggle span::before,
.menu-toggle span::after {
  display: block;
  width: 20px;
  height: 2px;
  background: var(--color-text);
  position: absolute;
  transition: transform 0.3s;
}

.menu-toggle span {
  top: 13px;
  left: 4px;
}

.menu-toggle span::before {
  content: '';
  top: -6px;
}

.menu-toggle span::after {
  content: '';
  top: 6px;
}

.menu-toggle span.open {
  background: transparent;
}

.menu-toggle span.open::before {
  transform: rotate(45deg);
  top: 0;
}

.menu-toggle span.open::after {
  transform: rotate(-45deg);
  top: 0;
}

@media (max-width: 768px) {
  .menu-toggle {
    display: block;
  }

  .navbar-links {
    position: fixed;
    top: var(--nav-height);
    left: 0;
    right: 0;
    background: var(--color-surface);
    flex-direction: column;
    padding: 0.5rem 1rem 1rem;
    border-bottom: 1px solid var(--color-border);
    display: none;
  }

  .navbar-links.open {
    display: flex;
  }

  .navbar-links a {
    padding: 0.6em 0;
  }
}
</style>
