/**
 * 头像组件
 * 支持图片显示、文字占位、在线状态指示
 */
<script setup lang="ts">
import { computed } from 'vue'

// 尺寸类型定义
type AvatarSize = 'sm' | 'md' | 'lg'

// 组件属性
const props = withDefaults(defineProps<{
  src?: string // 头像图片地址
  alt?: string // 图片替代文本
  name?: string // 用户名称（用于生成占位符）
  size?: AvatarSize // 头像尺寸
  isOnline?: boolean // 是否显示在线状态
  square?: boolean // 是否使用方形头像
}>(), {
  size: 'md', // 默认中等尺寸
  isOnline: false, // 默认不显示在线状态
  square: false // 默认圆形头像
})

// 尺寸样式映射
const sizeMap: Record<AvatarSize, string> = {
  sm: 'w-9 h-9 text-xs', // 小尺寸
  md: 'w-12 h-12 text-sm', // 中等尺寸
  lg: 'w-16 h-16 text-base' // 大尺寸
}

// 在线状态点尺寸映射
const statusSizeMap: Record<AvatarSize, string> = {
  sm: 'w-2.5 h-2.5', // 小尺寸状态点
  md: 'w-3 h-3', // 中等尺寸状态点
  lg: 'w-3.5 h-3.5' // 大尺寸状态点
}

// 头像容器样式
const avatarClass = computed(() => [
  'flex items-center justify-center overflow-hidden',
  'border border-white shadow-sm bg-slate-100 text-slate-500',
  'transition-transform duration-200 hover:scale-105',
  props.square ? 'rounded-lg' : 'rounded-full',
  sizeMap[props.size]
])

// 在线状态样式
const onlineClass = computed(() => [
  'absolute bottom-0 right-0 rounded-full bg-emerald-500 border-2 border-white',
  statusSizeMap[props.size]
])

// 是否有有效头像
const hasImage = computed(() => Boolean(props.src))

// 生成名字首字母
const initial = computed(() => {
  if (!props.name) return '?'
  return props.name.trim().charAt(0).toUpperCase()
})
</script>

<template>
  <div class="relative inline-flex">
    <!-- 图片头像 -->
    <img
      v-if="hasImage"
      :src="src"
      :alt="alt || 'User Avatar'"
      :class="avatarClass"
      class="object-cover"
    />

    <!-- 文字占位头像 -->
    <div v-else :class="avatarClass">
      <span class="font-medium select-none">{{ initial }}</span>
    </div>

    <!-- 在线状态指示器 -->
    <span v-if="isOnline" :class="onlineClass" />
  </div>
</template>
