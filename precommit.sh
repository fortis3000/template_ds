#!/usr/bin/env bash
export POETRY_PATH="poetry"

echo "List of changes fields comparing to master branch"
#git diff --stat master
export CHANGED_FILES=$(git diff --name-only --diff-filter=d master -- '***.py')

if [ -z "$CHANGED_FILES" ]; then
  echo "No Python files were changed, skipping linting"
  exit 0;
fi

echo
echo "Running isort import sorting"
${POETRY_PATH} run python -m isort -v --settings-file ./pyproject.toml $CHANGED_FILES

echo
echo "Running black formatting"
${POETRY_PATH} run python -m black -v $CHANGED_FILES

echo
echo "Running pylint linting"
${POETRY_PATH} run python -m pylint $CHANGED_FILES

echo
echo "Finished"