<script setup lang="ts">
import products from '../data/products.json'
</script>

<template>
  <div class="products">
    <div class="page-header">
      <h1>AI 产品</h1>
      <p class="subtitle">产品案例、产品思维和 Prompt 工程</p>
    </div>

    <div v-if="products.length === 0" class="empty">
      <p>暂无产品内容，敬请期待。</p>
    </div>

    <div v-else class="product-list">
      <a
        v-for="product in products"
        :key="product.id"
        :href="product.link"
        target="_blank"
        rel="noopener"
        class="product-card"
      >
        <div class="card-body">
          <h3>{{ product.title }}</h3>
          <p>{{ product.description }}</p>
        </div>
        <div class="card-footer">
          <span v-if="product.tag" class="tag">{{ product.tag }}</span>
          <div class="card-arrow">↗</div>
        </div>
      </a>
    </div>
  </div>
</template>

<style scoped>
.page-header {
  margin-bottom: 2.5rem;
}

.page-header h1 {
  font-size: 1.8rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: 0.4rem;
}

.subtitle {
  color: var(--color-text-secondary);
  font-size: 0.95rem;
}

.empty {
  text-align: center;
  padding: 3rem 0;
  color: var(--color-text-muted);
}

.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
}

.product-card {
  display: flex;
  flex-direction: column;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 24px;
  text-decoration: none;
  color: inherit;
  transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  overflow: hidden;
  position: relative;
}

.product-card::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: var(--radius-lg);
  padding: 1px;
  background: linear-gradient(135deg, transparent, rgba(255, 255, 255, 0.05), transparent);
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.35s;
}

.product-card:hover {
  background: var(--color-surface-hover);
  border-color: var(--color-border-hover);
  transform: translateY(-4px);
  box-shadow: var(--shadow-glow);
  color: inherit;
}

.product-card:hover::before {
  opacity: 1;
}

.card-body {
  flex: 1;
}

.card-body h3 {
  font-size: 1.1rem;
  font-weight: 600;
  margin-bottom: 8px;
}

.card-body p {
  font-size: 0.875rem;
  color: var(--color-text-secondary);
  line-height: 1.6;
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: 16px;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
}

.tag {
  font-size: 0.75rem;
  font-weight: 500;
  padding: 3px 10px;
  border-radius: 100px;
  background: rgba(255, 255, 255, 0.04);
  color: var(--color-text-muted);
}

.card-arrow {
  width: 28px;
  height: 28px;
  border-radius: 8px;
  background: rgba(255, 255, 255, 0.04);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-muted);
  font-size: 0.85rem;
  transition: all 0.25s;
}

.product-card:hover .card-arrow {
  background: rgba(255, 255, 255, 0.08);
  color: var(--color-text);
  transform: translate(2px, -2px);
}
</style>
