from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import pytest

class TestUser:
    def test_register_user(self, client: TestClient, test_user: dict):
        """测试用户注册"""
        response = client.post("/api/users/register", json=test_user)
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == test_user["username"]
        assert data["email"] == test_user["email"]
    
    def test_register_existing_username(self, client: TestClient, test_user: dict):
        """测试注册已存在的用户名"""
        # 先注册一次
        client.post("/api/users/register", json=test_user)
        # 再次注册相同用户名
        response = client.post("/api/users/register", json=test_user)
        assert response.status_code == 400
        assert "用户名已被使用" in response.json()["detail"]
    
    def test_user_login(self, client: TestClient, test_user: dict):
        """测试用户登录"""
        # 先注册用户
        client.post("/api/users/register", json=test_user)
        # 登录
        response = client.post(
            "/api/users/login",
            data={
                "username": test_user["username"],
                "password": test_user["password"]
            }
        )
        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        assert data["user"]["username"] == test_user["username"]
    
    def test_invalid_login(self, client: TestClient, test_user: dict):
        """测试无效登录"""
        response = client.post(
            "/api/users/login",
            data={
                "username": test_user["username"],
                "password": "wrongpassword"
            }
        )
        assert response.status_code == 401
    
    def test_get_current_user(self, auth_client):
        """测试获取当前用户信息"""
        response = auth_client.get("/api/users/me")
        assert response.status_code == 200
        data = response.json()
        assert "username" in data
        assert "email" in data
    
    def test_update_user_profile(self, auth_client):
        """测试更新用户信息"""
        update_data = {
            "full_name": "Updated Name",
            "phone_number": "13800138000"
        }
        response = auth_client.put("/api/users/me", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["full_name"] == update_data["full_name"]
        assert data["phone_number"] == update_data["phone_number"]
    
    def test_change_password(self, auth_client):
        """测试修改密码"""
        # 注意：这里需要修改router.py中的change_password接口，使其接受JSON格式
        # 当前实现需要调整以支持测试
        # 以下是假设接口已调整为接受JSON的测试
        response = auth_client.post(
            "/api/users/change-password",
            json={
                "current_password": "testpassword123",
                "new_password": "newpassword123"
            }
        )
        assert response.status_code == 200
        assert response.json()["message"] == "密码更新成功"
    
    def test_logout(self, auth_client):
        """测试用户登出"""
        response = auth_client.post("/api/users/logout")
        assert response.status_code == 200
        assert response.json()["message"] == "登出成功"