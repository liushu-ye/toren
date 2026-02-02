<script setup lang='ts'>

</script>

<template>
    <div class="hand-drawn">
        测试一下
        这是一个手绘效果的div
    </div>
<svg style="position: absolute; width: 0; height: 0;">
    <filter id="pencil-border">
        <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="3" result="noise" />
        <feDisplacementMap in="SourceGraphic" in2="noise" scale="3" />
    </filter>
</svg>

</template>

<style scoped>
.hand-drawn {
    width: 200px;
    height: 200px;
    margin: 0 auto;
    background-color: #f0f0f0;
    border: 2px solid #333;     /* 粗细不均感的基础 */
 filter: url(#pencil-border);    /* 直接引用 App.vue 里的 ID */
 border-radius: 8px;     /* 配合滤镜效果更佳 */
}
</style>