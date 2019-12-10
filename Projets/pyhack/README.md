
# pyhack

## Setup
```sh
# Install dependencies
pipenv install --dev

# Setup pre-commit and pre-push hooks
pipenv run pre-commit install -t pre-commit
pipenv run pre-commit install -t pre-push
```

## Tools
Liste des commandes :
```sh
black, isort, flake8, pytest, pytest --cov --cov-fail-under=100
```
```sh
pipenv run <command>

git commit/push --no-verify
```

## Profiling
TODO: refactor pyhack.py to profile only the map creation.
```sh
bash performances.sh perf.prof pyhack.py
```
