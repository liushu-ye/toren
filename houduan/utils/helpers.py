from typing import Any, Dict, List, Optional
from datetime import datetime, timedelta
import re
import json

def format_datetime(dt: datetime) -> str:
    """格式化日期时间"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def format_date(dt: datetime) -> str:
    """格式化日期"""
    return dt.strftime("%Y-%m-%d")

def calculate_time_remaining(deadline: datetime) -> Optional[Dict[str, Any]]:
    """计算剩余时间"""
    now = datetime.now(deadline.tzinfo) if deadline.tzinfo else datetime.now()
    if deadline <= now:
        return None
    
    remaining = deadline - now
    days = remaining.days
    hours, remainder = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    return {
        "total_seconds": remaining.total_seconds(),
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "formatted": f"{days}天 {hours}小时 {minutes}分钟"
    }

def validate_phone_number(phone: str) -> bool:
    """验证手机号码格式"""
    # 中国大陆手机号验证
    pattern = r'^1[3-9]\d{9}$'
    return bool(re.match(pattern, phone))

def sanitize_string(text: str, max_length: int = 255) -> str:
    """清理和验证字符串"""
    # 移除首尾空白字符
    text = text.strip()
    # 限制长度
    if len(text) > max_length:
        text = text[:max_length]
    # 移除危险字符（简单实现）
    text = re.sub(r'[<>"\']', '', text)
    return text

def pagination_metadata(
    total: int, 
    page: int, 
    page_size: int
) -> Dict[str, Any]:
    """生成分页元数据"""
    total_pages = (total + page_size - 1) // page_size
    has_next = page < total_pages
    has_prev = page > 1
    
    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "has_next": has_next,
        "has_prev": has_prev,
        "next_page": page + 1 if has_next else None,
        "prev_page": page - 1 if has_prev else None
    }

def to_camel_case(snake_str: str) -> str:
    """将蛇形命名转换为驼峰命名"""
    components = snake_str.split('_')
    # 首字母小写，其余单词首字母大写
    return components[0] + ''.join(x.title() for x in components[1:])

def to_snake_case(camel_str: str) -> str:
    """将驼峰命名转换为蛇形命名"""
    # 在大写字母前添加下划线，并转换为小写
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

def dict_to_camel_case(data: Dict[str, Any]) -> Dict[str, Any]:
    """将字典的键从蛇形命名转换为驼峰命名"""
    return {
        to_camel_case(key): value 
        if not isinstance(value, dict) 
        else dict_to_camel_case(value)
        for key, value in data.items()
    }

def safe_json_dumps(data: Any, default: Any = str) -> str:
    """安全地将数据转换为JSON字符串"""
    try:
        return json.dumps(data, ensure_ascii=False, default=default)
    except (TypeError, ValueError):
        return json.dumps({"error": "Invalid data for JSON serialization"})

def calculate_task_stats(tasks: List[Any]) -> Dict[str, Any]:
    """计算任务统计信息"""
    if not tasks:
        return {
            "total": 0,
            "pending": 0,
            "in_progress": 0,
            "completed": 0,
            "cancelled": 0,
            "total_reward": 0.0,
            "completed_reward": 0.0
        }
    
    from db.models.task import TaskStatus
    
    stats = {
        "total": len(tasks),
        "pending": 0,
        "in_progress": 0,
        "completed": 0,
        "cancelled": 0,
        "total_reward": 0.0,
        "completed_reward": 0.0
    }
    
    for task in tasks:
        stats["total_reward"] += task.reward
        
        if task.status == TaskStatus.PENDING:
            stats["pending"] += 1
        elif task.status == TaskStatus.IN_PROGRESS:
            stats["in_progress"] += 1
        elif task.status == TaskStatus.COMPLETED:
            stats["completed"] += 1
            stats["completed_reward"] += task.reward
        elif task.status == TaskStatus.CANCELLED:
            stats["cancelled"] += 1
    
    return stats