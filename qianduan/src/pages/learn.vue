<template>
  <div class="min-h-screen bg-[#f0fdf4] flex justify-center items-center py-4 font-sans text-gray-800">
    <div class="w-full max-w-[400px] bg-white border-4 border-[#86efac] rounded-xl shadow-[0_0_20px_rgba(134,239,172,0.6)] relative overflow-hidden pb-20">
      
      <div class="p-4 border-b border-gray-200 relative">
        <div class="flex justify-between items-start">
          <div>
            <h1 class="text-2xl font-bold text-[#d97777]">制作/售卖烤冷面</h1>
            <div class="flex items-center mt-2 text-sm">
              <ClockIcon class="w-4 h-4 mr-1" />
              <span>耗时：4小时</span>
            </div>
            <div class="flex items-center mt-1 text-sm">
              <GiftIcon class="w-4 h-4 mr-1" />
              <span>奖励：金币、经验</span>
            </div>
            <div class="mt-1 text-sm text-gray-600">具体规则如下</div>
          </div>
          
          <div class="absolute top-0 right-0 bg-[#e08e8e] text-white px-3 py-1 rounded-bl-xl font-bold shadow-sm">
            官方
          </div>

          <div class="flex flex-col gap-3 mt-8">
            <button class="hover:text-yellow-500 transition"><StarIcon class="w-6 h-6" /></button>
            <button class="hover:text-blue-500 transition"><ShareIcon class="w-6 h-6" /></button>
          </div>
        </div>
      </div>

      <div class="px-4 py-3 flex gap-2 flex-wrap">
        <span class="px-3 py-1 border border-black rounded-full text-xs font-medium">仅线上结算</span>
        <span class="px-3 py-1 border border-black rounded-full text-xs font-medium">官方</span>
        <span class="px-3 py-1 border border-black rounded-full text-xs font-medium">底薪+提成</span>
      </div>

      <div class="mx-4 mb-3 border border-black rounded-lg p-3">
        <div class="flex items-center gap-1 mb-1 font-medium">
          <MapPinIcon class="w-4 h-4" />
          <span>距离：100m</span>
        </div>
        <div class="text-sm">任务地点：开封大学门口歪口2号摊</div>
      </div>

      <div class="mx-4 mb-3 border border-black rounded-lg p-3">
        <h3 class="font-bold mb-2">技能需求</h3>
        <div class="flex gap-4 text-sm font-medium">
          <span>健康证</span>
          <span>烤冷面0级</span>
        </div>
      </div>

      <div class="mx-4 mb-3 border border-black rounded-lg p-3">
        <h3 class="font-bold mb-2">任务内容</h3>
        <p class="text-sm font-medium mb-4">在学校门口的摊位制作并售卖烤冷面</p>
        <p class="text-sm text-gray-600 mb-4">会有有人接待</p>
        
        <p class="font-bold mb-2 text-sm">奖励会根据如下两种方式取最高值结算</p>
        
        <div class="bg-[#1a1a1a] text-white text-[10px] rounded p-2 overflow-hidden">
          <table class="w-full text-left border-collapse">
            <thead>
              <tr class="border-b border-gray-700">
                <th class="p-1 w-1/5">要素</th>
                <th class="p-1 w-2/5">官方摊位 (我司)</th>
                <th class="p-1 w-2/5">入驻摊位 (第三方)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-700">
              <tr>
                <td class="p-1 font-bold">计算基础</td>
                <td class="p-1">利润额</td>
                <td class="p-1">销售额</td>
              </tr>
              <tr>
                <td class="p-1 font-bold">模式一<br><span class="scale-90 inline-block text-gray-400">(保障型)</span></td>
                <td class="p-1">底薪 + 利润的 30%<br><span class="text-gray-400 scale-90 inline-block">* (底薪建议: 22元/4小时任务) *</span></td>
                <td class="p-1">底薪 + 销售额的 8%<br><span class="text-gray-400 scale-90 inline-block">* (底薪建议: 20元/4小时任务) *</span></td>
              </tr>
              <tr>
                <td class="p-1 font-bold">模式二<br><span class="scale-90 inline-block">(激进型)</span></td>
                <td class="p-1">利润的 50%</td>
                <td class="p-1">销售额的 15%</td>
              </tr>
              <tr>
                <td class="p-1 font-bold">结算逻辑</td>
                <td class="p-1" colspan="2">系统自动计算两种模式，<span class="text-yellow-400 font-bold">取较高值发放</span>。</td>
              </tr>
              <tr>
                <td class="p-1 font-bold">平台攻略</td>
                <td class="p-1">高回报，强吸引<br><span class="text-gray-400 scale-90">让优秀兼职者沉淀在官方体系。</span></td>
                <td class="p-1">易结算，广兼容<br><span class="text-gray-400 scale-90">降低入驻摊主的理解和计算门槛。</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <div class="mx-4 mb-6 border border-black rounded-lg p-3">
        <h3 class="font-bold mb-3">任务发布方</h3>
        <div class="flex items-center gap-6">
          <div class="flex items-center gap-2">
            <div class="w-8 h-8 border border-red-400 rounded-sm flex items-center justify-center p-1">
               <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="text-red-400 w-full h-full"><path d="M12 2L2 22h20L12 2z"/></svg>
            </div>
            <span class="font-bold text-sm">全人官方</span>
          </div>
          <div class="flex items-center gap-2">
            <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix" alt="avatar" class="w-8 h-8 rounded bg-gray-200" />
            <span class="font-bold text-sm">朱邪墨染</span>
          </div>
        </div>
      </div>

      <div class="absolute bottom-6 left-0 right-0 flex justify-center">
        <button class="bg-[#4ade80] hover:bg-[#22c55e] text-black font-bold text-xl py-3 px-12 rounded-lg border-2 border-black shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] active:translate-y-1 active:shadow-none transition-all">
          接取
        </button>
      </div>

    </div>
  </div>
</template>

<script setup lang="ts">
/**
 * 组件逻辑部分
 * 此处仅为纯UI演示，未包含具体交互逻辑
 */

// 简单的 SVG 图标组件封装
import { h, type FunctionalComponent, type SVGAttributes } from 'vue';

const createIcon = (d: string): FunctionalComponent<SVGAttributes> => {
  return (props) => h('svg', {
    xmlns: "http://www.w3.org/2000/svg",
    viewBox: "0 0 24 24",
    fill: "none",
    stroke: "currentColor",
    "stroke-width": "2",
    "stroke-linecap": "round",
    "stroke-linejoin": "round",
    ...props
  }, [h('path', { d })]);
};

// 图标定义 (避免引入第三方库，方便复制运行)
const ClockIcon = createIcon("M12 6v6l4 2 M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z");
const GiftIcon = createIcon("M20 12v10H4V12 M2 7h20v5H2z M12 22V7 M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z");
const StarIcon = createIcon("m12 2 3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z");
const ShareIcon = createIcon("M4 12v8a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-8 M16 6l-4-4-4 4 M12 2v13");
const MapPinIcon = createIcon("M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z M12 10a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z");
</script>

<style scoped>
/* 可以在这里添加特定的覆盖样式，但大部分已由 Tailwind 完成 */
</style>