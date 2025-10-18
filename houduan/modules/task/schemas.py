from typing import Optional, List
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

from db.models.task import TaskStatus

class TaskBase(BaseModel):
    """任务基础模型"""
    title: str = Field(..., min_length=1, max_length=200, description="任务标题")
    description: Optional[str] = Field(None, description="任务描述")
    reward: float = Field(..., gt=0, description="任务奖励金额")
    deadline: Optional[datetime] = Field(None, description="任务截止时间")

class TaskCreate(TaskBase):
    """任务创建模型"""
    pass

class TaskUpdate(BaseModel):
    """任务更新模型"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    reward: Optional[float] = Field(None, gt=0)
    status: Optional[TaskStatus] = None
    deadline: Optional[datetime] = None

class TaskInDB(TaskBase):
    """数据库中的任务模型"""
    id: int
    status: TaskStatus
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)

class TaskResponse(TaskInDB):
    """任务响应模型"""
    pass

class TaskListResponse(BaseModel):
    """任务列表响应模型"""
    items: List[TaskResponse]
    total: int
    page: int
    page_size: int