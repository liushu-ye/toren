<script setup lang="ts">
// 导入Vue核心API和工具
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
// 导入路由工具
import { useRouter } from 'vue-router'
// 导入侧边栏状态管理
import { useSideRailStore } from '@/stores/zhao'

// 路由实例
const router = useRouter()
// 侧边栏状态管理实例
const store = useSideRailStore()
// 侧边栏DOM引用（支持多个）
const railRef = ref<HTMLElement | null>(null)
// 自动关闭定时器引用
let closeTimer: ReturnType<typeof setTimeout> | null = null

/**
 * 点击外部区域关闭侧边栏
 * @param e 点击事件
 */
function handleClickOutside(e: MouseEvent) {
  if (!railRef.value) return

  const refs = Array.isArray(railRef.value) ? railRef.value : [railRef.value]
  const isInside = refs.some(ref => ref && ref.contains(e.target as Node))

  if (!isInside) {
    store.close()
  }
}

/**
 * 启动侧边栏自动关闭定时器
 */
function startCloseTimer() {
  clearCloseTimer()
  closeTimer = setTimeout(() => {
    store.close()
  }, 100000) // 10秒后自动关闭
}

/**
 * 清除自动关闭定时器
 */
function clearCloseTimer() {
  if (closeTimer) {
    clearTimeout(closeTimer)
    closeTimer = null
  }
}

/**
 * 处理页面刷新
 */
function handleRefresh() {
  window.location.reload()
}

/**
 * 处理页面返回
 */
function handleBack() {
  window.history.back()
}

/**
 * 监听侧边栏状态变化
 */
watch(() => store.isOpen, (newVal) => {
  if (newVal) {
    startCloseTimer() // 打开时启动自动关闭定时器
  } else {
    clearCloseTimer() // 关闭时清除定时器
  }
})

/**
 * 组件挂载时的初始化
 */
onMounted(() => {
  document.addEventListener('click', handleClickOutside) // 添加点击外部监听
})

/**
 * 组件卸载时的清理
 */
onBeforeUnmount(() => {
  document.removeEventListener('click', handleClickOutside) // 移除点击外部监听
  clearCloseTimer() // 清除定时器
})
</script>


<template>
  <!-- 左侧上部侧边栏 -->
  <div ref="railRef" class="side-rail-base side-rail-left h-50 top-[15vh]" :class="store.isOpen ? 'side-open' : 'side-closed'"
      @click.stop="store.toggle">
    <!-- 学习页面导航图标 -->
    <div class="rail-item" v-if="store.isOpen" @click.stop="router.push('/learn')"><img src="@/assets/icons/learn.svg" alt="学习"></div>
  </div>

  <!-- 左侧下部侧边栏 -->
  <div ref="railRef" class="side-rail-base side-rail-left h-40 top-[60vh]" :class="store.isOpen ? 'side-open' : 'side-closed'"
      @click.stop="store.toggle">
    <!-- 设置页面导航图标 -->
    <div class="rail-item" v-if="store.isOpen" @click.stop="router.push('/setting')"><img src="@/assets/icons/settings.svg" alt="设置"></div>
    <!-- 反馈页面导航图标 -->
    <div class="rail-item" v-if="store.isOpen" @click.stop="router.push('/feedback')"><img src="@/assets/icons/feedback.svg" alt="反馈"></div>
  </div>

  <!-- 右侧上部侧边栏 -->
  <div ref="railRef" class="side-rail-base side-rail-right h-50 top-[15vh]" :class="store.isOpen ? 'side-open' : 'side-closed'"
      @click.stop="store.toggle">
    <!-- 公共页面导航图标 -->
    <div class="rail-item" v-if="store.isOpen" @click.stop="router.push('/public')"><img src="@/assets/icons/public.svg" alt="公共"></div>
  </div>

  <!-- 右侧下部侧边栏 -->
  <div ref="railRef" class="side-rail-base side-rail-right h-60 top-[60vh]" :class="store.isOpen ? 'side-open' : 'side-closed'"
      @click.stop="store.toggle">
    <!-- 首页导航图标 -->
    <div class="rail-item" v-if="store.isOpen" @click.stop="router.push('/')"><img src="@/assets/icons/home.svg" alt="首页"></div>
    <!-- 返回上一页图标 -->
    <div class="rail-item" v-if="store.isOpen" @click.stop="handleBack()"><img src="@/assets/icons/back.svg" alt="返回"></div>
    <!-- 刷新页面图标 -->
    <div class="rail-item" v-if="store.isOpen" @click.stop="handleRefresh()"><img src="@/assets/icons/refresh.svg" alt="刷新"></div>
  </div>

  
</template>

<style scoped>
/* 组件局部样式（如果需要） */
/* global.css */
</style>
