<script setup lang="ts">
import { ref, watch, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

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

// 路由变化时收起移动菜单
watch(() => route.path, () => {
  menuOpen.value = false
})

function onScroll() {
  scrolled.value = window.scrollY > 20
}

function onKeydown(e: KeyboardEvent) {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
    e.preventDefault()
    menuOpen.value = false
    router.push('/search')
  } else if (e.key === 'Escape') {
    menuOpen.value = false
  }
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('keydown', onKeydown)
})

onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('keydown', onKeydown)
})
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
        <span class="search-label">搜索文章、论文、产品…</span>
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
  /* --color-bg 的半透明版本 */
  background: rgba(250, 248, 243, 0.92);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--color-border);
  z-index: 100;
  transition: background var(--dur) var(--ease), box-shadow var(--dur) var(--ease);
}

.navbar.scrolled {
  background: rgba(250, 248, 243, 0.97);
  box-shadow: var(--shadow-sm);
}

.navbar-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 var(--space-5);
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.navbar-brand {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  text-decoration: none;
  color: var(--color-text);
  font-weight: 600;
  font-size: var(--text-base);
  letter-spacing: -0.01em;
}

.brand-icon {
  width: 24px;
  height: 24px;
  border-radius: var(--radius-sm);
  background: var(--color-text);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.6rem;
  font-weight: 800;
  color: var(--color-bg);
}

.navbar-links {
  display: flex;
  gap: 2px;
}

.navbar-links a {
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  color: var(--color-text-secondary);
  font-size: var(--text-sm);
  font-weight: 500;
  letter-spacing: 0.02em;
  transition: color var(--dur) var(--ease), background var(--dur) var(--ease);
}

.navbar-links a:hover {
  color: var(--color-text);
  background: var(--color-surface-sunken);
}

.navbar-links a.router-link-exact-active {
  color: var(--color-text);
  font-weight: 600;
}

.nav-search {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  background: var(--color-surface-sunken);
  border: 1px solid var(--color-border);
  color: var(--color-text-muted);
  font-size: var(--text-xs);
  cursor: pointer;
  transition: border-color var(--dur) var(--ease), color var(--dur) var(--ease);
  text-decoration: none;
}

.nav-search:hover {
  border-color: var(--color-border-strong);
  color: var(--color-text-secondary);
}

.nav-search kbd {
  font-family: inherit;
  font-size: 0.7rem;
  padding: 1px 5px;
  border-radius: 4px;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
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
  transition: transform var(--dur) var(--ease);
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
    padding: 0 var(--space-4);
  }

  .menu-toggle {
    display: block;
  }

  .navbar-links {
    position: fixed;
    top: var(--nav-height);
    left: 0;
    right: 0;
    background: var(--color-bg);
    flex-direction: column;
    padding: var(--space-2) var(--space-4) var(--space-4);
    border-bottom: 1px solid var(--color-border);
    display: none;
  }

  .navbar-links.open {
    display: flex;
  }

  .navbar-links a {
    padding: 0.6em 0;
  }

  .search-label,
  .nav-search kbd {
    display: none;
  }
}
</style>
