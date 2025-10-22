from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """用户基础模型"""
    username: str = Field(..., min_length=3, max_length=50, description="用户名")
    email: EmailStr = Field(..., description="邮箱")
    full_name: str | None = Field(None, max_length=100, description="全名")
    phone_number: str | None = Field(None, max_length=20, description="电话号码")


class UserCreate(UserBase):
    """用户创建模型"""
    password: str = Field(..., min_length=6, description="密码")


class UserUpdate(BaseModel):
    """用户更新模型"""
    email: EmailStr | None = None
    full_name: str | None = Field(None, max_length=100)
    phone_number: str | None = Field(None, max_length=20)
    avatar: str | None = None


class UserInDB(UserBase):
    """数据库中的用户模型"""
    id: int
    avatar: str | None = None
    is_active: bool
    is_admin: bool
    created_at: datetime
    updated_at: datetime | None = None
    model_config = {
        "from_attributes": True
    }


class UserResponse(UserInDB):
    """用户响应模型"""
    pass


class Token(BaseModel):
    """令牌模型"""
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """令牌数据模型"""
    username: str | None = None


class UserLogin(BaseModel):
    """用户登录模型"""
    username: str = Field(..., description="用户名")
    password: str = Field(..., description="密码")
