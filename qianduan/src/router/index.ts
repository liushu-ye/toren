import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: () => import('@/pages/testHome.vue'),
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/pages/logoIn.vue')
    },
  ],
})

export default router
