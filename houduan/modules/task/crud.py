from typing import Optional, List
from sqlalchemy.orm import Session
from sqlalchemy import func

from db.models.task import Task, TaskStatus
from modules.task.schemas import TaskCreate, TaskUpdate

class TaskCRUD:
    @staticmethod
    def get_task_by_id(db: Session, task_id: int) -> Optional[Task]:
        """通过ID获取任务"""
        return db.query(Task).filter(Task.id == task_id).first()
    
    @staticmethod
    def get_tasks_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
        """获取用户的任务列表"""
        return db.query(Task).filter(Task.user_id == user_id).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_tasks_by_status(db: Session, status: TaskStatus, skip: int = 0, limit: int = 100) -> List[Task]:
        """通过状态获取任务列表"""
        return db.query(Task).filter(Task.status == status).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[Task]:
        """获取所有任务"""
        return db.query(Task).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_task(db: Session, task: TaskCreate, user_id: int) -> Task:
        """创建任务"""
        db_task = Task(
            **task.model_dump(),
            user_id=user_id
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    
    @staticmethod
    def update_task(db: Session, task_id: int, task_update: TaskUpdate) -> Optional[Task]:
        """更新任务"""
        db_task = TaskCRUD.get_task_by_id(db, task_id)
        if not db_task:
            return None
        
        update_data = task_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)
        
        db.commit()
        db.refresh(db_task)
        return db_task
    
    @staticmethod
    def delete_task(db: Session, task_id: int) -> bool:
        """删除任务"""
        db_task = TaskCRUD.get_task_by_id(db, task_id)
        if not db_task:
            return False
        
        db.delete(db_task)
        db.commit()
        return True
    
    @staticmethod
    def get_tasks_count(db: Session, user_id: Optional[int] = None, status: Optional[TaskStatus] = None) -> int:
        """获取任务总数"""
        query = db.query(func.count(Task.id))
        if user_id:
            query = query.filter(Task.user_id == user_id)
        if status:
            query = query.filter(Task.status == status)
        return query.scalar() or 0
    
    @staticmethod
    def search_tasks(
        db: Session, 
        keyword: str = "", 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Task]:
        """搜索任务"""
        query = db.query(Task)
        if keyword:
            query = query.filter(
                (Task.title.ilike(f"%{keyword}%") | 
                 Task.description.ilike(f"%{keyword}%"))
            )
        return query.offset(skip).limit(limit).all()

# 创建crud实例
task_crud = TaskCRUD()