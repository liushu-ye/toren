<template>
  <div class="task-page">
    顶部导航
    <main class="task-main">
      <!-- 筛选 -->
      <nav class="task-filter-container">
        <div class="task-filter">
          <router-link class="task-filter-item" to="/official">官方</router-link>
          <router-link class="task-filter-item" to="/day">每日</router-link>
          <router-link class="task-filter-item" to="/adventure">冒险</router-link>
          <router-link class="task-filter-item" to="/bounty">悬赏</router-link>
          <router-link class="task-filter-item" to="/activity">活动</router-link>
          
        </div>
      </nav>
      
      

      <!-- 路由出口 -->
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup lang="ts">

</script>
