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

docker-build:
	docker build -t guimas/ua:latest . -f dev.Dockerfile --no-cache

docker-run:
	docker run -d --name test guimas/ua:latest

exec:
	docker exec -it test bash