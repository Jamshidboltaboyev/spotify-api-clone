up:
	docker-compose up -d

down:
	docker-compose down

migrate:
	python3 manage.py makemigrations \
 	&& python3 manage.py migrate



.DEFAULT_GOAL:=up
