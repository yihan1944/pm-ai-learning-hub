<script setup lang="ts">
interface Product { id: string; title: string; description: string; tag?: string; link?: string }

const products: Product[] = [
  {
    id: 'bianzhou-wangshi',
    title: '汴州往事',
    description: '隋末汴州，信息掮客顾衡以为自己在收割，却不知早已是别人棋盘上的棋子。',
    tag: '武侠小说',
    link: 'https://yihan1944.github.io/bianzhou-wangshi/index.html'
  },
  {
    id: 'sanguo-renwu',
    title: '三国人物',
    description: '探讨三国人物如何在乱世中生存的历史人物随笔。',
    tag: '历史随笔',
    link: 'https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MjM5MjU1NTk0OQ==&action=getalbum&album_id=4448591694527234049'
  },
  {
    id: 'dream-diary',
    title: '梦境笔记',
    description: '记录梦境，分析梦境，接入 DeepSeek 解构、分析梦境。',
    tag: '梦境分析',
    link: 'https://dream-diary-virid.vercel.app/'
  }
]
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
  padding: 0.2em 0.6em;
  border-radius: 999px;
  background: var(--color-primary);
  color: #fff;
  white-space: nowrap;
  margin-bottom: 0.6em;
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
