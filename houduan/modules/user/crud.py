from sqlalchemy.orm import Session

from db.models.user import User
from modules.user.schemas import UserCreate, UserUpdate


class UserCRUD:
    @staticmethod
    def get_user_by_id(db: Session, user_id: int) -> User | None:
        """通过ID获取用户"""
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str) -> User | None:
        """通过用户名获取用户"""
        return db.query(User).filter(User.username == username).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> User | None:
        """通过邮箱获取用户"""
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
        """获取用户列表"""
        return db.query(User).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db: Session, user: UserCreate, hashed_password: str) -> User:
        """创建用户"""
        db_user = User(
            **user.model_dump(),
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdate) -> User | None:
        """更新用户信息"""
        db_user = UserCRUD.get_user_by_id(db, user_id)
        if not db_user:
            return None

        update_data = user_update.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_user, field, value)

        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def update_password(db: Session, user_id: int, hashed_password: str) -> User | None:
        """更新用户密码"""
        db_user = UserCRUD.get_user_by_id(db, user_id)
        if not db_user:
            return None

        db_user.hashed_password = hashed_password
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def deactivate_user(db: Session, user_id: int) -> User | None:
        """禁用用户"""
        db_user = UserCRUD.get_user_by_id(db, user_id)
        if not db_user:
            return None

        db_user.is_active = False
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def activate_user(db: Session, user_id: int) -> User | None:
        """激活用户"""
        db_user = UserCRUD.get_user_by_id(db, user_id)
        if not db_user:
            return None

        db_user.is_active = True
        db.commit()
        db.refresh(db_user)
        return db_user


user_crud = UserCRUD()
