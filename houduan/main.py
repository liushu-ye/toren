from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from db.base import engine, Base
from modules.user.router import router as user_router
from modules.task.router import router as task_router
from modules.admin.router import router as admin_router

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 创建FastAPI应用
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(user_router, prefix="/api/users", tags=["users"])
app.include_router(task_router, prefix="/api/tasks", tags=["tasks"])
app.include_router(admin_router, prefix="/api/admin", tags=["admin"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Toren API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}