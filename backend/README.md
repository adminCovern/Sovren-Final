# Sovren AI Backend

FastAPI service with health and Prometheus metrics, Alembic migrations, and pytest tests.

## Quickstart

1. Create venv and install deps

```
python -m venv venv
./venv/Scripts/python -m pip install --upgrade pip
./venv/Scripts/pip install -r requirements.txt
```

2. Run tests

```
cd backend
./venv/Scripts/python -m pytest -q
```

3. Run the server

```
./venv/Scripts/uvicorn src.main:app --reload
```

4. Metrics

- Prometheus endpoint: `http://localhost:8000/metrics`

## Alembic Migrations

- Config: `alembic.ini`
- Env: `alembic/env.py` (wired to SQLAlchemy Base metadata)

Commands:

```
# Create an empty revision
./venv/Scripts/alembic -c alembic.ini revision -m "my change"

# Autogenerate based on models
./venv/Scripts/alembic -c alembic.ini revision --autogenerate -m "autogen"

# Apply migrations
./venv/Scripts/alembic -c alembic.ini upgrade head
```

Set DATABASE_URL if not using default:

```
set DATABASE_URL=postgresql+psycopg://user:pass@host:5432/db
```

