# Convenience make targets (use from WSL or Git Bash)

COMPOSE=infra/docker-compose.yml

.PHONY: up down restart logs backend-logs backend-test migrate fe-dev fe-build fe-audit

up:
	docker compose -f $(COMPOSE) up -d

down:
	docker compose -f $(COMPOSE) down

restart:
	docker compose -f $(COMPOSE) restart

logs:
	docker compose -f $(COMPOSE) logs -f

backend-logs:
	docker compose -f $(COMPOSE) logs -f backend

backend-test:
	docker compose -f $(COMPOSE) exec backend pytest -q

migrate:
	docker compose -f $(COMPOSE) exec -e DATABASE_URL=postgresql+psycopg://sovren:securepass@db:5432/sovren_ai backend alembic -c alembic.ini upgrade head

fe-dev:
	cd frontend && npm run dev

fe-build:
	cd frontend && npm run build

fe-audit:
	cd frontend && npm run audit

