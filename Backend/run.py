#!/usr/bin/env python3
"""
Startup script for Finance Tracker API
Run this file to start the FastAPI server
"""
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host="127.0.0.1", 
        port=8000, 
        reload=True,
        reload_dirs=["app/"]
    )