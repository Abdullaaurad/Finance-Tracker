# Finance Tracker Backend - Clean MVC Architecture

A well-structured FastAPI backend following MVC principles for the Finance Tracker application.

## Project Structure

```
Backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app initialization
│   ├── database/
│   │   ├── __init__.py
│   │   └── config.py          # Database configuration & Base class
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py            # User model (inherits from Base)
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py            # Pydantic schemas for validation
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py    # Business logic layer
│   ├── routes/
│   │   ├── __init__.py
│   │   └── user.py            # API endpoints (Controllers)
│   └── utils/
│       ├── __init__.py
│       └── helpers.py         # Utility functions
├── requirements.txt
├── .gitignore
├── run.py                     # Startup script
├── README.md
└── ARCHITECTURE.md
```

## Architecture Explanation

### Database Layer (`database/`)
- **config.py**: Contains database engine, session, and Base class
- **Responsibility**: Database infrastructure and configuration

### Models Layer (`models/`)
- **user.py**: User model that inherits from database Base
- **Responsibility**: Domain entities that map to database tables

### Other Layers
- **Schemas**: Pydantic models for API request/response validation
- **Services**: Business logic and data manipulation
- **Routes**: API endpoints (HTTP controllers)
- **Utils**: Helper functions and shared utilities

## Why This Structure?

1. **Clear Separation**:
   - `database/` = Database infrastructure
   - `models/` = Domain logic (inherits from database)

2. **Single Responsibility**: Each folder has a clear purpose

3. **Import Clarity**: Easy to understand where things come from

4. **Scalability**: Adding new models/entities follows same pattern

## Setup Instructions

### Option 1: Direct Installation (VSCode)
```bash
pip install -r requirements.txt
python run.py
```

### Option 2: Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python run.py
```

## API Endpoints
- `GET /api/v1/users` - Get all users
- `POST /api/v1/users` - Create user
- `GET /api/v1/users/{id}` - Get user by ID
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

Visit `http://127.0.0.1:8000/docs` for interactive documentation.