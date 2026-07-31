<script setup lang="ts">
import { ref } from 'vue'
import PageHeader from '../components/PageHeader.vue'
import products from '../data/products.json'

const toastMessage = ref('')
const toastVisible = ref(false)
let toastTimer: ReturnType<typeof setTimeout> | null = null

function isMiniApp(link: string): boolean {
  return link.startsWith('#小程序://')
}

function showToast(msg: string) {
  toastMessage.value = msg
  toastVisible.value = true
  if (toastTimer) clearTimeout(toastTimer)
  toastTimer = setTimeout(() => {
    toastVisible.value = false
  }, 2500)
}

async function handleProductClick(e: Event, link: string) {
  if (!isMiniApp(link)) return
  e.preventDefault()
  try {
    await navigator.clipboard.writeText(link)
    showToast('链接已复制，请在微信中打开')
  } catch {
    // fallback for insecure contexts
    const textarea = document.createElement('textarea')
    textarea.value = link
    textarea.style.position = 'fixed'
    textarea.style.opacity = '0'
    document.body.appendChild(textarea)
    textarea.select()
    document.execCommand('copy')
    document.body.removeChild(textarea)
    showToast('链接已复制，请在微信中打开')
  }
}
</script>

<template>
  <div class="products">
    <PageHeader title="AI 产品" subtitle="产品案例、产品思维和 Prompt 工程" />

    <div v-if="products.length === 0" class="empty">
      <p>暂无产品内容，敬请期待。</p>
    </div>

    <div v-else class="product-list">
      <a
        v-for="product in products"
        :key="product.id"
        :href="product.link"
        :target="isMiniApp(product.link) ? undefined : '_blank'"
        rel="noopener"
        class="card card-link product-card"
        @click="handleProductClick($event, product.link)"
      >
        <div class="card-body">
          <h3>{{ product.title }}</h3>
          <p>{{ product.description }}</p>
        </div>
        <div class="card-footer">
          <span v-if="product.tag" class="tag">{{ product.tag }}</span>
          <span class="card-arrow">↗</span>
        </div>
      </a>
    </div>
    <Transition name="toast">
      <div v-if="toastVisible" class="toast">{{ toastMessage }}</div>
    </Transition>
  </div>
</template>

<style scoped>
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--space-4);
}

.product-card {
  display: flex;
  flex-direction: column;
}

.card-body {
  flex: 1;
}

.card-body h3 {
  font-size: var(--text-lg);
  font-weight: 600;
  letter-spacing: -0.01em;
  margin-bottom: var(--space-2);
}

.card-body p {
  font-size: var(--text-md);
  color: var(--color-text-secondary);
  line-height: 1.6;
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: var(--space-4);
  padding-top: var(--space-3);
  border-top: 1px solid var(--color-border);
}

.card-arrow {
  color: var(--color-text-muted);
  transition: transform var(--dur) var(--ease), color var(--dur) var(--ease);
}

.product-card:hover .card-arrow {
  color: var(--color-primary);
  transform: translate(2px, -2px);
}

.toast {
  position: fixed;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  background: var(--color-text);
  color: var(--color-bg);
  padding: 10px 24px;
  border-radius: 8px;
  font-size: var(--text-sm);
  white-space: nowrap;
  z-index: 1000;
  pointer-events: none;
}

.toast-enter-active,
.toast-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.toast-enter-from,
.toast-leave-to {
  opacity: 0;
  transform: translateX(-50%) translateY(8px);
}
</style>
