import logging
import sys
from datetime import datetime
import os

# 确保logs目录存在
logs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(logs_dir, exist_ok=True)

# 日志文件名
log_file = os.path.join(logs_dir, f"app_{datetime.now().strftime('%Y-%m-%d')}.log")

# 配置日志记录器
logger = logging.getLogger("toren_api")
logger.setLevel(logging.INFO)

# 创建格式化器
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# 创建文件处理器
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# 创建控制台处理器
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# 添加处理器到记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def get_logger() -> logging.Logger:
    """获取配置好的日志记录器"""
    return logger

def log_request(request, response=None, error=None):
    """记录API请求日志"""
    log_data = {
        "method": request.method,
        "url": request.url.path,
        "query_params": dict(request.query_params),
        "client_ip": request.client.host if request.client else "unknown"
    }
    
    if response:
        log_data["status_code"] = response.status_code
        logger.info(f"API Request: {log_data}")
    elif error:
        log_data["error"] = str(error)
        logger.error(f"API Request Error: {log_data}")
    else:
        logger.info(f"API Request Started: {log_data}")