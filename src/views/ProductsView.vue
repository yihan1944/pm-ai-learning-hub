<script setup lang="ts">
import productsData from '../data/products.json'

interface Product { id: string; title: string; description: string }
const products = productsData as Product[]
</script>

<template>
  <div class="products">
    <h1>AI 产品</h1>
    <p class="subtitle">产品案例、产品思维和 Prompt 工程</p>

    <div v-if="products.length === 0" class="empty">
      <p>暂无产品内容，敬请期待。</p>
    </div>

    <div v-else class="product-list">
      <div v-for="product in products" :key="product.id" class="product-card">
        <h3>{{ product.title }}</h3>
        <p>{{ product.description }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.subtitle {
  color: var(--color-text-muted);
  margin-bottom: 2rem;
}

.empty {
  text-align: center;
  padding: 3rem 0;
  color: var(--color-text-muted);
}

.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1rem;
}

.product-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 1.25rem;
}

.product-card h3 {
  font-size: 1.05rem;
  margin-bottom: 0.4em;
}

.product-card p {
  font-size: 0.9rem;
  color: var(--color-text-muted);
}
</style>
