<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import SectionHeader from '../components/SectionHeader.vue'
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

// 生成球面上的点（Fibonacci 球面均匀分布）
interface SpherePoint {
  x: number
  y: number
  z: number
  size: number
  opacity: number
  twinkle: boolean
  delay: number
}

function generateSpherePoints(count: number, radius: number): SpherePoint[] {
  const points: SpherePoint[] = []
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
      opacity: 0.45 + Math.random() * 0.4,
      twinkle: i % 3 === 0, // 只有部分点闪烁，降低动画开销
      delay: Math.random() * 8,
    })
  }
  return points
}

const spherePoints = generateSpherePoints(130, 190)

// 球体滚出视口时暂停动画
const sphereRef = ref<HTMLElement | null>(null)
const spherePaused = ref(false)

let io: IntersectionObserver | null = null

onMounted(() => {
  if (sphereRef.value) {
    io = new IntersectionObserver(([entry]) => {
      spherePaused.value = !entry.isIntersecting
    })
    io.observe(sphereRef.value)
  }
})

onUnmounted(() => io?.disconnect())

const cards = [
  {
    route: '/knowledge',
    title: '学习路线',
    description: `从 AI 认知到产品落地的 ${knowledge.stages.length} 阶段系统化学习路径，含术语表与进阶指引`,
    tag: `${knowledge.stages.length} 个学习阶段`,
  },
  {
    route: '/papers',
    title: '论文笔记',
    description: '经典 AI 论文阅读笔记，涵盖 Transformer、GPT、DeepSeek 等核心架构',
    tag: `已收录 ${papers.length} 篇`,
  },
  {
    route: '/products',
    title: 'AI 产品',
    description: '产品案例分析、产品思维方法论与 Prompt 工程实战技巧',
    tag: `${products.length} 个案例`,
  },
  {
    route: '/agents',
    title: 'Agent 资源',
    description: 'Agent 框架、设计模式和项目实践资源汇总',
    tag: '持续更新',
  },
  {
    route: '/exam',
    title: '面试题库',
    description: 'AI 产品经理岗位高频面试题，含答题方向与思路指引',
    tag: `共 ${exam.length} 道`,
  },
  {
    route: '',
    title: '我的想法',
    description: 'AI 产品灵感、思考笔记和创意收集',
    tag: '占坑中',
  },
]
</script>

<template>
  <div class="home">
    <!-- Hero：左文案 + 右旋转球体 -->
    <section class="hero">
      <div class="hero-left">
        <h1 class="hero-title">
          Keep Learning.<br>
          Keep Building.
        </h1>
        <p class="hero-subtitle">
          AI 产品经理的学习与实践笔记。
        </p>
      </div>
      <div class="hero-right">
        <div ref="sphereRef" class="sphere-container" :class="{ paused: spherePaused }">
          <div class="sphere">
            <div
              v-for="(point, i) in spherePoints"
              :key="i"
              class="sphere-point"
              :class="{ twinkle: point.twinkle }"
              :style="{
                transform: `translate3d(${point.x}px, ${point.y}px, ${point.z}px)`,
                width: `${point.size}px`,
                height: `${point.size}px`,
                opacity: point.opacity,
                '--twinkle-delay': point.delay,
              }"
            ></div>
          </div>
        </div>
      </div>
    </section>

    <!-- 导航卡片 -->
    <section class="cards-section">
      <SectionHeader title="探索学习" />

      <div class="cards-grid">
        <template v-for="(card, index) in cards" :key="card.route || card.title">
          <router-link
            v-if="card.route"
            :to="card.route"
            class="card card-link card-item anim-fade-up"
            :style="{ '--i': index }"
          >
            <div class="card-body">
              <h3>{{ card.title }}</h3>
              <p>{{ card.description }}</p>
            </div>
            <div class="card-footer">
              <span class="tag">{{ card.tag }}</span>
              <span class="link-arrow">→</span>
            </div>
          </router-link>
          <div
            v-else
            class="card card-item is-placeholder anim-fade-up"
            :style="{ '--i': index }"
          >
            <div class="card-body">
              <h3>{{ card.title }}</h3>
              <p>{{ card.description }}</p>
            </div>
            <div class="card-footer">
              <span class="tag">{{ card.tag }}</span>
            </div>
          </div>
        </template>
      </div>
    </section>

    <!-- 统计 -->
    <section class="stats-section anim-fade-up">
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
/* ── Hero ── */
.hero {
  display: flex;
  align-items: center;
  gap: var(--space-5);
  padding: var(--space-6) 0 var(--space-7);
}

.hero-left {
  flex: 1;
}

.hero-title {
  font-size: var(--text-hero);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.03em;
  margin-bottom: var(--space-4);
}

.hero-subtitle {
  font-size: var(--text-lg);
  color: var(--color-text-secondary);
  max-width: 400px;
}

.hero-right {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* ── 旋转球体 ── */
.sphere-container {
  width: 450px;
  height: 450px;
  perspective: 800px;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0.85;
  animation: floatSphere 8s ease-in-out infinite;
}

.sphere {
  position: relative;
  width: 0;
  height: 0;
  transform-style: preserve-3d;
  will-change: transform;
  animation: rotateSphere 20s linear infinite;
}

.sphere-point {
  position: absolute;
  background: var(--color-primary);
  border-radius: 50%;
}

.sphere-point.twinkle {
  animation: twinkle 4s ease-in-out infinite;
  animation-delay: calc(var(--twinkle-delay, 0) * 1s);
}

.sphere-container.paused .sphere,
.sphere-container.paused .sphere-point,
.sphere-container.paused {
  animation-play-state: paused;
}

@keyframes rotateSphere {
  from { transform: rotateY(0deg) rotateX(15deg); }
  to { transform: rotateY(360deg) rotateX(15deg); }
}

@keyframes floatSphere {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}

@keyframes twinkle {
  0%, 100% { opacity: inherit; }
  50% { opacity: 0.3; }
}

/* ── 卡片 ── */
.cards-section {
  padding-bottom: var(--space-7);
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: var(--space-4);
}

.card-item {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  animation-delay: calc(var(--i, 0) * 60ms);
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
  margin-top: auto;
  padding-top: var(--space-3);
  border-top: 1px solid var(--color-border);
}

.link-arrow {
  color: var(--color-text-muted);
  transition: transform var(--dur) var(--ease), color var(--dur) var(--ease);
}

.card-link:hover .link-arrow {
  color: var(--color-primary);
  transform: translateX(3px);
}

.is-placeholder {
  opacity: 0.55;
}

/* ── 统计 ── */
.stats-section {
  padding: var(--space-7) 0;
  border-top: 1px solid var(--color-border);
}

.stats-grid {
  display: flex;
  justify-content: center;
  gap: var(--space-8);
}

.stat-item {
  text-align: center;
}

.stat-num {
  font-size: var(--text-2xl);
  font-weight: 700;
  letter-spacing: -0.03em;
}

.stat-label {
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  margin-top: var(--space-1);
  font-weight: 500;
}

/* ── 响应式 ── */
@media (max-width: 768px) {
  .hero {
    flex-direction: column;
    gap: var(--space-6);
    text-align: center;
  }

  .hero-subtitle {
    max-width: 100%;
  }

  .hero-right {
    width: 100%;
  }

  .sphere-container {
    width: 280px;
    height: 280px;
  }

  .cards-grid {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    gap: var(--space-6);
    flex-wrap: wrap;
  }
}
</style>
