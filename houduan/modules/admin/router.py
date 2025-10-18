from typing import Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy import func

from core.dependencies import get_db, get_current_admin_user
from db.models.user import User
from db.models.task import Task, TaskStatus
from modules.admin.schemas import (
    AdminUserResponse, UserListResponse, UserStatusUpdate,
    AdminTaskResponse
)

router = APIRouter()

@router.get("/users", response_model=UserListResponse)
def get_users(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页数量"),
    username: Optional[str] = Query(None, description="用户名搜索"),
    email: Optional[str] = Query(None, description="邮箱搜索"),
    is_active: Optional[bool] = Query(None, description="用户状态筛选"),
    current_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """管理员获取用户列表"""
    # 构建查询
    query = db.query(User)
    
    # 应用筛选条件
    if username:
        query = query.filter(User.username.ilike(f"%{username}%"))
    if email:
        query = query.filter(User.email.ilike(f"%{email}%"))
    if is_active is not None:
        query = query.filter(User.is_active == is_active)
    
    # 获取总数
    total = query.count()
    
    # 分页查询
    skip = (page - 1) * page_size
    users = query.offset(skip).limit(page_size).all()
    
    # 转换为响应模型
    items = [AdminUserResponse.model_validate(user) for user in users]
    
    return UserListResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size
    )

@router.get("/users/{user_id}", response_model=AdminUserResponse)
def get_user_detail(
    user_id: int,
    current_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """管理员获取用户详情"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return AdminUserResponse.model_validate(user)

@router.put("/users/{user_id}/status", response_model=dict)
def update_user_status(
    user_id: int,
    status_update: UserStatusUpdate,
    current_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """管理员更新用户状态"""
    # 不能修改自己的状态
    if user_id == current_user.id:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="不能修改自己的状态"
        )
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    user.is_active = status_update.is_active
    db.commit()
    
    return {
        "message": "用户状态更新成功",
        "user_id": user_id,
        "is_active": status_update.is_active
    }

@router.get("/tasks", response_model=dict)
def get_all_tasks(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(10, ge=1, le=100, description="每页数量"),
    status: Optional[TaskStatus] = Query(None, description="任务状态筛选"),
    user_id: Optional[int] = Query(None, description="用户ID筛选"),
    current_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """管理员获取所有任务列表"""
    # 构建查询
    query = db.query(Task, User.username).join(User, Task.user_id == User.id)
    
    # 应用筛选条件
    if status:
        query = query.filter(Task.status == status)
    if user_id:
        query = query.filter(Task.user_id == user_id)
    
    # 获取总数
    total = query.count()
    
    # 分页查询
    skip = (page - 1) * page_size
    task_results = query.offset(skip).limit(page_size).all()
    
    # 转换为响应格式
    items = []
    for task, username in task_results:
        task_data = {
            "id": task.id,
            "title": task.title,
            "reward": task.reward,
            "status": task.status.value,
            "user_id": task.user_id,
            "username": username,
            "created_at": task.created_at
        }
        items.append(task_data)
    
    return {
        "items": items,
        "total": total,
        "page": page,
        "page_size": page_size
    }

@router.get("/dashboard/stats", response_model=dict)
def get_dashboard_stats(
    current_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """获取管理员仪表盘统计数据"""
    # 统计用户数量
    total_users = db.query(func.count(User.id)).scalar() or 0
    active_users = db.query(func.count(User.id)).filter(User.is_active == True).scalar() or 0
    
    # 统计任务数量
    total_tasks = db.query(func.count(Task.id)).scalar() or 0
    pending_tasks = db.query(func.count(Task.id)).filter(Task.status == TaskStatus.PENDING).scalar() or 0
    completed_tasks = db.query(func.count(Task.id)).filter(Task.status == TaskStatus.COMPLETED).scalar() or 0
    
    return {
        "users": {
            "total": total_users,
            "active": active_users,
            "inactive": total_users - active_users
        },
        "tasks": {
            "total": total_tasks,
            "pending": pending_tasks,
            "completed": completed_tasks,
            "in_progress": db.query(func.count(Task.id)).filter(Task.status == TaskStatus.IN_PROGRESS).scalar() or 0,
            "cancelled": db.query(func.count(Task.id)).filter(Task.status == TaskStatus.CANCELLED).scalar() or 0
        }
    }