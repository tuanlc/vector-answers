# Vector Answers - AI Coding Agent Instructions

## Project Overview
FastAPI-based vector search application with PostgreSQL + pgvector backend for question answering.

## Architecture & Components
- **FastAPI Server**: Located in `server/` directory with main app in `main.py`
- **Database**: PostgreSQL with pgvector extension via Docker Compose
- **Configuration**: Environment-based config using `config.py` with `.env` files
- **Database Layer**: SQLModel/SQLAlchemy abstractions in `db.py`

## Essential Workflows

### Development Setup
All development commands run from `./server` directory (critical requirement):
```bash
# Database setup
docker-compose up -d  # (run from project root)
cd server            # Always work from server/ directory
uvicorn main:app --reload
```

### Environment Configuration
- Copy `server/.env.example` to `server/.env` for local development
- Database config pattern: `postgresql://{user}:{pass}@localhost:{port}/{db}`
- Default database credentials: postgres/postgres on port 5432, db name 'vectordb'

### Project Structure Patterns
- **Server-centric**: All Python code lives in `server/` subdirectory
- **Separation of concerns**: `config.py` for env vars, `db.py` for database operations, `main.py` for FastAPI app
- **Docker-first database**: No local PostgreSQL installation required

## Key Implementation Patterns

### Database Connection
```python
# Standard pattern in db.py
from sqlmodel import create_engine, Session
DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)
```

### FastAPI Application Structure
- App initialization includes `init_db()` call for table creation
- Health check endpoint at `/healthz` verifies database connectivity
- Import pattern: `from db import init_db, health_connection`

### Configuration Management
- Environment variables loaded via `python-dotenv` in `config.py`
- All config variables accessed through `config.py` imports, not direct `os.getenv()`
- Port defaulting pattern: `os.getenv("DB_PORT", "5432")`

## Technology Stack
- **Backend**: FastAPI with SQLModel (SQLAlchemy + Pydantic integration)
- **Database**: PostgreSQL with pgvector extension for vector operations
- **Dev Environment**: Python virtual environment in `server/venv/`

## Critical Notes
- **Working Directory**: Always execute Python commands from `./server` folder
- **Vector Database**: Uses pgvector/pgvector:pg18 Docker image for vector search capabilities
- **Database Echo**: SQLAlchemy echo=True enabled for SQL query logging
- **Health Monitoring**: `/healthz` endpoint executes `SELECT 1` to verify database connectivity