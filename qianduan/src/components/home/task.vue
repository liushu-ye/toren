<script setup lang='ts'>
/**
 * ===============================
 * 任务列表组件
 * ===============================
 * 功能：展示任务列表，包含大卡和小卡的混合布局
 * 布局：每8个小卡后显示1个大卡
 * 作者：系统生成
 * 日期：2026-02-12
 */

// 导入卡片组件
import TaskBigCard from '@/components/home/LargeCard.vue' // 大卡组件
import TaskSmallCard from '@/components/home/SmallCard.vue' // 小卡组件

/**
 * ===============================
 * 常量定义
 * ===============================
 */

// 每组卡片配置：8个小卡 + 1个大卡
const SMALL_COUNT = 8

/**
 * ===============================
 * 工具函数
 * ===============================
 */

/**
 * 判断是否应该显示大卡
 * @param index 当前任务的索引（从0开始）
 * @returns boolean - 是否显示大卡
 */
const isBigCard = (index: number) => {
  // index 从 0 开始，所以 +1 转换为从1开始的计数
  return (index + 1) % (SMALL_COUNT + 1) === 0
}

/**
 * 根据任务等级获取边框颜色
 * @param level 任务等级（E/S/A/B/C等）
 * @returns string - Tailwind CSS边框颜色类名
 */
const getBorderColor = (level: string) => {
  if (level === 'E') return 'border-emerald-400' // E级：浅绿色边框
  if (level === 'S' || level === 'A') return 'border-red-500' // S/A级：红色边框
  return 'border-orange-400' // 其他等级：橙色边框
}

/**
 * 根据任务等级获取文字颜色
 * @param level 任务等级（E/S/A/B/C等）
 * @returns string - Tailwind CSS文字颜色类名
 */
const getTextColor = (level: string) => {
  if (level === 'E') return 'text-emerald-600' // E级：深绿色文字
  if (level === 'S' || level === 'A') return 'text-red-600' // S/A级：深红色文字
  return 'text-orange-500' // 其他等级：橙色文字
}

/**
 * 根据任务等级获取徽章背景颜色
 * @param level 任务等级（E/S/A/B/C等）
 * @returns string - Tailwind CSS背景颜色类名
 */
const getBadgeBg = (level: string) => {
  if (level === 'E') return 'bg-emerald-500' // E级：绿色徽章背景
  if (level === 'S' || level === 'A') return 'bg-red-500' // S/A级：红色徽章背景
  return 'bg-orange-500' // 其他等级：橙色徽章背景
}

/**
 * 打开任务详情
 * @param task 任务对象
 */
const openDetail = (task: any) => {
  console.log('点击任务：', task.id)
  // 这里可以添加跳转到任务详情页的逻辑
}

/**
 * ===============================
 * 任务数据
 * ===============================
 * 数据结构说明：
 * id: 任务ID
 * title: 任务标题
 * desc: 任务描述
 * wage: 薪资
 * unit: 薪资单位（时/篇等）
 * stamina: 体力消耗
 * level: 任务等级
 * tag: 任务标签
 * distance: 距离（公里）
 * image: 任务图片URL
 */
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
  { 
    id: 2, 
    title: '食堂餐盘回收', 
    desc: '饭点高峰期协助', 
    wage: 23, 
    unit: '时', 
    stamina: 15, 
    level: 'E', 
    tag: '简单', 
    distance: 0.1, 
    image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 3, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 4, 
    title: '图书馆闭馆整理', 
    desc: '将归还书籍上架', 
    wage: 24, 
    unit: '时', 
    stamina: 20, 
    level: 'E', 
    tag: '简单', 
    distance: 0.5, 
    image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 5, 
    title: '线上文案编辑', 
    desc: '小红书风格，远程结算', 
    wage: 30, 
    unit: '篇', 
    stamina: 10, 
    level: 'C', 
    tag: '中等', 
    distance: 0.0, 
    image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 6, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 7, 
    title: '食堂餐盘回收', 
    desc: '饭点高峰期协助', 
    wage: 23, 
    unit: '时', 
    stamina: 15, 
    level: 'E', 
    tag: '简单', 
    distance: 0.1, 
    image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 8, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 9, 
    title: '食堂餐盘回收', 
    desc: '饭点高峰期协助', 
    wage: 23, 
    unit: '时', 
    stamina: 15, 
    level: 'E', 
    tag: '简单', 
    distance: 0.1, 
    image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 10, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 11, 
    title: '食堂餐盘回收', 
    desc: '饭点高峰期协助', 
    wage: 23, 
    unit: '时', 
    stamina: 15, 
    level: 'E', 
    tag: '简单', 
    distance: 0.1, 
    image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 12, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 13, 
    title: '食堂餐盘回收', 
    desc: '饭点高峰期协助', 
    wage: 23, 
    unit: '时', 
    stamina: 15, 
    level: 'E', 
    tag: '简单', 
    distance: 0.1, 
    image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 14, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 15, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 16, 
    title: '食堂餐盘回收', 
    desc: '饭点高峰期协助', 
    wage: 23, 
    unit: '时', 
    stamina: 15, 
    level: 'E', 
    tag: '简单', 
    distance: 0.1, 
    image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 17, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  { 
    id: 18, 
    title: '【品牌】瑞幸咖啡师学徒', 
    desc: '需持有健康证，长期优先，提供专业培训与认证', 
    wage: 28, 
    unit: '时', 
    stamina: 30, 
    level: 'B', 
    tag: '技能', 
    distance: 1.5, 
    image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' 
  },
  // 其余数据照你原来的即可
]
</script>

<template>
  <!-- 任务网格布局 -->
  <div class="task-grid">
    <!-- 遍历任务列表 -->
    <template
      v-for="(task, index) in taskList"
      :key="task.id"
    >
      <!-- 每9个位置插入一个大卡（8小 + 1大） -->
      <TaskBigCard
        v-if="isBigCard(index)"
        :task="task"
        :border-color="getBorderColor(task.level)"
        :text-color="getTextColor(task.level)"
        :badge-bg="getBadgeBg(task.level)"
        @click="openDetail(task)"
      />

      <!-- 其他位置显示小卡 -->
      <TaskSmallCard
        v-else
        :task="task"
        :border-color="getBorderColor(task.level)"
        :text-color="getTextColor(task.level)"
        @click="openDetail(task)"
      />
    </template>
  </div>

  <!-- 底部提示信息 -->
  <div class="task-footer">
    —— 到底了 冒险者 ——
  </div>
</template>

<style scoped>
/* 组件样式 */
/* 注：主要样式已在全局样式文件中定义，这里可以添加组件特定的样式 */
</style>
