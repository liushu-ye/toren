from typing import Optional
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from core.config import settings
from core.security import verify_password, get_password_hash, create_access_token
from modules.user.schemas import UserCreate, UserUpdate, Token
from modules.user.crud import user_crud

class UserService:
    @staticmethod
    def register_user(db: Session, user_create: UserCreate) -> dict:
        """注册新用户"""
        # 检查用户名是否已存在
        if user_crud.get_user_by_username(db, username=user_create.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="用户名已被使用"
            )
        
        # 检查邮箱是否已存在
        if user_crud.get_user_by_email(db, email=user_create.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="邮箱已被注册"
            )
        
        # 创建用户
        hashed_password = get_password_hash(user_create.password)
        db_user = user_crud.create_user(db, user_create, hashed_password)
        
        return {
            "id": db_user.id,
            "username": db_user.username,
            "email": db_user.email
        }
    
    @staticmethod
    def authenticate_user(db: Session, username: str, password: str) -> Optional[dict]:
        """用户认证"""
        user = user_crud.get_user_by_username(db, username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        
        # 创建访问令牌
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.username}, expires_delta=access_token_expires
        )
        
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "full_name": user.full_name,
                "is_admin": user.is_admin
            }
        }
    
    @staticmethod
    def update_user_profile(db: Session, user_id: int, user_update: UserUpdate) -> dict:
        """更新用户信息"""
        # 如果更新邮箱，检查是否已存在
        if user_update.email:
            existing_user = user_crud.get_user_by_email(db, user_update.email)
            if existing_user and existing_user.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="邮箱已被其他用户使用"
                )
        
        updated_user = user_crud.update_user(db, user_id, user_update)
        if not updated_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="用户不存在"
            )
        
        return {
            "id": updated_user.id,
            "username": updated_user.username,
            "email": updated_user.email,
            "full_name": updated_user.full_name,
            "phone_number": updated_user.phone_number,
            "avatar": updated_user.avatar
        }
    
    @staticmethod
    def change_password(db: Session, user_id: int, current_password: str, new_password: str) -> dict:
        """修改密码"""
        user = user_crud.get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="用户不存在"
            )
        
        # 验证当前密码
        if not verify_password(current_password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="当前密码错误"
            )
        
        # 更新密码
        hashed_password = get_password_hash(new_password)
        user_crud.update_password(db, user_id, hashed_password)
        
        return {"message": "密码更新成功"}

user_service = UserService()