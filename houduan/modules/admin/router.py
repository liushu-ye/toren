from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def admin_dashboard():
    return {"message": "Admin dashboard"}


@router.get("/users")
def get_all_users():
    return {"message": "Get all users"}
