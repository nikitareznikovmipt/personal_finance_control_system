PROJECT:=app
TESTS:=test
VENV:=.venv

setup:
	poetry install --no-root
	poetry config virtualenvs.in-project true
	poetry check

clean:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf $(VENV)

# Format

isort_fix: .venv
	poetry run isort $(PROJECT) $(TESTS)


black_fix:
	poetry run black $(PROJECT) $(TESTS)

format: isort_fix black_fix

isort: .venv
	poetry run isort --check $(PROJECT) $(TESTS)

.black:
	poetry run black --check --diff $(PROJECT) $(TESTS)

flake: .venv
	poetry run flake8 $(PROJECT) $(TESTS)

mypy: .venv
	poetry run mypy $(PROJECT) $(TESTS)

pylint: .venv
	poetry run pylint $(PROJECT) $(TESTS)

lint: isort flake mypy pylint

# Test

test:
	poetry run pytest $(TESTS)


# Docker


