#!/usr/bin/env bash

:"
VINCENT Nicolas

Création d'une architecture de projet dans le répertoire courant.

USAGE:
  bash create_python_project.sh <project_name>

  pipenv run black
  pipenv run isort
  pipenv run flake8
  pipenv run pytest
  pipenv run pytest --cov --cov-fail-under=100

  git commit/push --no-verify

from https://sourcery.ai/blog/python-best-practices/
"

echo $(python3.6 --version)

project_name="$1"
repo_name="$2"

# Installation de pipx s'il ne l'est pas déjà
python3.6 -m pip install --user pipx
python3.6 -m pipx ensurepath

# Enter the project name and repo name
echo "$project_name
$repo_name
" | python3.6 -m pipx run --no-cache cookiecutter gh:sourceryai/python-best-practices-cookiecutter

# Enter project directory
cd $repo_name

# Initialise git repo
git init

# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
