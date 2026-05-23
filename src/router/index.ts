import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: () => import('../views/HomeView.vue') },
    { path: '/papers', name: 'papers', component: () => import('../views/PapersView.vue') },
    { path: '/papers/:id', name: 'paper-detail', component: () => import('../views/PaperDetailView.vue') },
    { path: '/knowledge', name: 'knowledge', component: () => import('../views/KnowledgeView.vue') },
    { path: '/agents', name: 'agents', component: () => import('../views/AgentsView.vue') },
    { path: '/products', name: 'products', component: () => import('../views/ProductsView.vue') },
    { path: '/exam', name: 'exam', component: () => import('../views/ExamView.vue') },
    { path: '/search', name: 'search', component: () => import('../views/SearchView.vue') },
  ],
  scrollBehavior() {
    return { top: 0 }
  },
})

export default router
