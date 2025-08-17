# Contributing

## Setup
- Clone repo and checkout a feature branch
- Frontend: `cd frontend && npm ci`
- Backend: `python -m venv backend/venv && backend/venv/Scripts/pip install -r backend/requirements.txt`

## Testing
- Backend: `cd backend && backend/venv/Scripts/python -m pytest -q`
- Frontend: `cd frontend && npm run build && npx playwright install --with-deps && npx playwright test`

## CI
- PRs run backend tests and frontend lint/build + E2E

## Migrations
- Ensure Postgres running (or adjust DATABASE_URL)
- `cd backend && ./venv/Scripts/alembic -c alembic.ini revision --autogenerate -m "change" && ./venv/Scripts/alembic -c alembic.ini upgrade head`

