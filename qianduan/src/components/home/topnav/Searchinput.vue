<script setup lang="ts">
import { computed } from 'vue'

/**
 * ================================
 * 一、Props 定义
 * ================================
 * 这个组件只关心「输入框本身」
 */
const props = withDefaults(defineProps<{
  modelValue?: string        // v-model 绑定的值
  placeholder?: string       // 占位文字
  disabled?: boolean         // 是否禁用
}>(), {
  modelValue: '',
  placeholder: '搜索...',
  disabled: false,
})

/**
 * ================================
 * 二、事件定义
 * ================================
 * update:modelValue：标准 v-model
 * search：点击搜索 / 回车时触发
 * clear：点击清空按钮时触发
 */
const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
  (e: 'search', value: string): void
  (e: 'clear'): void
}>()

/**
 * ================================
 * 三、输入处理
 * ================================
 */
const onInput = (e: Event) => {
  const value = (e.target as HTMLInputElement).value
  emit('update:modelValue', value)
}

/**
 * 回车搜索
 */
const onEnter = () => {
  emit('search', props.modelValue)
}

/**
 * 清空输入
 */
const onClear = () => {
  emit('update:modelValue', '')
  emit('clear')
}

/**
 * ================================
 * 四、样式类（统一集中）
 * ================================
 */
const inputClass = computed(() => [
  'w-35 pl-9 pr-9 py-1',
  'rounded-lg border border-slate-300',
  'bg-white text-slate-800',
  'placeholder:text-slate-400',
  'focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
  'disabled:bg-slate-100 disabled:cursor-not-allowed',
])
</script>

<template>
  <div class="relative  flex-1">

    <span
      class="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 pointer-events-none"
    >
      <img src="@/assets/icons/search.svg" alt="">
    </span>
    

    <!-- 输入框 -->
    <input
      type="text"
      :value="modelValue"
      :placeholder="placeholder"
      :disabled="disabled"
      :class="inputClass"
      @input="onInput"
      @keyup.enter="onEnter"
    />

    <!-- =========================
         右侧清空按钮
         ========================= -->
    <button
      v-if="modelValue"
      type="button"
      class="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
      @click="onClear"
    >
      ❌
      <!--
        同样，这里可以换成你自己的本地图标
      -->
    </button>
  </div>
</template>
