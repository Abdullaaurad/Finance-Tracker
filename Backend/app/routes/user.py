from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.utils.helpers import get_db, validate_username, validate_email, validate_password, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from app.services.user_service import UserService
from app.schemas.user import UserCreate, UserUpdate, User, UserLogin, Token
from typing import List

router = APIRouter()

@router.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    user_service = UserService(db)
    users = user_service.get_users(skip=skip, limit=limit)
    return users

@router.post("/users/login", response_model=Token)
def login_user(user_login: UserLogin, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.authenticate_user(user_login.username, user_login.password)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    
    # Validate username
    if not validate_username(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username format"
        )
    
    # Validate email
    if not validate_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email format"
        )
    
    # Validate password
    if not validate_password(user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid password format"
        )
    
    # Check if email already exists
    db_user = user_service.get_user_by_email(user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Check if username already exists
    db_user = user_service.get_user_by_username(user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    return user_service.create_user(user)

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.get_user(user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    user_service = UserService(db)
    db_user = user_service.update_user(user_id, user)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service = UserService(db)
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return {"message": "User deleted successfully"}