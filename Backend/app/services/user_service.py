from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserUpdate, User
from app.utils.helpers import hash_password, verify_password

class UserService:
    def __init__(self, db: Session):
        self.db = db
    
    def get_user(self, user_id: int) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.id == user_id).first()
    
    def get_user_by_username(self, user_username: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.username == user_username).first()
    
    def get_user_by_email(self, email: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def get_users(self, skip: int = 0, limit: int = 100) -> List[UserModel]:
        return self.db.query(UserModel).offset(skip).limit(limit).all()
    
    def authenticate_user(self, username: str, password: str) -> Optional[UserModel]:
        user = self.get_user_by_username(username)
        if user and verify_password(password, user.hashed_password):
            return user  # Return the User object, not a set
        return None
    
    def create_user(self, user: UserCreate) -> UserModel:
        from app.utils.helpers import validate_username, validate_email, validate_password
        
        # Validate inputs
        if not validate_username(user.username):
            raise ValueError("Invalid username format")
        
        if not validate_email(user.email):
            raise ValueError("Invalid email format")
        
        is_valid, error_msg = validate_password(user.password)
        if not is_valid:
            raise ValueError(f"Invalid password: {error_msg}")
        
        hashed_password = hash_password(user.password)
        db_user = UserModel(
            username=user.username,
            email=user.email,
            hashed_password=hashed_password
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