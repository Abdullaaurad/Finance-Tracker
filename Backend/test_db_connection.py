#!/usr/bin/env python3
"""
Test script to verify database connection
"""
import sys
import os

# Add the app directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.database.config import engine, Base
from app.models.user import User

def test_database_connection():
    try:
        # Test connection by creating tables
        print("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        print("[SUCCESS] Database tables created successfully!")
        
        # Test database connection
        with engine.connect() as connection:
            print("[SUCCESS] Database connection successful!")
            
        # Show database info
        import sqlite3
        db_path = os.path.join(os.path.dirname(__file__), 'test.db')
        if os.path.exists(db_path):
            print(f"[SUCCESS] Database file exists: {db_path}")
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Get table info
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"[SUCCESS] Database tables: {[table[0] for table in tables]}")
            
            # Get user table structure
            if any('user' in str(table).lower() for table in tables):
                cursor.execute("PRAGMA table_info(user);")
                columns = cursor.fetchall()
                print("[SUCCESS] User table columns:")
                for col in columns:
                    print(f"  - {col[1]} ({col[2]})")
                    
            conn.close()
        else:
            print("[ERROR] Database file not found")
            
    except Exception as e:
        print(f"[ERROR] Database connection failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    print("Testing database connection...")
    test_database_connection()