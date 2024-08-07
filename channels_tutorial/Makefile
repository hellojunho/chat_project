# Define variables
PYTHON = python3

# Define targets
new-makemigrations:
	$(PYTHON) manage.py makemigrations chat
	$(PYTHON) manage.py makemigrations accounts
	$(PYTHON) manage.py makemigrations

new-migrate:
	$(PYTHON) manage.py migrate chat
	$(PYTHON) manage.py migrate accounts
	$(PYTHON) manage.py migrate

migrate: new-makemigrations new-migrate
