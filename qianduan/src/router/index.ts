import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/pages/home.vue'),
      meta: { requiresAuth: false }, // 需要登录
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/pages/logoIn.vue'),
      meta: { requiresAuth: false }, // 不需要登录
    },
    {
      path: '/time',
      name: 'time',
      component: () => import('@/components/time.vue'),
      meta: { requiresAuth: false }, // 不需要登录
    },
    {
      path: '/learn',
      name: 'learn',
      component: () => import('@/pages/learn.vue'),
      meta: { requiresAuth: false }, // 不需要登录
    },
    {
      path: '/setting',
      name: 'setting',
      component: () => import('@/pages/setting.vue'),
      meta: { requiresAuth: false }, // 不需要登录
    },
    {
      path: '/feedback',
      name: 'feedback',
      component: () => import('@/pages/feedback.vue'),
      meta: { requiresAuth: false }, // 不需要登录
    },
    {
      path: '/public',
      name: 'public',
      component: () => import('@/pages/public.vue'),
      meta: { requiresAuth: false }, // 不需要登录
    },
    
  ],
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()

  // 使用路由元信息判断是否需要登录
  if (to.meta.requiresAuth && !userStore.isLoggedIn) {
    next('/login')
  } else {
    next()
  }
})
export default router
