from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from core.dependencies import get_db, get_current_active_user
from db.models.user import User
from modules.user.schemas import (
    UserCreate, UserUpdate, UserResponse, Token, UserLogin
)
from modules.user.service import user_service

router = APIRouter()

@router.post("/register", response_model=dict, status_code=status.HTTP_201_CREATED)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    """用户注册"""
    return user_service.register_user(db, user_create)

@router.post("/login", response_model=dict)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """用户登录"""
    result = user_service.authenticate_user(db, form_data.username, form_data.password)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return result

@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    """获取当前用户信息"""
    return current_user

@router.put("/me", response_model=dict)
def update_current_user(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """更新当前用户信息"""
    return user_service.update_user_profile(db, current_user.id, user_update)

@router.post("/change-password", response_model=dict)
def change_password(
    current_password: str,
    new_password: str,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_db)
):
    """修改密码"""
    return user_service.change_password(db, current_user.id, current_password, new_password)

@router.post("/logout", response_model=dict)
def logout(current_user: User = Depends(get_current_active_user)):
    """用户登出"""
    # JWT是无状态的，客户端删除token即可
    return {"message": "登出成功"}