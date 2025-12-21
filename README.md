# 兼职平台 MVP

## 项目简介
本项目旨在构建一个高质量、低社交负担的兼职与任务发布平台。  
用户可以快速浏览、领取、完成任务，也可以作为发布方创建任务。  
系统目标是帮助用户以最低沟通成本完成高效合作。

## 核心功能
- 用户注册与登录（手机号 / 邮箱）
- 发布与领取任务
- 任务状态追踪（待接取、进行中、已完成）
- 收益与结算系统
- 后台管理面板（任务审核、用户管理）

## 技术栈
- **前端**：Vu0.e 3 + TypeScript + Pinia + Vite + tailwindcss
- **后端**：FastAPI + SQLite（初期） / PostgreSQL（后期）
- **工具**：Git + GitHub + VS Code

## 本地运行步骤
1. 克隆项目仓库
2. 安装依赖：`npm install` / `pip install -r requirements.txt`
3. 启动开发环境：  
   - 前端：`npm run dev`  
   - 后端：`uvicorn main:app --reload`
