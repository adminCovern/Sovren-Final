# Sovren AI Monorepo

This repo contains:
- frontend: Next.js + TypeScript + Playwright E2E
- backend: FastAPI + Prometheus metrics + SQLAlchemy + Alembic + pytest
- infra: docker compose (dev-only) for Postgres, Redis, Mongo, backend

## Quickstart

Frontend
- cd frontend
- npm install
- npm run dev (http://localhost:3000)
- npx playwright install --with-deps
- npx playwright test -g "homepage loads and health endpoint returns ok"

Backend
- python -m venv backend/venv
- backend/venv/Scripts/pip install -r backend/requirements.txt
- cd backend && backend/venv/Scripts/python -m pytest -q
- backend/venv/Scripts/uvicorn src.main:app --reload (http://localhost:8000)
- Metrics: http://localhost:8000/metrics

Migrations (optional)
- Ensure Postgres running (see infra), set DATABASE_URL or use alembic.ini default
- cd backend
- backend/venv/Scripts/alembic -c alembic.ini upgrade head

Dev Infra (Docker Desktop required)
- docker compose -f infra/docker-compose.yml up -d

## CI
- GitHub Actions runs backend tests, then frontend lint/build + Playwright E2E

## Notes
- No secrets committed; see .env.example files
- Compose is dev-only; no prod compose added

