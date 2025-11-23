from typing import Generator, Optional
from sqlalchemy.orm import Session
from app.database.config import SessionLocal
import os
from datetime import datetime, timedelta
from jose import JWTError, jwt
import bcrypt

# JWT Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "Abdulla")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing

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
    # Truncate password to 72 bytes (bcrypt limit)
    if len(password.encode('utf-8')) > 72:
        password = password[:72]
    # Use bcrypt directly, encoding password to bytes
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt(rounds=12)
    hashed = bcrypt.hashpw(password_bytes, salt)
    # Return the hash as a string
    return hashed.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against its hash
    """
    try:
        # Truncate password to 72 bytes (bcrypt limit) before verification
        if len(plain_password.encode('utf-8')) > 72:
            plain_password = plain_password[:72]
        # Use bcrypt directly, encoding both password and hash to bytes
        plain_password_bytes = plain_password.encode('utf-8')
        hashed_password_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)
    except Exception:
        return False

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create JWT access token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """
    Verify and decode JWT token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return username
    except JWTError:
        return None

def validate_username(username: str) -> bool:
    import re
    username_regex = r'^[a-zA-Z0-9_\-@]{3,20}$'
    return re.match(username_regex, username) is not None

def validate_email(email: str) -> bool:
    import re
    email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return re.match(email_regex, email) is not None

def validate_password(password: str) -> tuple[bool, str]:
    """
    Validate password and return (is_valid, error_message)
    """
    import re
    
    # Check bcrypt 72-byte limit
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        return False, "Password cannot exceed 72 bytes (approximately 72 characters)"
    
    # Check minimum length
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    # Check for at least one letter and one digit
    if not re.search(r'[A-Za-z]', password):
        return False, "Password must contain at least one letter"
    
    if not re.search(r'\d', password):
        return False, "Password must contain at least one number"
    
    return True, ""
