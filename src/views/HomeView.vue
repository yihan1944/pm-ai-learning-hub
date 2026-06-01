<script setup lang="ts">
import papers from '../data/papers.json'
import knowledge from '../data/knowledge.json'
import agents from '../data/agents.json'
import products from '../data/products.json'
import exam from '../data/exam.json'

const categories = [
  {
    title: '学习路线',
    description: `从 AI 认知到产品落地的 ${knowledge.stages.length} 阶段学习路径 + 术语表`,
    count: `${knowledge.stages.length} 个学习阶段`,
    route: '/knowledge',
    icon: 'route',
  },
  {
    title: '论文笔记',
    description: '经典 AI 论文阅读笔记，涵盖 Transformer、GPT、DeepSeek 等',
    count: `已收录 ${papers.length} 篇`,
    route: '/papers',
    icon: 'file-text',
  },
  {
    title: 'AI 产品',
    description: '产品案例、产品思维和 Prompt 工程',
    count: `${products.length} 个案例`,
    route: '/products',
    icon: 'lightbulb',
  },
  {
    title: 'Agent 资源',
    description: 'Agent 框架、设计模式和项目实践',
    count: `${agents.length} 个资源`,
    route: '/agents',
    icon: 'bot',
  },
  {
    title: '面试题库',
    description: 'AI 产品经理岗位面试题，含答题方向',
    count: `共 ${exam.length} 道`,
    route: '/exam',
    icon: 'target',
  },
  {
    title: '我的想法',
    description: 'AI 产品灵感、思考笔记和创意收集',
    count: '占坑中',
    route: '',
    icon: 'pen',
  },
]
</script>

<template>
  <div class="home">
    <section class="hero">
      <h1>PM AI Learning Hub</h1>
      <p class="hero-subtitle">构建 AI 产品经理知识体系</p>
      <p class="hero-tags">学习路线 · 论文精读 · Agent · 产品案例 · 面试题</p>
    </section>

    <section class="categories">
      <template v-for="cat in categories" :key="cat.route || cat.title">
        <router-link
          v-if="cat.route"
          :to="cat.route"
          class="category-card"
        >
          <span class="card-icon">
            <svg v-if="cat.icon === 'route'" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="19" r="3"/><path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15"/><circle cx="18" cy="5" r="3"/></svg>
            <svg v-else-if="cat.icon === 'file-text'" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/></svg>
            <svg v-else-if="cat.icon === 'lightbulb'" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/></svg>
            <svg v-else-if="cat.icon === 'bot'" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>
            <svg v-else-if="cat.icon === 'target'" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
            <svg v-else-if="cat.icon === 'pen'" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/></svg>
          </span>
          <h2>{{ cat.title }}</h2>
          <p>{{ cat.description }}</p>
          <span class="card-count">{{ cat.count }}</span>
        </router-link>
        <div v-else class="category-card placeholder">
          <span class="card-icon">
            <svg v-if="cat.icon === 'pen'" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L3.842 16.174a2 2 0 0 0-.5.83l-1.321 4.352a.5.5 0 0 0 .623.622l4.353-1.32a2 2 0 0 0 .83-.497z"/></svg>
          </span>
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
  padding: 3.5rem 0 3rem;
  position: relative;
}

.hero::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 400px;
  background: radial-gradient(circle, rgba(99, 102, 241, 0.12) 0%, transparent 65%);
  pointer-events: none;
}

.hero h1 {
  font-size: 2rem;
  font-weight: 700;
  margin-bottom: 0.6rem;
  letter-spacing: -0.02em;
  position: relative;
}

.hero-subtitle {
  color: var(--color-text-muted);
  font-size: 1.15rem;
  margin-bottom: 0.8rem;
  position: relative;
}

.hero-tags {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  opacity: 0.7;
  position: relative;
}

.categories {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: stretch;
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
  display: flex;
  flex-direction: column;
  background: var(--color-surface);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  padding: 1.25rem;
  transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  color: var(--color-text);
}

.category-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.25);
  border-color: rgba(99, 102, 241, 0.3);
  color: var(--color-text);
}

.card-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: rgba(99, 102, 241, 0.1);
  color: var(--color-primary-hover);
  margin-bottom: 0.8rem;
}

.category-card h2 {
  font-size: 1.1rem;
  margin-bottom: 0.4rem;
  font-weight: 600;
}

.category-card p {
  color: var(--color-text-muted);
  font-size: 0.88rem;
  line-height: 1.5;
  margin-bottom: 0.75rem;
}

.card-count {
  display: inline-block;
  margin-top: auto;
  background: rgba(99, 102, 241, 0.12);
  color: var(--color-primary-hover);
  padding: 0.2em 0.7em;
  border-radius: 99px;
  font-size: 0.78rem;
  font-weight: 600;
  align-self: flex-start;
}

.category-card.placeholder {
  border-style: dashed;
  opacity: 0.7;
  cursor: default;
}

.placeholder-count {
  background: rgba(148, 163, 184, 0.15);
  color: var(--color-text-muted);
}
</style>
