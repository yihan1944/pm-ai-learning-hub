<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'

const menuOpen = ref(false)
const scrolled = ref(false)

const links = [
  { to: '/', label: '首页' },
  { to: '/papers', label: '论文' },
  { to: '/products', label: '产品' },
  { to: '/knowledge', label: '知识' },
  { to: '/agents', label: 'Agent' },
  { to: '/exam', label: '面试题' },
]

function onScroll() {
  scrolled.value = window.scrollY > 20
}

onMounted(() => window.addEventListener('scroll', onScroll))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<template>
  <nav class="navbar" :class="{ scrolled }">
    <div class="navbar-inner">
      <router-link to="/" class="navbar-brand" @click="menuOpen = false">
        <div class="brand-icon">AI</div>
        <span>PM AI Hub</span>
      </router-link>

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

      <router-link to="/search" class="nav-search" @click="menuOpen = false">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/>
        </svg>
        <span class="search-label">搜索</span>
        <kbd>⌘K</kbd>
      </router-link>
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
  background: rgba(10, 10, 15, 0.7);
  backdrop-filter: blur(20px) saturate(1.2);
  -webkit-backdrop-filter: blur(20px) saturate(1.2);
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  z-index: 100;
  transition: all 0.3s ease;
}

.navbar.scrolled {
  background: rgba(10, 10, 15, 0.9);
  box-shadow: 0 1px 30px rgba(0, 0, 0, 0.3);
}

.navbar-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 2rem;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--color-text);
  font-weight: 700;
  font-size: 1.1rem;
}

.brand-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  background: var(--gradient-main);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 800;
  color: white;
  box-shadow: 0 2px 12px rgba(99, 102, 241, 0.3);
}

.navbar-links {
  display: flex;
  gap: 2px;
}

.navbar-links a {
  padding: 6px 14px;
  border-radius: 8px;
  color: var(--color-text-secondary);
  font-size: 0.875rem;
  font-weight: 500;
  transition: all 0.2s;
}

.navbar-links a:hover {
  color: var(--color-text);
  background: rgba(255, 255, 255, 0.05);
}

.navbar-links a.router-link-exact-active {
  color: var(--color-text);
}

.nav-search {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.06);
  color: var(--color-text-muted);
  font-size: 0.8rem;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;
}

.nav-search:hover {
  background: rgba(255, 255, 255, 0.07);
  border-color: rgba(255, 255, 255, 0.1);
  color: var(--color-text-secondary);
}

.nav-search kbd {
  font-family: inherit;
  font-size: 0.7rem;
  padding: 1px 5px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.08);
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
  .navbar-inner {
    padding: 0 1rem;
  }

  .menu-toggle {
    display: block;
  }

  .navbar-links {
    position: fixed;
    top: var(--nav-height);
    left: 0;
    right: 0;
    background: rgba(10, 10, 15, 0.95);
    backdrop-filter: blur(20px);
    flex-direction: column;
    padding: 0.5rem 1rem 1rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.04);
    display: none;
  }

  .navbar-links.open {
    display: flex;
  }

  .navbar-links a {
    padding: 0.6em 0;
  }

  .search-label {
    display: none;
  }

  .nav-search kbd {
    display: none;
  }
}
</style>
