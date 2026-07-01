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

// 生成球面上的点
function generateSpherePoints(count: number, radius: number) {
  const points: { x: number; y: number; z: number; size: number; opacity: number }[] = []
  const goldenAngle = Math.PI * (3 - Math.sqrt(5))

  for (let i = 0; i < count; i++) {
    const y = 1 - (i / (count - 1)) * 2
    const radiusAtY = Math.sqrt(1 - y * y)
    const theta = goldenAngle * i

    points.push({
      x: Math.cos(theta) * radiusAtY * radius,
      y: y * radius,
      z: Math.sin(theta) * radiusAtY * radius,
      size: 3 + Math.random() * 3.5,
      opacity: 0.6 + Math.random() * 0.4,
    })
  }
  return points
}

const spherePoints = generateSpherePoints(250, 160)

const cards = [
  {
    route: '/knowledge',
    icon: 'route',
    color: 'blue',
    title: '学习路线',
    description: `从 AI 认知到产品落地的 ${knowledge.stages.length} 阶段系统化学习路径，含术语表与进阶指引`,
    tag: `${knowledge.stages.length} 个学习阶段`,
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
  {
    route: '',
    icon: 'pen',
    color: 'purple',
    title: '我的想法',
    description: 'AI 产品灵感、思考笔记和创意收集',
    tag: '占坑中',
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
    <!-- Hero — Minimalist: left text + right rotating sphere -->
    <section class="hero">
      <div class="hero-left">
        <h1>
          Keep Learning.<br>
          Keep Building.
        </h1>
        <p class="hero-subtitle">
          AI 产品经理的学习与实践笔记。
        </p>
      </div>
      <div class="hero-right">
        <div class="sphere-container">
          <div class="sphere" :style="{ transform: `rotateY(${0}deg) rotateX(${15}deg)` }">
            <div
              v-for="(point, i) in spherePoints"
              :key="i"
              class="sphere-point"
              :style="{
                transform: `translate3d(${point.x}px, ${point.y}px, ${point.z}px)`,
                width: `${point.size}px`,
                height: `${point.size}px`,
                opacity: point.opacity,
              }"
            ></div>
          </div>
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
        <template v-for="card in cards" :key="card.route || card.title">
          <router-link
            v-if="card.route"
            :to="card.route"
            class="card fade-in"
          >
            <div class="card-body">
              <h3>{{ card.title }}</h3>
              <p>{{ card.description }}</p>
            </div>
            <div class="card-footer">
              <span class="card-tag">{{ card.tag }}</span>
              <span class="link-arrow">→</span>
            </div>
          </router-link>
          <div v-else class="card fade-in placeholder">
            <div class="card-body">
              <h3>{{ card.title }}</h3>
              <p>{{ card.description }}</p>
            </div>
            <div class="card-footer">
              <span class="card-tag">{{ card.tag }}</span>
            </div>
          </div>
        </template>
      </div>
    </section>

    <!-- Stats -->
    <section class="stats-section fade-in">
      <div class="stats-grid">
        <div v-for="s in stats" :key="s.label" class="stat-item">
          <div class="stat-num">{{ s.num }}</div>
          <div class="stat-label">{{ s.label }}</div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
/* ── Home ── */
.home {
  padding-top: 20px;
}

/* ── Hero — Minimalist ── */
.hero {
  display: flex;
  align-items: center;
  gap: 24px;
  padding: 100px 0 60px;
  min-height: calc(100vh - var(--nav-height) - 100px);
}

.hero-left {
  flex: 1;
}

.hero-left h1 {
  font-size: clamp(2.2rem, 4.5vw, 3.4rem);
  font-weight: 800;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: var(--color-text);
  margin-bottom: 20px;
}

.hero-subtitle {
  font-size: 1.1rem;
  color: var(--color-text-secondary);
  line-height: 1.75;
  max-width: 400px;
  margin-bottom: 32px;
}

.hero-right {
  flex: 1;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ── Rotating Sphere ── */
.sphere-container {
  width: 380px;
  height: 380px;
  perspective: 800px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sphere {
  position: relative;
  width: 0;
  height: 0;
  transform-style: preserve-3d;
  animation: rotateSphere 20s linear infinite;
}

@keyframes rotateSphere {
  from { transform: rotateY(0deg) rotateX(15deg); }
  to { transform: rotateY(360deg) rotateX(15deg); }
}

.sphere-point {
  position: absolute;
  background: var(--color-primary);
  border-radius: 50%;
  transform-origin: center center;
}

/* ── Section header ── */
.section-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 24px;
}

.section-header h2 {
  font-size: 1.3rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--color-text);
  flex-shrink: 0;
}

.section-header .line {
  flex: 1;
  height: 1px;
  background: var(--color-border);
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
  background: var(--color-card-bg);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: 28px;
  text-decoration: none;
  color: inherit;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.card:hover {
  background: var(--color-surface-hover);
  border-color: var(--color-border-hover);
  transform: translateY(-2px);
  box-shadow: var(--shadow);
  color: inherit;
}

.card-body h3 {
  font-size: 1.1rem;
  font-weight: 600;
  letter-spacing: -0.01em;
  margin-bottom: 6px;
  color: var(--color-text);
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
  border-top: 1px solid var(--color-border);
}

.card-tag {
  font-size: 0.75rem;
  font-weight: 500;
  padding: 3px 10px;
  border-radius: 100px;
  background: rgba(0, 0, 0, 0.04);
  color: var(--color-text-muted);
}

/* ── Placeholder card ── */
.card.placeholder {
  cursor: default;
  opacity: 0.6;
}

.card.placeholder:hover {
  transform: none;
  box-shadow: none;
}

/* ── Stats ── */
.stats-section {
  padding: 48px 0;
  border-top: 1px solid var(--color-border);
}

.stats-grid {
  display: flex;
  justify-content: center;
  gap: 64px;
}

.stat-item {
  text-align: center;
}

.stat-num {
  font-size: 2rem;
  font-weight: 800;
  color: var(--color-text);
  letter-spacing: -0.03em;
}

.stat-label {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  margin-top: 4px;
  font-weight: 500;
}

/* ── Responsive ── */
@media (max-width: 768px) {
  .hero {
    flex-direction: column;
    gap: 40px;
    padding: 40px 0;
    text-align: center;
  }

  .hero-subtitle {
    max-width: 100%;
  }

  .hero-right {
    width: 100%;
  }

  .sphere-container {
    width: 240px;
    height: 240px;
  }

  .cards-grid {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    gap: 32px;
    flex-wrap: wrap;
  }
}
</style>
