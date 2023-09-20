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

up:
	docker compose up -d

# crie a imagem do container
docker-build:
	docker build -t guimas/ua:latest . --no-cache

# rode o container
docker-run:
	docker run -d --name test guimas/ua:latest

# acesse o container em execução
exec:
	docker exec -it test bash

or:
	open https://github.com/guimassoqueto/under-armour