<script lang='ts'>
import type { Segment } from './time.vue'

/**
 * 生成等分角度的基础 segments（不含颜色语义）
 */
export function buildBaseSegments(
  count: number
): Omit<Segment, 'color'>[] {
  const step = 360 / count
  return Array.from({ length: count }, (_, i) => ({
    startAngle: i * step,
    endAngle: (i + 1) * step,
  }))
}

/**
 * 时间环：24 等分
 * - pastUntil: 已过去的小时（0~24）
 * - highlightRanges: 标记区间（如专注 / 风险时段）
 */
export function buildTimeSegments(options: {
  pastUntil: number
  highlightRanges?: { start: number; end: number; color: string }[]
}) {
  const base = buildBaseSegments(24)

  return base.map((seg, index) => {
    // 已过去时间
    if (index < options.pastUntil) {
      return { ...seg, color: '#d1d5db' }
    }

    // 标记区间（黄 / 红 / 蓝等）
    const hit = options.highlightRanges?.find(
      r => index >= r.start && index < r.end
    )

    if (hit) {
      return { ...seg, color: hit.color }
    }

    // 默认可用时间
    return { ...seg, color: '#4ade80' }
  })
}

/**
 * 进度 / 经验环：25 等分（2% 一格）
 * - percent: 当前进度 0~100
 */
export function buildProgressSegments(percent: number) {
  const base = buildBaseSegments(25)
  const filledCount = Math.round((percent / 100) * 25)

  return base.map((seg, index) => ({
    ...seg,
    color: index < filledCount ? '#4ade80' : '#1f2937',
  }))
}

</script>

<template>
</template>

<style scoped>

</style>
