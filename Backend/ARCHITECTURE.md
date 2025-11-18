# Finance Tracker Backend - MVC Architecture

A well-structured FastAPI backend following MVC principles for the Finance Tracker application.

## Project Structure

```
Backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app initialization
│   ├── database/
│   │   ├── __init__.py
│   │   ├── config.py          # Database configuration
│   │   └── models/            # Database models
│   │       ├── __init__.py
│   │       └── base.py        # Base model class
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py            # User model
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py            # Pydantic schemas
│   ├── services/
│   │   ├── __init__.py
│   │   └── user_service.py    # Business logic
│   ├── routes/
│   │   ├── __init__.py
│   │   └── user.py            # API endpoints
│   └── utils/
│       ├── __init__.py
│       └── helpers.py         # Utility functions
├── requirements.txt
├── .gitignore
└── README.md
```

## Architecture Explanation

- **Models** (`models/`): Database models (SQLAlchemy)
- **Schemas** (`schemas/`): Pydantic models for validation
- **Services** (`services/`): Business logic layer
- **Routes** (`routes/`): API endpoints (Controllers)
- **Database** (`database/`): Database configuration and base models
- **Utils** (`utils/`): Helper functions and utilities

## Benefits

1. **Separation of Concerns**: Each layer has a specific responsibility
2. **Maintainability**: Easy to find and modify specific functionality
3. **Testability**: Each component can be tested independently
4. **Scalability**: Easy to add new features without cluttering
5. **Team Collaboration**: Multiple developers can work on different layers