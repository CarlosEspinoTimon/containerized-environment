backend=$(shell docker-compose ps -q backend)


# Init
init:
	docker-compose up

# Build
build:
	docker-compose build

# Init the debuger
debug-backend:
	export FLASK_DEBUG=1 && docker-compose -f docker-compose.debug.yaml up

# Access backend
access-backend:
	docker exec -it $(backend) sh

# Install a module
# usage --> make backend-install-module module="MODULE NAME"
backend-install-module:
	docker exec -t $(backend) pipenv install '$(module)'

# Run the tests
backend-tests:
	docker exec -t $(backend) pipenv run python tests/tests.py

# Run only one test
# usage --> make backend-one-test test="TEST NAME"
backend-one-test:
	docker exec -t $(backend) pipenv run python tests/tests.py '$(test)'

# Init database
db-init:
	docker exec -t $(backend) pipenv run flask db init

# Generate database migrations
db-migrate:
	docker exec -t $(backend) pipenv run flask db migrate -m '$(comment)'

# Merge two heads
db-merge:
	docker exec -t $(backend) pipenv run alembic -c migrations/alembic.ini merge heads

# Apply database upgrade
db-upgrade:
	docker exec -t $(backend) pipenv run flask db upgrade

# Apply database downgrade
db-downgrade:
	docker exec -t $(backend) pipenv run flask db downgrade



