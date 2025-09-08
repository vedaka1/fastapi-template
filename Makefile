DC = docker compose
DEV = docker-compose.yml
PROD = docker-compose.prod.yml

dev:
	$(DC) -f $(DEV) up -d --build

prod:
	$(DC) -f $(PROD) up -d --build

down:
	$(DC) -f $(DEV) down

logs:
	$(DC) -f $(DEV)  logs | tail -50