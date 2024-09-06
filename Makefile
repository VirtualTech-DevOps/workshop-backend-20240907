install:
	poetry install --no-root

start:
	poetry run uvicorn api.main:app --reload

test:
	pytest -vv

ci-test:
	poetry run pytest --cov=. --cov-branch --cov-report=xml:reports/pytest/coverage.xml

dev-migrate:
	poetry run python -m api.migrate_db

new-migrate:
	poetry run alembic revision --autogenerate -m "${MESSAGE}"

migrate:
	poetry run alembic upgrade head

psql:
	psql -h db -U postgres

format-check:
	black --check .
