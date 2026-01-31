<template>
  <!-- 横向大卡 -->
  <div
    class="task-card task-big"
    :class="borderColor"
    @click="emitClick"
  >
    <!-- 左侧图片 -->
    <div class="task-big-image">
      <img :src="task.image" class="w-full h-full object-cover" />
      <div class="task-big-gradient"></div>

      <div class="task-big-tag" :class="badgeBg">
        {{ task.tag }}
      </div>
    </div>

    <!-- 右侧内容 -->
    <div class="task-big-content">
      <div class="task-big-level-bg">
        {{ task.level }}
      </div>

      <div>
        <h3 class="font-bold text-base leading-normal line-clamp-2">
          {{ task.title }}
        </h3>
        <p class="text-[10px] text-slate-400 mt-1.5 line-clamp-2">
          {{ task.desc }}
        </p>
      </div>

      <div class="flex justify-between items-end">
        <div>
          <span class="text-lg font-black" :class="textColor">
            ¥{{ task.wage }}
          </span>
          <span class="text-[10px] text-slate-400 ml-1">
            /{{ task.unit }}
          </span>
        </div>

        <span class="text-xs font-bold text-slate-600 bg-slate-100 px-2 py-0.5 rounded-full">
          ⚡{{ task.stamina }}
        </span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
/**
 * 横向大卡组件
 */

const props = defineProps<{
  task: any
  borderColor: string
  textColor: string
  badgeBg: string
}>()

const emit = defineEmits<{
  (e: 'click', task: any): void
}>()

const emitClick = () => {
  emit('click', props.task)
}
</script>
