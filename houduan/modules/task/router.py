from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from core.dependencies import get_db, get_current_active_user
from db.models.user import User
from db.models.task import TaskStatus
from modules.task.schemas import (
    TaskCreate, TaskUpdate, TaskResponse, TaskListResponse
)
from modules.task.service import task_service

router = APIRouter()

@router.post("/", response_model=dict, status_code=201)
def create_task(
    task_create: TaskCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """创建新任务"""
    return task_service.create_task(db, task_create, current_user.id)

@router.get("/me", response_model=dict)
def get_my_tasks(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页数量"),
    status: Optional[TaskStatus] = Query(None, description="任务状态筛选"),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取当前用户的任务列表"""
    return task_service.get_user_tasks(db, current_user.id, page, page_size, status)

@router.get("/{task_id}", response_model=dict)
def get_task_detail(
    task_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """获取任务详情"""
    return task_service.get_task_detail(db, task_id, current_user.id)

@router.put("/{task_id}", response_model=dict)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """更新任务"""
    return task_service.update_task(db, task_id, task_update, current_user.id)

@router.delete("/{task_id}", response_model=dict)
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """删除任务"""
    return task_service.delete_task(db, task_id, current_user.id)

@router.get("/search/list", response_model=dict)
def search_tasks(
    keyword: str = Query("", description="搜索关键词"),
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页数量"),
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """搜索任务"""
    return task_service.search_tasks(db, keyword, page, page_size)