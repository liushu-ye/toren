from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from db.models.user import User
from db.models.task import Task

class AdminUserResponse(BaseModel):
    """管理员查看的用户响应模型"""
    id: int
    username: str
    email: str
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    is_active: bool
    is_admin: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class UserFilter(BaseModel):
    """用户筛选条件"""
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None

class UserListResponse(BaseModel):
    """用户列表响应模型"""
    items: List[AdminUserResponse]
    total: int
    page: int
    page_size: int

class UserStatusUpdate(BaseModel):
    """用户状态更新模型"""
    is_active: bool = Field(..., description="用户状态")

class TaskFilter(BaseModel):
    """任务筛选条件"""
    user_id: Optional[int] = None
    status: Optional[str] = None
    title: Optional[str] = None

class AdminTaskResponse(BaseModel):
    """管理员查看的任务响应模型"""
    id: int
    title: str
    reward: float
    status: str
    user_id: int
    username: Optional[str] = None  # 关联的用户名
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)