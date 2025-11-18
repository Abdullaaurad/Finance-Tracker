from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.config import engine, Base
from app.routes import user

# Import all models to ensure they are registered with SQLAlchemy
import app.models.user

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Finance Tracker API",
    description="A FastAPI backend for Finance Tracker application",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router, prefix="/api/v1", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Finance Tracker API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}