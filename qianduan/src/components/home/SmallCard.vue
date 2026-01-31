<template>
  <!-- 竖向小卡 -->
  <div
    class="task-card task-small"
    :class="borderColor"
    @click="emitClick"
  >
    <!-- 图片区域 -->
    <div class="task-small-image">
      <img :src="task.image" class="w-full h-full object-cover" />

      <!-- 底部渐变 -->
      <div class="task-small-gradient"></div>

      <!-- 右上角等级 -->
      <div class="task-small-rank" :class="textColor">
        RANK {{ task.level }}
      </div>
    </div>

    <!-- 文本内容 -->
    <div class="task-small-content">
      <div>
        <h3 class="font-bold text-base leading-tight line-clamp-2 min-h-[2.4em]">
          {{ task.title }}
        </h3>

        <div class="mt-1 flex gap-1.5">
          <span class="text-[9px] text-slate-400 bg-slate-100 px-1.5 py-0.5 rounded">
            {{ task.distance }}km
          </span>
          <span class="text-[9px] text-slate-400 bg-slate-100 px-1.5 py-0.5 rounded">
            日结
          </span>
        </div>
      </div>

      <div class="flex justify-between items-center mt-3">
        <span class="font-black text-lg" :class="textColor">
          ¥{{ task.wage }}
        </span>
        <span class="text-[10px] text-slate-400 font-bold bg-slate-100 px-1.5 py-0.5 rounded-full">
          ⚡{{ task.stamina }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
/**
 * 竖向小卡组件
 */

const props = defineProps<{
  task: any
  borderColor: string
  textColor: string
}>()

const emit = defineEmits<{
  (e: 'click', task: any): void
}>()

const emitClick = () => {
  emit('click', props.task)
}
</script>
