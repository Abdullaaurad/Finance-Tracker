from typing import Generator, Optional
from sqlalchemy.orm import Session
from app.database.config import SessionLocal

def get_db() -> Generator[Session, None, None]:
    """
    Database dependency for FastAPI routes
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user():
    """
    Placeholder for authentication dependency
    """
    pass

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt
    """
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash
    """
    from passlib.context import CryptContext
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(plain_password, hashed_password)