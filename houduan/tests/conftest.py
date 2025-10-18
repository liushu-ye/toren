import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from db.base import Base, SessionLocal
from core.config import settings
from main import app

# 使用测试数据库
TEST_DATABASE_URL = "sqlite:///./test.db"

def override_get_db():
    """覆盖数据库依赖，使用测试数据库"""
    try:
        engine = create_engine(
            TEST_DATABASE_URL,
            connect_args={"check_same_thread": False}
        )
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
        # 创建测试数据库表
        Base.metadata.create_all(bind=engine)
        
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        # 测试结束后删除数据库表
        Base.metadata.drop_all(bind=engine)

# 应用数据库依赖覆盖
app.dependency_overrides[SessionLocal] = override_get_db

@pytest.fixture(scope="module")
def client():
    """测试客户端夹具"""
    with TestClient(app) as c:
        yield c

@pytest.fixture(scope="module")
def db():
    """数据库会话夹具"""
    for db in override_get_db():
        yield db

@pytest.fixture(scope="module")
def test_user():
    """测试用户数据"""
    return {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpassword123",
        "full_name": "Test User"
    }

@pytest.fixture(scope="module")
def test_task():
    """测试任务数据"""
    from datetime import datetime, timedelta
    return {
        "title": "测试任务",
        "description": "这是一个测试任务",
        "reward": 100.0,
        "deadline": (datetime.now() + timedelta(days=7)).isoformat()
    }

@pytest.fixture(scope="module")
def auth_client(client, test_user):
    """已认证的测试客户端"""
    # 注册用户
    client.post("/api/users/register", json=test_user)
    
    # 登录获取token
    response = client.post(
        "/api/users/login",
        data={
            "username": test_user["username"],
            "password": test_user["password"]
        }
    )
    
    token = response.json()["access_token"]
    
    # 创建带认证头的客户端
    class AuthClient:
        def __init__(self, client, token):
            self.client = client
            self.token = token
        
        def get(self, *args, **kwargs):
            headers = kwargs.get("headers", {})
            headers["Authorization"] = f"Bearer {self.token}"
            kwargs["headers"] = headers
            return self.client.get(*args, **kwargs)
        
        def post(self, *args, **kwargs):
            headers = kwargs.get("headers", {})
            headers["Authorization"] = f"Bearer {self.token}"
            kwargs["headers"] = headers
            return self.client.post(*args, **kwargs)
        
        def put(self, *args, **kwargs):
            headers = kwargs.get("headers", {})
            headers["Authorization"] = f"Bearer {self.token}"
            kwargs["headers"] = headers
            return self.client.put(*args, **kwargs)
        
        def delete(self, *args, **kwargs):
            headers = kwargs.get("headers", {})
            headers["Authorization"] = f"Bearer {self.token}"
            kwargs["headers"] = headers
            return self.client.delete(*args, **kwargs)
    
    return AuthClient(client, token)