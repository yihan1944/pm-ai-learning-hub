<script setup lang="ts">
import PageHeader from '../components/PageHeader.vue'
import products from '../data/products.json'
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
        target="_blank"
        rel="noopener"
        class="card card-link product-card"
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
</style>
