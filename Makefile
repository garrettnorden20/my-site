.PHONY: dev build up down logs test migrate backup restore smoke

dev:
	uvicorn app.main:app --reload

build:
	docker buildx build --platform linux/amd64,linux/arm64 -t my-site-app -f ops/Dockerfile.app .

up:
	docker compose -f ops/compose.yaml up -d

down:
	docker compose -f ops/compose.yaml down

logs:
	docker compose -f ops/compose.yaml logs -f

test:
	pytest

migrate:
	alembic upgrade head

backup:
	bash ops/scripts/backup_now.sh

restore:
	bash ops/scripts/restore_latest.sh

smoke:
	bash ops/scripts/smoke_test.sh
