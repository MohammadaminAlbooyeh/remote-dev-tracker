.PHONY: install run dev test lint migrate seed clean

install:
	pip install -r requirements.txt

run:
	uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

dev:
	uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest tests/ -v

lint:
	ruff check backend/ tests/

migrate:
	alembic upgrade head

seed:
	python scripts/seed_data.py

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
