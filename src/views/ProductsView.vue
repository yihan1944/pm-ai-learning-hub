<script setup lang="ts">
import products from '../data/products.json'
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
        <span v-if="product.tag" class="tag">{{ product.tag }}</span>
        <p>{{ product.description }}</p>
        <a v-if="product.link" :href="product.link" target="_blank" rel="noopener" class="card-link">
          访问产品 →
        </a>
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
  display: flex;
  flex-direction: column;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
}

.product-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-primary);
}

.product-card h3 {
  font-size: 1.05rem;
  margin: 0 0 0.4em;
}

.tag {
  display: inline-block;
  font-size: 0.75rem;
  padding: 0.2em 0.7em;
  border-radius: 999px;
  background: rgba(99, 102, 241, 0.15);
  color: var(--color-primary-hover);
  white-space: nowrap;
  margin-bottom: 0.6em;
  align-self: flex-start;
}

.product-card p {
  font-size: 0.9rem;
  color: var(--color-text-muted);
  margin-bottom: 1em;
}

.card-link {
  display: inline-block;
  margin-top: auto;
  font-size: 0.85rem;
  color: var(--color-primary);
  text-decoration: none;
  font-weight: 500;
}

.card-link:hover {
  text-decoration: underline;
}
</style>
