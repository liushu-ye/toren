from typing import Optional, List, Dict
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from db.models.task import TaskStatus
from modules.task.schemas import TaskCreate, TaskUpdate
from modules.task.crud import task_crud

class TaskService:
    @staticmethod
    def create_task(db: Session, task_create: TaskCreate, user_id: int) -> dict:
        """创建新任务"""
        # 验证截止时间
        if task_create.deadline and task_create.deadline < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="截止时间不能早于当前时间"
            )
        
        # 创建任务
        db_task = task_crud.create_task(db, task_create, user_id)
        
        return {
            "id": db_task.id,
            "title": db_task.title,
            "reward": db_task.reward,
            "status": db_task.status.value,
            "created_at": db_task.created_at
        }
    
    @staticmethod
    def get_task_detail(db: Session, task_id: int, user_id: int) -> dict:
        """获取任务详情"""
        task = task_crud.get_task_by_id(db, task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="任务不存在"
            )
        
        # 验证任务归属
        if task.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="无权访问该任务"
            )
        
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "reward": task.reward,
            "status": task.status.value,
            "deadline": task.deadline,
            "created_at": task.created_at,
            "updated_at": task.updated_at
        }
    
    @staticmethod
    def update_task(db: Session, task_id: int, task_update: TaskUpdate, user_id: int) -> dict:
        """更新任务"""
        # 获取任务并验证归属
        task = task_crud.get_task_by_id(db, task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="任务不存在"
            )
        
        if task.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="无权修改该任务"
            )
        
        # 验证状态转换逻辑
        if task_update.status and task.status != task_update.status:
            # 已完成的任务不能再修改
            if task.status == TaskStatus.COMPLETED:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="已完成的任务不能修改状态"
                )
            # 已取消的任务不能再修改
            if task.status == TaskStatus.CANCELLED:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="已取消的任务不能修改状态"
                )
        
        # 更新任务
        updated_task = task_crud.update_task(db, task_id, task_update)
        
        return {
            "id": updated_task.id,
            "title": updated_task.title,
            "status": updated_task.status.value,
            "reward": updated_task.reward,
            "updated_at": updated_task.updated_at
        }
    
    @staticmethod
    def delete_task(db: Session, task_id: int, user_id: int) -> dict:
        """删除任务"""
        # 获取任务并验证归属
        task = task_crud.get_task_by_id(db, task_id)
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="任务不存在"
            )
        
        if task.user_id != user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="无权删除该任务"
            )
        
        # 执行删除
        task_crud.delete_task(db, task_id)
        
        return {"message": "任务删除成功"}
    
    @staticmethod
    def get_user_tasks(
        db: Session, 
        user_id: int, 
        page: int = 1, 
        page_size: int = 10, 
        status: Optional[TaskStatus] = None
    ) -> dict:
        """获取用户的任务列表"""
        # 计算偏移量
        skip = (page - 1) * page_size
        
        # 获取任务列表
        if status:
            tasks = task_crud.get_tasks_by_status(db, status, skip, page_size)
            # 过滤用户的任务
            tasks = [task for task in tasks if task.user_id == user_id]
            total = len(tasks)
        else:
            tasks = task_crud.get_tasks_by_user(db, user_id, skip, page_size)
            total = task_crud.get_tasks_count(db, user_id=user_id)
        
        # 转换为响应格式
        items = [
            {
                "id": task.id,
                "title": task.title,
                "reward": task.reward,
                "status": task.status.value,
                "deadline": task.deadline,
                "created_at": task.created_at
            }
            for task in tasks
        ]
        
        return {
            "items": items,
            "total": total,
            "page": page,
            "page_size": page_size
        }
    
    @staticmethod
    def search_tasks(
        db: Session, 
        keyword: str = "", 
        page: int = 1, 
        page_size: int = 10
    ) -> dict:
        """搜索任务"""
        skip = (page - 1) * page_size
        
        tasks = task_crud.search_tasks(db, keyword, skip, page_size)
        # 这里简化处理，实际可能需要计算总数
        
        items = [
            {
                "id": task.id,
                "title": task.title,
                "reward": task.reward,
                "status": task.status.value,
                "created_at": task.created_at
            }
            for task in tasks
        ]
        
        return {
            "items": items,
            "total": len(items),
            "page": page,
            "page_size": page_size
        }

# 创建service实例
task_service = TaskService()