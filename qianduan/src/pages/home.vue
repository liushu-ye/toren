<template>
  <div class="task-page">
    顶部导航
    <main class="task-main">
      筛选
      <div class="task-grid">
        <template
          v-for="(task, index) in taskList"
          :key="task.id"
        >
          <!-- 每 9 个位置插入一个大卡（8 小 + 1 大） -->
          <TaskBigCard
            v-if="isBigCard(index)"
            :task="task"
            :border-color="getBorderColor(task.level)"
            :text-color="getTextColor(task.level)"
            :badge-bg="getBadgeBg(task.level)"
            @click="openDetail"
          />

          <TaskSmallCard
            v-else
            :task="task"
            :border-color="getBorderColor(task.level)"
            :text-color="getTextColor(task.level)"
            @click="openDetail"
          />
        </template>
      </div>

      <div class="task-footer">
        —— 到底了 冒险者 ——
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
import TaskBigCard from '@/components/home/LargeCard.vue'
import TaskSmallCard from '@/components/home/SmallCard.vue'

/**
 * 列表页逻辑
 */

// 每组：8 个小卡 + 1 个大卡
const SMALL_COUNT = 8

const isBigCard = (index: number) => {
  // index 从 0 开始，所以 +1
  return (index + 1) % (SMALL_COUNT + 1) === 0
}

const taskList = [
  {
    id: 1,
    title: '菜鸟驿站快递分拣',
    desc: '轻松简单，室内作业',
    wage: 25,
    unit: '时',
    stamina: 20,
    level: 'E',
    tag: '简单',
    distance: 0.3,
    image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80'
  },
   { id: 2, title: '食堂餐盘回收', desc: '饭点高峰期协助', wage: 23, unit: '时', stamina: 15, level: 'E', tag: '简单', distance: 0.1, image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' },
  { id: 3, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
  { id: 4, title: '图书馆闭馆整理', desc: '将归还书籍上架', wage: 24, unit: '时', stamina: 20, level: 'E', tag: '简单', distance: 0.5, image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=400&q=80' },
  { id: 5, title: '线上文案编辑', desc: '小红书风格，远程结算', wage: 30, unit: '篇', stamina: 10, level: 'C', tag: '中等', distance: 0.0, image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80' },
  { id: 6, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
  { id: 7, title: '食堂餐盘回收', desc: '饭点高峰期协助', wage: 23, unit: '时', stamina: 15, level: 'E', tag: '简单', distance: 0.1, image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' },
  { id: 8, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
  { id: 9, title: '食堂餐盘回收', desc: '饭点高峰期协助', wage: 23, unit: '时', stamina: 15, level: 'E', tag: '简单', distance: 0.1, image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' },
  { id: 10, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
  { id: 11, title: '食堂餐盘回收', desc: '饭点高峰期协助', wage: 23, unit: '时', stamina: 15, level: 'E', tag: '简单', distance: 0.1, image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' },
  { id: 12, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
  { id: 13, title: '食堂餐盘回收', desc: '饭点高峰期协助', wage: 23, unit: '时', stamina: 15, level: 'E', tag: '简单', distance: 0.1, image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' },
  { id: 14, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
   { id: 12, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
  { id: 13, title: '食堂餐盘回收', desc: '饭点高峰期协助', wage: 23, unit: '时', stamina: 15, level: 'E', tag: '简单', distance: 0.1, image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' },
  { id: 14, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
   { id: 12, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
  // 其余数据照你原来的即可
]

const getBorderColor = (level: string) => {
  if (level === 'E') return 'border-emerald-400'
  if (level === 'S' || level === 'A') return 'border-red-500'
  return 'border-orange-400'
}

const getTextColor = (level: string) => {
  if (level === 'E') return 'text-emerald-600'
  if (level === 'S' || level === 'A') return 'text-red-600'
  return 'text-orange-500'
}

const getBadgeBg = (level: string) => {
  if (level === 'E') return 'bg-emerald-500'
  if (level === 'S' || level === 'A') return 'bg-red-500'
  return 'bg-orange-500'
}

const openDetail = (task: any) => {
  console.log('点击任务：', task.id)
}
</script>
