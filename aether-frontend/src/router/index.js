import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const routes = [
  {
    path: '/',
    name: 'landing',
    component: () => import('@/views/LandingPage.vue'),
    meta: { guest: true }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('@/views/LoginPage.vue'),
    meta: { guest: true }
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('@/views/RegisterPage.vue'),
    meta: { guest: true }
  },
  {
    path: '/chat',
    name: 'chat',
    component: () => import('@/views/ChatPage.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/mood',
    name: 'mood',
    component: () => import('@/views/MoodTracking.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/resources',
    name: 'resources',
    component: () => import('@/views/ResourceCenter.vue'),
    meta: { requiresAuth: true }
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'not-found',
    component: () => import('@/views/NotFound.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    if (to.hash) return { el: to.hash, behavior: 'smooth' }
    return { top: 0, behavior: 'smooth' }
  }
})

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'login' })
  } else if (to.meta.guest && authStore.isAuthenticated && to.name !== 'landing') {
    next({ name: 'chat' })
  } else {
    next()
  }
})

export default router
