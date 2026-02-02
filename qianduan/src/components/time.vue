

<script setup lang="ts">
import { computed } from 'vue'

/**
 * 单个分段的最小数据结构
 */
export interface Segment {
  color: string
  startAngle: number
  endAngle: number
}

const props = withDefaults(
  defineProps<{
    size?: number
    strokeWidth?: number
    gapAngle?: number
    segments: Segment[]
  }>(),
  {
    size: 200,
    strokeWidth: 16,
    gapAngle: 2,
  }
)

const center = computed(() => props.size / 2)
const radius = computed(() => props.size / 2 - props.strokeWidth)

/**
 * 极坐标转 SVG 路径
 */
function polarToCartesian(cx: number, cy: number, r: number, angle: number) {
  const rad = ((angle - 90) * Math.PI) / 180
  return {
    x: cx + r * Math.cos(rad),
    y: cy + r * Math.sin(rad),
  }
}

function describeArc(
  cx: number,
  cy: number,
  r: number,
  startAngle: number,
  endAngle: number
) {
  if (endAngle <= startAngle) return ''

  const start = polarToCartesian(cx, cy, r, endAngle)
  const end = polarToCartesian(cx, cy, r, startAngle)

  const largeArcFlag = endAngle - startAngle <= 180 ? '0' : '1'

  return [
    'M', start.x, start.y,
    'A', r, r, 0, largeArcFlag, 0, end.x, end.y,
  ].join(' ')
}
</script>
<template>
  <svg
    :width="size"
    :height="size"
    :viewBox="`0 0 ${size} ${size}`"
  >
    <g :transform="`translate(${center}, ${center})`">
      <path
        v-for="(seg, index) in segments"
        :key="index"
        :d="describeArc(0, 0, radius, seg.startAngle + gapAngle / 2, seg.endAngle - gapAngle / 2)"
        :stroke="seg.color"
        :stroke-width="strokeWidth"
        fill="none"
        stroke-linecap="butt"
      />
    </g>
  </svg>
</template>

<style scoped>

</style>
