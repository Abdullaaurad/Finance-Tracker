from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserUpdate, User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_user(self, user_id: int) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def get_user_by_email(self, email: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def get_user_by_username(self, username: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.username == username).first()
    
    def get_users(self, skip: int = 0, limit: int = 100) -> List[UserModel]:
        return self.db.query(UserModel).offset(skip).limit(limit).all()
    
    def create_user(self, user: UserCreate) -> UserModel:
        hashed_password = self.get_password_hash(user.password)
        db_user = UserModel(
            email=user.email,
            username=user.username,
            full_name=user.full_name,
            hashed_password=hashed_password,
            is_active=user.is_active
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[UserModel]:
        db_user = self.get_user(user_id)
        if db_user:
            update_data = user_update.dict(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_user, field, value)
            self.db.commit()
            self.db.refresh(db_user)
        return db_user
    
    def delete_user(self, user_id: int) -> bool:
        db_user = self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
            return True
        return False
    
    def get_password_hash(self, password: str) -> str:
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)