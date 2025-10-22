from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_tasks():
    return {"message": "Get all tasks"}


@router.post("/")
def create_task():
    return {"message": "Create a new task"}
