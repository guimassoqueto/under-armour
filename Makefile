# install all dependencies
i: 
	poetry shell && poetry install

# install pre-commit, update its dependencies and install hook for commit messages
pc:
	pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg

env:
	cp .env.sample .env

a:
	poetry run python main.py