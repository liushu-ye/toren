from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import pytest

class TestTask:
    def test_create_task(self, auth_client, test_task: dict):
        """测试创建任务"""
        response = auth_client.post("/api/tasks/", json=test_task)
        assert response.status_code == 201
        data = response.json()
        assert data["title"] == test_task["title"]
        assert data["reward"] == test_task["reward"]
        assert data["status"] == "pending"
    
    def test_get_my_tasks(self, auth_client, test_task: dict):
        """测试获取我的任务列表"""
        # 先创建一个任务
        auth_client.post("/api/tasks/", json=test_task)
        
        # 获取任务列表
        response = auth_client.get("/api/tasks/me")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] >= 1
        assert len(data["items"]) >= 1
    
    def test_get_task_detail(self, auth_client, test_task: dict):
        """测试获取任务详情"""
        # 创建任务
        create_response = auth_client.post("/api/tasks/", json=test_task)
        task_id = create_response.json()["id"]
        
        # 获取详情
        response = auth_client.get(f"/api/tasks/{task_id}")
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == task_id
        assert data["title"] == test_task["title"]
    
    def test_update_task(self, auth_client, test_task: dict):
        """测试更新任务"""
        # 创建任务
        create_response = auth_client.post("/api/tasks/", json=test_task)
        task_id = create_response.json()["id"]
        
        # 更新任务
        update_data = {
            "title": "Updated Task Title",
            "status": "in_progress"
        }
        response = auth_client.put(f"/api/tasks/{task_id}", json=update_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == update_data["title"]
        assert data["status"] == update_data["status"]
    
    def test_delete_task(self, auth_client, test_task: dict):
        """测试删除任务"""
        # 创建任务
        create_response = auth_client.post("/api/tasks/", json=test_task)
        task_id = create_response.json()["id"]
        
        # 删除任务
        response = auth_client.delete(f"/api/tasks/{task_id}")
        assert response.status_code == 200
        assert response.json()["message"] == "任务删除成功"
        
        # 验证任务已删除
        detail_response = auth_client.get(f"/api/tasks/{task_id}")
        assert detail_response.status_code == 404
    
    def test_search_tasks(self, auth_client, test_task: dict):
        """测试搜索任务"""
        # 创建任务
        auth_client.post("/api/tasks/", json=test_task)
        
        # 搜索任务
        keyword = "测试"
        response = auth_client.get(f"/api/tasks/search/list?keyword={keyword}")
        assert response.status_code == 200
        data = response.json()
        assert "items" in data
    
    def test_task_status_transition(self, auth_client, test_task: dict):
        """测试任务状态转换"""
        # 创建任务
        create_response = auth_client.post("/api/tasks/", json=test_task)
        task_id = create_response.json()["id"]
        
        # 更新为进行中
        response = auth_client.put(f"/api/tasks/{task_id}", json={"status": "in_progress"})
        assert response.status_code == 200
        assert response.json()["status"] == "in_progress"
        
        # 更新为已完成
        response = auth_client.put(f"/api/tasks/{task_id}", json={"status": "completed"})
        assert response.status_code == 200
        assert response.json()["status"] == "completed"
        
        # 已完成的任务不能再修改状态
        response = auth_client.put(f"/api/tasks/{task_id}", json={"status": "in_progress"})
        assert response.status_code == 400