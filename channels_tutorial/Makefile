new-makemigrations:
	python3 manage.py makemigrations chat
	python3 manage.py makemigrations accounts
	python3 manage.py makemigrations

new-migrate:
	python3 manage.py migrate chat
	python3 manage.py migrate accounts
	python3 manage.py migrate

migrate:
	make makemigrations
	make migrate
