from typing import List
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # 项目基本配置
    PROJECT_NAME: str = Field(default="Toren API", description="项目名称")
    VERSION: str = Field(default="1.0.0", description="项目版本")
    DESCRIPTION: str = Field(default="兼职任务管理系统API", description="项目描述")
    
    # 数据库配置
    DATABASE_URL: str = Field(..., description="数据库连接URL")
    
    # JWT配置
    SECRET_KEY: str = Field(..., description="JWT密钥")
    ALGORITHM: str = Field(default="HS256", description="JWT算法")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(default=30, description="访问令牌过期时间（分钟）")
    
    # CORS配置
    BACKEND_CORS_ORIGINS: List[str] = Field(default=["http://localhost:3000"], description="允许的跨域来源")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()