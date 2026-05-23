<script setup lang="ts">
import papers from '../data/papers.json'
import knowledge from '../data/knowledge.json'
import agents from '../data/agents.json'
import products from '../data/products.json'
import exam from '../data/exam.json'

const categories = [
  {
    title: '论文笔记',
    description: '经典 AI 论文阅读笔记，涵盖 Transformer、GPT、DeepSeek 等',
    count: papers.length,
    route: '/papers',
    icon: '📄',
  },
  {
    title: '学习路线',
    description: '从基础认知到 AI 产品的 5 阶段学习路径 + 术语表',
    count: knowledge.stages.length + ' 阶段',
    route: '/knowledge',
    icon: '🗺️',
  },
  {
    title: 'Agent 资源',
    description: 'Agent 框架、设计模式和项目实践',
    count: agents.length,
    route: '/agents',
    icon: '🤖',
  },
  {
    title: 'AI 产品',
    description: '产品案例、产品思维和 Prompt 工程',
    count: products.length,
    route: '/products',
    icon: '💡',
  },
  {
    title: '面试题库',
    description: 'AI 产品经理岗位面试题，含答题方向',
    count: exam.length,
    route: '/exam',
    icon: '🎯',
  },
  {
    title: '我的想法',
    description: 'AI 产品灵感、思考笔记和创意收集',
    count: '占坑中',
    route: '',
    icon: '💭',
  },
]
</script>

<template>
  <div class="home">
    <section class="hero">
      <h1>PM AI Learning Hub</h1>
      <p>AI 产品经理的学习知识库 — 论文、术语、Agent、产品、面试题</p>
    </section>

    <section class="categories">
      <template v-for="cat in categories" :key="cat.route || cat.title">
        <router-link
          v-if="cat.route"
          :to="cat.route"
          class="category-card"
        >
          <span class="card-icon">{{ cat.icon }}</span>
          <h2>{{ cat.title }}</h2>
          <p>{{ cat.description }}</p>
          <span class="card-count">{{ cat.count }}</span>
        </router-link>
        <div v-else class="category-card placeholder">
          <span class="card-icon">{{ cat.icon }}</span>
          <h2>{{ cat.title }}</h2>
          <p>{{ cat.description }}</p>
          <span class="card-count placeholder-count">{{ cat.count }}</span>
        </div>
      </template>
    </section>
  </div>
</template>

<style scoped>
.hero {
  text-align: center;
  padding: 2rem 0 3rem;
}

.hero h1 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

.hero p {
  color: var(--color-text-muted);
  font-size: 1.1rem;
}

.categories {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
}

.category-card {
  flex: 0 1 calc((100% - 2rem) / 3);
  min-width: 280px;
}

@media (max-width: 900px) {
  .category-card {
    flex: 0 1 calc((100% - 1rem) / 2);
    min-width: 240px;
  }
}

@media (max-width: 580px) {
  .category-card {
    flex: 1 1 100%;
    min-width: 0;
  }
}

.category-card {
  display: block;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 1.5rem;
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
  color: var(--color-text);
}

.category-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--color-primary);
  color: var(--color-text);
}

.card-icon {
  font-size: 2rem;
  display: block;
  margin-bottom: 0.75rem;
}

.category-card h2 {
  font-size: 1.15rem;
  margin-bottom: 0.4rem;
}

.category-card p {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  line-height: 1.5;
  margin-bottom: 0.75rem;
}

.card-count {
  display: inline-block;
  background: var(--color-primary);
  color: #fff;
  padding: 0.15em 0.6em;
  border-radius: 99px;
  font-size: 0.8rem;
  font-weight: 600;
}

.category-card.placeholder {
  border-style: dashed;
  opacity: 0.7;
  cursor: default;
}

.placeholder-count {
  background: var(--color-text-muted);
}
</style>
