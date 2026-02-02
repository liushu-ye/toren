<template>
  <SegmentRing
    :segments="segments"
    :size="240"
    :stroke-width="18"
    :gap-angle="2"
  />
</template>

<script setup lang="ts">
import SegmentRing from '@/components/time.vue'
import { buildTimeSegments } from '@/components/utils.vue'

// 假设现在是下午 3 点
const segments = buildTimeSegments({
  pastUntil: 15,
  highlightRanges: [
    { start: 18, end: 22, color: '#f59e0b' }, // 黄
    { start: 22, end: 24, color: '#ef4444' }, // 红
  ],
})
</script>
