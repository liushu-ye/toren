<template>
  <div class="min-h-screen bg-[#ede8e8] py-8 px-4 font-sans text-gray-800 flex justify-center">
    
    <div class="w-full max-w-md">
      
      <section class="relative pl-6 pb-2">
        <div class="absolute left-[7px] top-2 bottom-0 w-[4px] bg-amber-400 rounded-full"></div>

        <h2 class="text-xl font-bold mb-6 ml-2 text-black">待办</h2>

        <div v-for="(group, gIndex) in todoList" :key="gIndex" class="relative mb-8">
          <div class="absolute -left-[23px] top-1 w-3.5 h-3.5 bg-[#ede8e8] border-2 border-gray-600 rounded-full z-10"></div>
          
          <div class="text-xs text-gray-600 font-medium mb-2 ml-1">{{ group.time }}</div>

          <div class="flex flex-col gap-4">
            <TaskCard 
              v-for="(item, iIndex) in group.items" 
              :key="iIndex" 
              :data="item" 
            />
          </div>
        </div>
      </section>

      <section class="relative pl-6">
        <div class="absolute left-[7px] top-2 bottom-0 w-[4px] bg-red-500 rounded-full"></div>

        <h2 class="text-xl font-bold mb-6 ml-2 text-black">历史</h2>

        <div v-for="(group, gIndex) in historyList" :key="gIndex" class="relative mb-8">
           <div class="absolute -left-[23px] top-1 w-3.5 h-3.5 bg-[#ede8e8] border-2 border-gray-600 rounded-full z-10"></div>
          
          <div class="text-xs text-gray-600 font-medium mb-2 ml-1">{{ group.time }}</div>

          <div class="flex flex-col gap-4">
            <TaskCard 
              v-for="(item, iIndex) in group.items" 
              :key="iIndex" 
              :data="item" 
            />
          </div>
        </div>
      </section>

    </div>
  </div>
</template>

<script setup lang="ts">
import { h, defineComponent, type PropType } from 'vue';

// --- 类型定义 ---

type CardType = 'task' | 'memo'; // 任务(发光) | 备忘录(普通)
type StatusType = 'income' | 'expense' | 'pending' | 'memo';

interface TaskItem {
  type: CardType;
  title: string;
  author?: string;
  location?: string;
  locationLabel?: string; // 比如 "线上"
  statusLabel?: string; // 比如 "备忘录", "未完成"
  amount?: string;      // 显示金额文本
  amountValue?: number; // 用于判断颜色逻辑
  xp?: number;
}

interface TimeGroup {
  time: string;
  items: TaskItem[];
}

// --- 子组件：TaskCard ---
// 这里直接写在同一个文件里方便复制，实际项目中建议拆分
const TaskCard = defineComponent({
  props: {
    data: {
      type: Object as PropType<TaskItem>,
      required: true
    }
  },
  setup(props) {
    const LocationIcon = () => h('svg', {
      xmlns: "http://www.w3.org/2000/svg", viewBox: "0 0 24 24", fill: "none", stroke: "currentColor",
      "stroke-width": "2", "stroke-linecap": "round", "stroke-linejoin": "round", class: "w-3.5 h-3.5 mr-1"
    }, [
      h('path', { d: "M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z" }),
      h('circle', { cx: "12", cy: "10", r: "3" })
    ]);

    return () => {
      const { data } = props;
      const isTask = data.type === 'task';

      // 动态样式类
      const containerClass = isTask
        ? "bg-[#e5e7eb] border border-black/60 rounded-lg p-1 shadow-[0_0_15px_rgba(74,222,128,0.4)] relative overflow-hidden group" // 任务: 绿色光晕
        : "bg-white border border-black rounded-sm shadow-sm relative overflow-hidden"; // 备忘录: 普通白底

      const innerClass = isTask
        ? "border border-black/30 rounded flex justify-between items-center p-3 bg-[#ebe7e7]" 
        : "p-3 flex justify-between items-center";
      
      // 金额颜色逻辑 (仿照图示：+为红，-为绿)
      let amountColorClass = "text-gray-500";
      if (data.amountValue && data.amountValue > 0) amountColorClass = "text-red-500";
      if (data.amountValue && data.amountValue < 0) amountColorClass = "text-[#22c55e]"; // Bright Green

      return h('div', { class: containerClass }, [
        // 只有 Task 类型有那层淡淡的绿色外框背景，这里模拟内部结构
        h('div', { class: innerClass }, [
          // 左侧内容
          h('div', { class: "flex flex-col gap-1" }, [
            h('h3', { class: "font-medium text-gray-900 text-sm leading-tight" }, data.title),
            h('div', { class: "text-xs text-slate-500 font-medium" }, data.author || ''),
            h('div', { class: "flex items-center text-xs text-black font-medium mt-0.5" }, [
              h(LocationIcon),
              h('span', data.locationLabel ? `${data.locationLabel} : ` : ''),
              h('span', data.location)
            ])
          ]),
          
          // 右侧内容
          h('div', { class: "flex flex-col items-end gap-1 min-w-[80px]" }, [
            // 金额或状态
            data.amount 
              ? h('div', { class: `text-sm font-bold ${amountColorClass}` }, data.amount) 
              : null,
            
            data.statusLabel 
              ? h('div', { class: "text-xs font-bold text-gray-600" }, data.statusLabel) 
              : null,

            // XP
            data.xp 
              ? h('div', { class: "text-xs text-black font-medium" }, `+ ${data.xp}XP`) 
              : null
          ])
        ])
      ]);
    };
  }
});

// --- 数据 ---

const todoList: TimeGroup[] = [
  {
    time: "上午 9:24",
    items: [
      {
        type: "task",
        title: "制作/售卖烤冷面",
        author: "全人官方",
        location: "开封大学门口歪口2号摊",
        amount: "¥ 60元",
        amountValue: 60,
        xp: 200
      }
    ]
  },
  {
    time: "", // 如果没有具体时间，可以为空，逻辑兼容
    items: [
       {
        type: "memo",
        title: "今天该交作业了",
        author: "朱邪墨染",
        location: "学习通",
        locationLabel: "线上",
        statusLabel: "备忘录",
      }
    ]
  }
];

const historyList: TimeGroup[] = [
  {
    time: "今天",
    items: [
      {
        type: "task",
        title: "制作/售卖烤冷面",
        author: "全人官方",
        location: "开封大学门口歪口2号摊",
        amount: "+60.00",
        amountValue: 60,
        xp: 200
      }
    ]
  },
  {
    time: "昨天",
    items: [
      {
        type: "task",
        title: "制作/售卖烤冷面",
        author: "全人官方",
        location: "开封大学门口歪口2号摊",
        amount: "-60.00",
        amountValue: -60,
        xp: 200
      },
      {
        type: "task",
        title: "制作/售卖烤冷面",
        author: "全人官方",
        location: "开封大学门口歪口2号摊",
        statusLabel: "未完成"
      }
    ]
  }
];

</script>

<style scoped>
/* 如果有特别复杂的阴影需要在这里微调，
   但目前 Tailwind 的 arbitary value 已经足够 */
</style>