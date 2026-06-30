<script setup lang="ts">
import { onMounted } from 'vue'
import papers from '../data/papers.json'
import knowledge from '../data/knowledge.json'
import products from '../data/products.json'
import exam from '../data/exam.json'

const stats = [
  { num: knowledge.stages.length, label: '学习阶段' },
  { num: papers.length, label: '论文笔记' },
  { num: exam.length, label: '面试题' },
  { num: products.length, label: '产品案例' },
]

const cards = [
  {
    route: '/knowledge',
    icon: 'route',
    color: 'blue',
    title: '学习路线',
    description: `从 AI 认知到产品落地的 ${knowledge.stages.length} 阶段系统化学习路径，含术语表与进阶指引`,
    tag: `${knowledge.stages.length} 个学习阶段`,
    wide: true,
  },
  {
    route: '/papers',
    icon: 'book',
    color: 'purple',
    title: '论文笔记',
    description: '经典 AI 论文阅读笔记，涵盖 Transformer、GPT、DeepSeek 等核心架构',
    tag: `已收录 ${papers.length} 篇`,
  },
  {
    route: '/products',
    icon: 'grid',
    color: 'cyan',
    title: 'AI 产品',
    description: '产品案例分析、产品思维方法论与 Prompt 工程实战技巧',
    tag: `${products.length} 个案例`,
  },
  {
    route: '/agents',
    icon: 'bot',
    color: 'green',
    title: 'Agent 资源',
    description: 'Agent 框架、设计模式和项目实践资源汇总',
    tag: '持续更新',
  },
  {
    route: '/exam',
    icon: 'smile',
    color: 'rose',
    title: '面试题库',
    description: 'AI 产品经理岗位高频面试题，含答题方向与思路指引',
    tag: `共 ${exam.length} 道`,
  },
]

onMounted(() => {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          setTimeout(() => entry.target.classList.add('visible'), i * 80)
          observer.unobserve(entry.target)
        }
      })
    },
    { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
  )
  document.querySelectorAll('.fade-in').forEach((el) => observer.observe(el))
})
</script>

<template>
  <div class="home">
    <!-- Background effects -->
    <div class="bg-grid"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <!-- Hero -->
    <section class="hero">
      <div class="hero-badge">
        <span class="hero-badge-dot">✦</span>
        AI 产品经理学习平台
      </div>
      <h1>
        <span class="gradient-text">PM AI</span> Learning Hub
      </h1>
      <p class="hero-subtitle">
        从 AI 认知到产品落地，系统化学习路径。<br>
        覆盖论文精读、产品思维、Agent 实践与面试准备。
      </p>
      <div class="hero-stats">
        <div v-for="s in stats" :key="s.label" class="hero-stat">
          <div class="hero-stat-num">{{ s.num }}</div>
          <div class="hero-stat-label">{{ s.label }}</div>
        </div>
      </div>
    </section>

    <!-- Cards -->
    <section class="cards-section">
      <div class="section-header">
        <h2>探索学习</h2>
        <div class="line"></div>
      </div>

      <div class="cards-grid">
        <router-link
          v-for="card in cards"
          :key="card.route"
          :to="card.route"
          class="card fade-in"
          :class="{ wide: card.wide }"
        >
          <div class="card-icon" :class="card.color">
            <!-- route -->
            <svg v-if="card.icon === 'route'" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12h4l3 8 4-16 3 8h4"/></svg>
            <!-- book -->
            <svg v-else-if="card.icon === 'book'" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/></svg>
            <!-- grid -->
            <svg v-else-if="card.icon === 'grid'" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M9 21V9"/></svg>
            <!-- bot -->
            <svg v-else-if="card.icon === 'bot'" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/></svg>
            <!-- smile (exam) -->
            <svg v-else-if="card.icon === 'smile'" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" x2="9.01" y1="9" y2="9"/><line x1="15" x2="15.01" y1="9" y2="9"/></svg>
          </div>
          <div class="card-body">
            <h3>{{ card.title }}</h3>
            <p>{{ card.description }}</p>
          </div>
          <div class="card-footer">
            <span class="card-tag">{{ card.tag }}</span>
            <div class="card-arrow">↗</div>
          </div>
        </router-link>
      </div>
    </section>

    <!-- Thoughts -->
    <section class="thoughts-section">
      <div class="section-header">
        <h2>我的想法</h2>
        <div class="line"></div>
      </div>

      <div class="thoughts-card fade-in">
        <div class="thoughts-content">
          <p>
            AI 不只是一个技术浪潮，它正在重新定义「产品经理」这个角色的边界。
            从 Prompt 工程到 Agent 架构，从论文理解到产品落地——PM 需要建立一套全新的认知框架。
          </p>
          <p>
            这个站点记录我的学习路径：读过的论文、做过的产品思考、踩过的坑。
            不追求大而全，只记录真正有收获的内容。希望对你也有帮助。
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ── Background ── */
.home {
  position: relative;
}

.bg-grid {
  position: fixed;
  inset: 0;
  z-index: -2;
  background-image:
    radial-gradient(ellipse 80% 50% at 50% -20%, rgba(99, 102, 241, 0.12), transparent),
    radial-gradient(ellipse 60% 40% at 80% 60%, rgba(168, 85, 247, 0.06), transparent),
    radial-gradient(ellipse 50% 30% at 20% 80%, rgba(6, 182, 212, 0.06), transparent);
  pointer-events: none;
}

.bg-grid::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255, 255, 255, 0.015) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
  background-size: 60px 60px;
  mask-image: radial-gradient(ellipse 70% 60% at 50% 30%, black, transparent);
}

.orb {
  position: fixed;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.4;
  pointer-events: none;
  z-index: -1;
  animation: float 20s ease-in-out infinite;
}

.orb-1 { width: 400px; height: 400px; background: #6366f1; top: -100px; left: -100px; animation-delay: 0s; }
.orb-2 { width: 350px; height: 350px; background: #a855f7; top: 50%; right: -80px; animation-delay: -7s; }
.orb-3 { width: 300px; height: 300px; background: #06b6d4; bottom: -50px; left: 30%; animation-delay: -14s; }

@keyframes float {
  0%, 100% { transform: translate(0, 0) scale(1); }
  33% { transform: translate(30px, -20px) scale(1.05); }
  66% { transform: translate(-20px, 15px) scale(0.95); }
}

/* ── Hero ── */
.hero {
  padding-top: 60px;
  padding-bottom: 60px;
  text-align: center;
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px 6px 8px;
  border-radius: 100px;
  background: rgba(99, 102, 241, 0.08);
  border: 1px solid rgba(99, 102, 241, 0.15);
  font-size: 0.8rem;
  color: #818cf8;
  font-weight: 500;
  margin-bottom: 28px;
  animation: fadeInUp 0.6s ease-out;
}

.hero-badge-dot {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #6366f1;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.65rem;
}

.hero h1 {
  font-size: clamp(2.5rem, 5vw, 3.8rem);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.03em;
  margin-bottom: 18px;
  animation: fadeInUp 0.6s ease-out 0.1s both;
}

.gradient-text {
  background: var(--gradient-main);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-subtitle {
  font-size: 1.1rem;
  color: var(--color-text-secondary);
  max-width: 560px;
  margin: 0 auto 40px;
  line-height: 1.7;
  font-weight: 400;
  animation: fadeInUp 0.6s ease-out 0.2s both;
}

.hero-stats {
  display: flex;
  justify-content: center;
  gap: 48px;
  animation: fadeInUp 0.6s ease-out 0.3s both;
}

.hero-stat {
  text-align: center;
}

.hero-stat-num {
  font-size: 1.8rem;
  font-weight: 700;
  color: var(--color-text);
  letter-spacing: -0.02em;
}

.hero-stat-label {
  font-size: 0.8rem;
  color: var(--color-text-muted);
  margin-top: 4px;
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ── Section header ── */
.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 28px;
}

.section-header h2 {
  font-size: 1.35rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.section-header .line {
  flex: 1;
  height: 1px;
  background: linear-gradient(90deg, rgba(255, 255, 255, 0.08), transparent);
}

/* ── Cards ── */
.cards-section {
  padding-bottom: 48px;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
  gap: 16px;
}

.card {
  position: relative;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 28px;
  text-decoration: none;
  color: inherit;
  transition: all 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.card::before {
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

.card:hover {
  background: var(--color-surface-hover);
  border-color: var(--color-border-hover);
  transform: translateY(-4px);
  box-shadow: var(--shadow-glow);
  color: inherit;
}

.card:hover::before {
  opacity: 1;
}

.card-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.card-icon::after {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 12px;
  opacity: 0.15;
}

.card-icon.blue { background: rgba(99, 102, 241, 0.1); color: #818cf8; }
.card-icon.blue::after { background: #6366f1; }
.card-icon.purple { background: rgba(168, 85, 247, 0.1); color: #c084fc; }
.card-icon.purple::after { background: #a855f7; }
.card-icon.cyan { background: rgba(6, 182, 212, 0.1); color: #22d3ee; }
.card-icon.cyan::after { background: #06b6d4; }
.card-icon.green { background: rgba(16, 185, 129, 0.1); color: #34d399; }
.card-icon.green::after { background: #10b981; }
.card-icon.rose { background: rgba(244, 63, 94, 0.1); color: #fb7185; }
.card-icon.rose::after { background: #f43f5e; }

.card-body h3 {
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  margin-bottom: 6px;
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
  margin-top: auto;
  padding-top: 12px;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
}

.card-tag {
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

.card:hover .card-arrow {
  background: rgba(255, 255, 255, 0.08);
  color: var(--color-text);
  transform: translate(2px, -2px);
}

/* Wide card */
.card.wide {
  grid-column: 1 / -1;
  flex-direction: row;
  align-items: center;
  gap: 32px;
  padding: 32px 36px;
}

.card.wide .card-icon {
  width: 56px;
  height: 56px;
  flex-shrink: 0;
}

.card.wide .card-body h3 {
  font-size: 1.25rem;
}

/* ── Thoughts ── */
.thoughts-section {
  padding-bottom: 80px;
}

.thoughts-card {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 36px;
  position: relative;
  overflow: hidden;
}

.thoughts-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 2px;
  background: var(--gradient-main);
  opacity: 0.5;
}

.thoughts-content {
  font-size: 0.95rem;
  color: var(--color-text-secondary);
  line-height: 1.8;
}

.thoughts-content p {
  margin-bottom: 12px;
}

.thoughts-content p:last-child {
  margin-bottom: 0;
}

/* ── Responsive ── */
@media (max-width: 768px) {
  .hero { padding-top: 40px; padding-bottom: 40px; }
  .hero-stats { gap: 32px; }
  .cards-grid { grid-template-columns: 1fr; }
  .card.wide { flex-direction: column; gap: 20px; }
  .thoughts-card { padding: 24px; }
}
</style>
