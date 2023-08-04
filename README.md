# Portfolio Manager

This project makes it possible to connect entities that have the company in common togheter. The entities are in relation with each other as for example. A company has employees working for them on different projects that company is realising. These projects are beeing created by the employees.

Entities that can be manipulated at this moment:

- Company
- Employee
- Project

## Project Setup

Created a small `makefile` that helps you setup and walk through the project. For this to work you have to create a `.env` file in the root folder and add following variables to it.

```yaml
PROJECT_SOURCE_CODE=<URL-TO-YOUR-CODE>

COMPOSE_FILE=./compose.yaml
COMPOSE_EXECUTION_ALIAS=docker-compose

APPLICATION_DOMAIN=http://localhost
```

List all urls that are used in the project

```bash
make list
```

Build the project with compose

```bash
make build
```

Start the project with compose

```bash
make start
```

Stop and remove all the project containers

```bash
make down
```

Show the project container logs

```bash
make logs
```
