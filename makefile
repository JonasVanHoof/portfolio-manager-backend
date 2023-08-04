include .env

list:
	@printf "\n"
	@printf "Open %s: %s\n" "project source code $(PROJECT_SOURCE_CODE)"
	@printf "\n"
	@printf "Open %s: %s\n" "Portfolio Manager" "$(APPLICATION_DOMAIN):4200"
	@printf "Open %s: %s\n" "resource COMPANIES" "$(APPLICATION_DOMAIN)/companies"
	@printf "Open %s: %s\n" "resource EMPLOYEES" "$(APPLICATION_DOMAIN)/employees"
	@printf "Open %s: %s\n" "resource PROJECTS" "$(APPLICATION_DOMAIN)/projects"
	@printf "\n"
	@printf "Open %s: %s\n" "virtuoso" "$(APPLICATION_DOMAIN):8890"
	@printf "\n"

build: 
	echo "Building docker compose"
	$(COMPOSE_EXECUTION_ALIAS) -f $(COMPOSE_FILE) build

start:
	echo "Running docker compose file"
	$(COMPOSE_EXECUTION_ALIAS) -f $(COMPOSE_FILE) up -d

down:
	$(COMPOSE_EXECUTION_ALIAS) down

logs:
	$(COMPOSE_EXECUTION_ALIAS) logs -f

# NOTE
# - als je wel graag ook specifiek build-dev en build-prod toch wilt hebben, kan je altijd expliciet docker compose --file FILE --file FILE2 command doen in je makefile