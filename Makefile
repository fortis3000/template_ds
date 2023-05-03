.PHONY: precommit requirements_lint

POETRY_PATH = /home/user/.local/bin/poetry
PYTHON_FILES = **/*.py *.py

# Install linting requirements
requirements_lint:
	${POETRY_PATH} install --only codestyle

# Local precommit
precommit: requirements_lint
	${POETRY_PATH} run isort -v --settings-file ./pyproject.toml ${PYTHON_FILES}
	${POETRY_PATH} run black -v ${PYTHON_FILES}
	${POETRY_PATH} run pylint ${PYTHON_FILES}