.PHONY: install lint format typecheck test test-eval clean build all

# --- Python ---
PYTHON := python3
UV_PIP := uv pip
VENV := .venv

install:
	$(UV_PIP) install -e ".[dev]"

lint:
	ruff check .

format:
	ruff format .

typecheck:
	mypy src/ app.py pages/ utils.py

test:
	pytest tests/ -v --tb=short

test-eval:
	pytest tests/test_eval.py -v --tb=short

test-cov:
	pytest tests/ -v --cov=src --cov-report=term-missing

clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache .ruff_cache
	rm -rf build/ dist/ *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

build:
	$(PYTHON) -m build

all: lint format typecheck test
	@echo "=== All checks passed ==="
