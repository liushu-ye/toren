# 样式文件组织指南

## 📂 当前结构

```
src/assets/styles/
├── tailwind.css              # 主入口文件
├── theme/                   # 主题系统
│   ├── base.css             # 基础变量和CSS变量
│   ├── colors.css           # 颜色系统
│   ├── typography.css       # 字体系统
│   └── spacing.css          # 间距系统
├── components/              # 组件样式
│   ├── rail.css             # 轨道组件样式
│   ├── buttons.css          # 按钮组件
│   ├── forms.css            # 表单组件
│   └── navigation.css       # 导航组件
├── features/               # 功能样式
│   ├── animations.css       # 动画效果
│   ├── transitions.css      # 过渡效果
│   └── responsive.css      # 响应式工具
├── pages/                 # 页面样式
│   ├── home.css            # 首页
│   ├── login.css           # 登录页
│   └── public.css          # 公共页
├── utilities/             # 工具类
│   ├── common.css          # 通用工具
│   └── layout.css         # 布局工具
└── readme-style-organization.md
```

## 🚀 使用方法

### 添加新样式文件

1. **主题相关**：在 `theme/` 文件夹中创建
   - 颜色变量 → `colors.css`
   - 字体变量 → `typography.css`
   - 间距变量 → `spacing.css`

2. **组件相关**：在 `components/` 文件夹中创建
   - 按钮样式 → `buttons.css`
   - 表单样式 → `forms.css`
   - 导航样式 → `navigation.css`
   - 其他组件 → 按组件名创建

3. **功能相关**：在 `features/` 文件夹中创建
   - 动画效果 → `animations.css`
   - 过渡效果 → `transitions.css`
   - 响应式 → `responsive.css`

4. **页面相关**：在 `pages/` 文件夹中创建
   - 按页面名创建对应的CSS文件

5. **工具类**：在 `utilities/` 文件夹中创建
   - 通用工具 → `common.css`
   - 布局工具 → `layout.css`

### 更新主入口文件

在 `tailwind.css` 中添加新文件的引用：

```css
@import "tailwindcss";

/* 主题系统 */
@import "./theme/base.css";
@import "./theme/colors.css";
@import "./theme/typography.css";
@import "./theme/spacing.css";

/* 组件样式 */
@import "./components/rail.css";
@import "./components/buttons.css";
@import "./components/forms.css";
@import "./components/navigation.css";

/* 功能样式 */
@import "./features/animations.css";
@import "./features/transitions.css";
@import "./features/responsive.css";

/* 页面样式 */
@import "./pages/home.css";
@import "./pages/login.css";
@import "./pages/public.css";

/* 工具类 */
@import "./utilities/common.css";
@import "./utilities/layout.css";
```

## 💡 最佳实践

1. **命名规范**：
   - 使用小写字母和连字符：`button-primary.css`
   - 按功能分组：`navigation-top.css`、`navigation-sidebar.css`

2. **组织原则**：
   - 相关样式放在同一文件夹
   - 每个文件保持合理大小（建议不超过200行）
   - 使用 `@layer` 指令确保样式优先级

3. **导入顺序**：
   - 基础变量 → 组件样式 → 功能样式 → 页面样式 → 工具类

4. **注释规范**：
   - 每个文件顶部添加功能说明
   - 复杂样式添加行内注释

## 🎯 快速参考

| 文件夹 | 用途 | 示例 |
|--------|------|------|
| `theme/` | 主题变量、颜色、字体 | `colors.css`、`typography.css` |
| `components/` | 可复用组件样式 | `buttons.css`、`rail.css` |
| `features/` | 功能性样式 | `animations.css`、`responsive.css` |
| `pages/` | 特定页面样式 | `home.css`、`login.css` |
| `utilities/` | 工具类、布局 | `common.css`、`layout.css` |

## 📝 示例：添加新组件样式

假设要添加一个卡片组件：

1. 创建文件：`src/assets/styles/components/cards.css`

```css
/* 卡片组件样式 */
@layer components {
  .card {
    @apply bg-white rounded-lg shadow-md p-6;
  }
  
  .card-header {
    @apply text-xl font-bold mb-4;
  }
  
  .card-body {
    @apply text-gray-700;
  }
}
```

2. 在 `tailwind.css` 中添加引用：

```css
@import "./components/cards.css";
```

3. 在组件中使用：

```vue
<template>
  <div class="card">
    <div class="card-header">标题</div>
    <div class="card-body">内容</div>
  </div>
</template>
```

这样可以让您的代码更加模块化、易于维护和扩展！
