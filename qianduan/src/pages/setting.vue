<template>
  <div class="min-h-screen bg-[#f8f9fa] text-slate-800 font-sans pb-24">
    <main class="px-4 mt-4">
      <div class="grid grid-cols-2 gap-4"> <!-- 优化间距更舒适 -->
        <template v-for="(task, index) in taskList" :key="task.id">

          <!-- 横向大卡（克制型）- 优化hover动效、阴影、过渡 -->
          <div
            v-if="(index + 1) % 3 === 0"
            class="col-span-2 flex bg-white rounded-xl overflow-hidden shadow-md hover:shadow-lg border-[2px] h-40 transition-all duration-300 hover:-translate-y-1 cursor-pointer"
            :class="getBorderColor(task.level)"
            @click="openDetail(task)"
          >
            <!-- Image - 优化渐变自然度 -->
            <div class="relative h-full shrink-0" style="width:48%">
              <img :src="task.image" class="w-full h-full object-cover" />
              <div class="absolute inset-y-0 right-0 w-24 bg-gradient-to-r from-transparent via-white/30 to-white"></div>
              <div class="absolute top-0 left-0 text-[10px] font-bold text-white px-2 py-1 rounded-br-lg shadow-sm"
                   :class="getBadgeBg(task.level)">
                {{ task.tag }}
              </div>
            </div>

            <!-- Text - 优化行高和间距 -->
            <div class="flex-1 pl-3 pr-4 py-3 flex flex-col justify-between relative">
              <div class="absolute right-0 top-0 text-[56px] opacity-[0.02] font-black">
                {{ task.level }}
              </div>

              <div>
                <h3 class="font-bold text-base leading-normal line-clamp-2">
                  {{ task.title }}
                </h3>
                <p class="text-[10px] text-slate-400 mt-1.5 line-clamp-2 leading-relaxed">
                  {{ task.desc }}
                </p>
              </div>

              <div class="flex items-end justify-between">
                <div>
                  <span class="text-lg font-black" :class="getTextColor(task.level)">
                    ¥{{ task.wage }}
                  </span>
                  <span class="text-[10px] text-slate-400 ml-1">/{{ task.unit }}</span>
                </div>
                <span class="text-xs font-bold text-slate-600 bg-slate-100 px-2 py-0.5 rounded-full">⚡{{ task.stamina }}</span>
              </div>
            </div>
          </div>

          <!-- 竖向小卡（强化型）- 优化hover动效、阴影、内边距 -->
          <div
            v-else
            class="bg-white rounded-xl overflow-hidden shadow-md hover:shadow-lg border-[2px] flex flex-col transition-all duration-300 hover:-translate-y-1 cursor-pointer"
            :class="getBorderColor(task.level)"
            @click="openDetail(task)"
          >
            <!-- Image - 优化渐变范围和透明度 -->
            <div class="relative aspect-[4/3]">
              <img :src="task.image" class="w-full h-full object-cover" />
              <div class="absolute inset-x-0 bottom-0 h-2/5 bg-gradient-to-t from-white via-white/60 to-transparent"></div>
              <div class="absolute top-2 right-2 text-[9px] font-black bg-white/95 px-1.5 py-0.5 rounded shadow-sm"
                   :class="getTextColor(task.level)">
                RANK {{ task.level }}
              </div>
            </div>

            <!-- Text - 优化内边距和行高 -->
            <div class="-mt-5 px-3 pt-1 pb-3.5 flex flex-col justify-between flex-1 relative z-10">
              <div>
                <h3 class="font-bold text-base leading-tight line-clamp-2 min-h-[2.4em]">
                  {{ task.title }}
                </h3>
                <div class="mt-1 flex gap-1.5"> <!-- 优化标签间距 -->
                  <span class="text-[9px] text-slate-400 bg-slate-100 px-1.5 py-0.5 rounded">
                    {{ task.distance }}km
                  </span>
                  <span class="text-[9px] text-slate-400 bg-slate-100 px-1.5 py-0.5 rounded">
                    日结
                  </span>
                </div>
              </div>

              <div class="flex justify-between items-center mt-3">
                <span class="font-black text-lg" :class="getTextColor(task.level)">
                  ¥{{ task.wage }}
                </span>
                <span class="text-[10px] text-slate-400 font-bold bg-slate-100 px-1.5 py-0.5 rounded-full">
                  ⚡{{ task.stamina }}
                </span>
              </div>
            </div>
          </div>

        </template>
      </div>

      <!-- 优化底部提示文字样式 -->
      <div class="text-center mt-10 mb-4 text-slate-300 text-xs tracking-wider py-2">
        —— 到底了 冒险者 ——
      </div>
    </main>
  </div>
</template>

<script setup lang="ts">
/**
 * 视觉配置：
 * 1. 统一图片比例：小卡片 4:3，大卡片左侧区域撑满。
 * 2. 颜色逻辑：
 * E (Green) = 简单/安全
 * C/B (Orange) = 中等/标准
 * A/S (Red) = 困难/挑战/高收益
 */

const taskList = [
  { id: 1, title: '菜鸟驿站快递分拣', desc: '轻松简单，室内作业，无体能要求', wage: 25, unit: '时', stamina: 20, level: 'E', tag: '简单', distance: 0.3, image: 'https://images.unsplash.com/photo-1566576912321-d58ddd7a6047?auto=format&fit=crop&w=400&q=80' },
  { id: 2, title: '食堂餐盘回收', desc: '饭点高峰期协助', wage: 23, unit: '时', stamina: 15, level: 'E', tag: '简单', distance: 0.1, image: 'https://images.unsplash.com/photo-1576867757603-05b134ebc379?auto=format&fit=crop&w=400&q=80' },
  { id: 3, title: '【品牌】瑞幸咖啡师学徒', desc: '需持有健康证，长期优先，提供专业培训与认证', wage: 28, unit: '时', stamina: 30, level: 'B', tag: '技能', distance: 1.5, image: 'https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=400&q=80' },
  { id: 4, title: '图书馆闭馆整理', desc: '将归还书籍上架', wage: 24, unit: '时', stamina: 20, level: 'E', tag: '简单', distance: 0.5, image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=400&q=80' },
  { id: 5, title: '线上文案编辑', desc: '小红书风格，远程结算', wage: 30, unit: '篇', stamina: 10, level: 'C', tag: '中等', distance: 0.0, image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=400&q=80' },
  { id: 6, title: '【S级悬赏】漫展现场机动安保', desc: '维持现场秩序，包午餐，需连续站立工作，报酬极其丰厚', wage: 200, unit: '天', stamina: 80, level: 'S', tag: '高薪', distance: 3.2, image: 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=400&q=80' },
];

const getBorderColor = (level: string) => {
  if (level === 'E') return 'border-emerald-400';
  if (level === 'S' || level === 'A') return 'border-red-500';
  return 'border-orange-400';
};

const getTextColor = (level: string) => {
  if (level === 'E') return 'text-emerald-600';
  if (level === 'S' || level === 'A') return 'text-red-600';
  return 'text-orange-500';
};

const getBadgeBg = (level: string) => {
  if (level === 'E') return 'bg-emerald-500';
  if (level === 'S' || level === 'A') return 'bg-red-500';
  return 'bg-orange-500';
};

const openDetail = (task: any) => {
  console.log('Task Clicked:', task.id);
};
</script>