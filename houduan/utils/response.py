from fastapi.responses import JSONResponse
from datetime import datetime


def success(data=None, message="success"):
    return JSONResponse({
        "code": 0,
        "message": message,
        "data": data,
        "timestamp": int(datetime.now().timestamp())
    })


def error(code=1, message="error", data=None):
    return JSONResponse({
        "code": code,
        "message": message,
        "data": data,
        "timestamp": int(datetime.now().timestamp())
    })
