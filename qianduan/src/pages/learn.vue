<script setup lang='ts'>

</script>

<template>
    <body>
    <div class="layout-container">
        <!-- 风格1：大众简约风格 -->
        <div class="style-title">风格1：大众简约风格</div>
        <div class="row">
            <div class="task-card card-long card-style-1 easy">
                <span class="difficulty-tag easy-tag">简单</span>
                <div class="task-title">校园快递分拣</div>
                <div class="task-meta">
                    <span>15元/小时</span>
                    <span>0.8km</span>
                </div>
            </div>
            <div class="task-card card-long card-style-1 medium">
                <span class="difficulty-tag medium-tag">中等</span>
                <div class="task-title">线上文案编辑</div>
                <div class="task-meta">
                    <span>30元/篇</span>
                    <span>远程</span>
                </div>
            </div>
        </div>
        <div class="task-card card-wide card-style-1 hard">
            <span class="difficulty-tag hard-tag">困难</span>
            <div class="task-title">活动现场摄影</div>
            <div class="task-meta">
                <span>200元/天</span>
                <span>3.2km</span>
            </div>
        </div>

        <!-- 风格2：大众渐变风格 -->
        <div class="style-title">风格2：大众渐变风格</div>
        <div class="row">
            <div class="task-card card-long card-style-2 easy">
                <span class="difficulty-tag easy-tag">简单</span>
                <div class="task-title">奶茶店店员</div>
                <div class="task-meta">
                    <span>18元/小时</span>
                    <span>1.5km</span>
                </div>
            </div>
            <div class="task-card card-long card-style-2 medium">
                <span class="difficulty-tag medium-tag">中等</span>
                <div class="task-title">家教辅导</div>
                <div class="task-meta">
                    <span>50元/小时</span>
                    <span>2.1km</span>
                </div>
            </div>
        </div>
        <div class="task-card card-wide card-style-2 hard">
            <span class="difficulty-tag hard-tag">困难</span>
            <div class="task-title">翻译兼职（日语）</div>
            <div class="task-meta">
                <span>150元/千字</span>
                <span>远程</span>
            </div>
        </div>

        <!-- 风格3：轻二次元风格（日系简约） -->
        <div class="style-title">风格3：轻二次元风格（日系简约）</div>
        <div class="row">
            <div class="task-card card-long card-style-3 easy">
                <span class="difficulty-tag easy-tag">简单</span>
                <div class="task-title">超市理货员</div>
                <div class="task-meta">
                    <span>16元/小时</span>
                    <span>1.2km</span>
                </div>
            </div>
            <div class="task-card card-long card-style-3 medium">
                <span class="difficulty-tag medium-tag">中等</span>
                <div class="task-title">短视频剪辑</div>
                <div class="task-meta">
                    <span>80元/条</span>
                    <span>远程</span>
                </div>
            </div>
        </div>
        <div class="task-card card-wide card-style-3 hard">
            <span class="difficulty-tag hard-tag">困难</span>
            <div class="task-title">UI设计兼职</div>
            <div class="task-meta">
                <span>500元/单</span>
                <span>远程</span>
            </div>
        </div>

        <!-- 风格4：轻二次元风格（萌系简约） -->
        <div class="style-title">风格4：轻二次元风格（萌系简约）</div>
        <div class="row">
            <div class="task-card card-long card-style-4 easy">
                <span class="difficulty-tag easy-tag">简单</span>
                <div class="task-title">餐厅服务员</div>
                <div class="task-meta">
                    <span>17元/小时</span>
                    <span>0.9km</span>
                </div>
            </div>
            <div class="task-card card-long card-style-4 medium">
                <span class="difficulty-tag medium-tag">中等</span>
                <div class="task-title">数据标注</div>
                <div class="task-meta">
                    <span>120元/天</span>
                    <span>远程</span>
                </div>
            </div>
        </div>
        <div class="task-card card-wide card-style-4 hard">
            <span class="difficulty-tag hard-tag">困难</span>
            <div class="task-title">游戏原画兼职</div>
            <div class="task-meta">
                <span>800元/张</span>
                <span>远程</span>
            </div>
        </div>
    </div>
</body>
</template>

<style scoped>
  /* 基础重置 */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: "Microsoft YaHei", sans-serif;
        }

        body {
            background-color: #1e1e1e;
            padding: 20px;
        }

        /* 容器样式 */
        .layout-container {
            max-width: 400px;
            margin: 0 auto;
            gap: 15px;
            display: flex;
            flex-direction: column;
        }

        /* 风格标题 */
        .style-title {
            margin: 30px 0 15px;
            font-size: 18px;
            color: #fff;
            font-weight: 600;
            border-left: 4px solid #666;
            padding-left: 8px;
        }

        /* 行容器 */
        .row {
            display: flex;
            gap: 15px;
            width: 100%;
        }

        /* 通用卡片样式 */
        .task-card {
            border-radius: 8px;
            padding: 12px 15px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            position: relative;
            overflow: hidden;
        }

        /* 上排卡片（长条形） */
        .card-long {
            width: 50%;
            height: 120px;
        }

        /* 下排卡片（宽条形） */
        .card-wide {
            width: 100%;
            height: 100px;
        }

        /* 难度标签通用样式 */
        .difficulty-tag {
            position: absolute;
            top: 8px;
            right: 8px;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 12px;
            color: white;
            font-weight: 500;
        }

        /* 任务信息样式 */
        .task-title {
            font-size: 16px;
            font-weight: 600;
            color: #222;
        }

        .task-meta {
            display: flex;
            justify-content: space-between;
            font-size: 14px;
            color: #555;
            flex-wrap: wrap;
            gap: 4px;
        }

        /* -------------------------- 风格1：大众简约风格 -------------------------- */
        .card-style-1 {
            background-color: white;
            border: 2px solid transparent;
            box-shadow: 0 2px 6px rgba(0,0,0,0.08);
            transition: all 0.2s;
        }
        /* 难度配色 - 简约风格 */
        .card-style-1.easy { border-color: #4CAF50; }
        .card-style-1.medium { border-color: #FF9800; }
        .card-style-1.hard { border-color: #F44336; }
        /* 难度标签配色 */
        .easy-tag { background-color: #4CAF50; }
        .medium-tag { background-color: #FF9800; }
        .hard-tag { background-color: #F44336; }

        /* -------------------------- 风格2：大众渐变风格 -------------------------- */
        .card-style-2 {
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
            transition: all 0.2s;
        }
        /* 渐变风格难度边框 */
        .card-style-2.easy { 
            background: linear-gradient(135deg, #f0fdf4 0%, #e8f5e9 100%);
            border: 1px solid #4CAF50;
        }
        .card-style-2.medium { 
            background: linear-gradient(135deg, #fff8e1 0%, #fff3e0 100%);
            border: 1px solid #FF9800;
        }
        .card-style-2.hard { 
            background: linear-gradient(135deg, #ffebee 0%, #fce4ec 100%);
            border: 1px solid #F44336;
        }

        /* -------------------------- 风格3：轻二次元风格（日系简约） -------------------------- */
        .card-style-3 {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            border: 1px solid #eee;
            position: relative;
        }
        /* 二次元风格难度装饰 */
        .card-style-3::before {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            width: 4px;
            height: 100%;
        }
        .card-style-3.easy::before { background-color: #4CAF50; }
        .card-style-3.medium::before { background-color: #FF9800; }
        .card-style-3.hard::before { background-color: #F44336; }
        /* 二次元轻微装饰 */
        .card-style-3 .task-title {
            font-family: "SimHei", "Microsoft YaHei", sans-serif;
            color: #333;
        }
        .card-style-3::after {
            content: "✦";
            position: absolute;
            bottom: 8px;
            right: 8px;
            font-size: 10px;
            opacity: 0.3;
        }

        /* -------------------------- 风格4：轻二次元风格（萌系简约） -------------------------- */
        .card-style-4 {
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.05);
            border: 1px solid #f0f0f0;
        }
        /* 萌系难度配色 */
        .card-style-4.easy { 
            border: 2px solid #81C784;
            background: #f9fffa;
        }
        .card-style-4.medium { 
            border: 2px solid #FFB74D;
            background: #fffbf2;
        }
        .card-style-4.hard { 
            border: 2px solid #E57373;
            background: #fff5f5;
        }
        /* 萌系小装饰 */
        .card-style-4 .difficulty-tag {
            border-radius: 0 12px 0 12px;
            font-size: 11px;
            font-weight: bold;
        }
        .card-style-4 .task-title::after {
            content: "✨";
            font-size: 12px;
            margin-left: 4px;
            opacity: 0.6;
        }
</style>
