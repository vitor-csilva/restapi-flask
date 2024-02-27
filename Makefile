APP = comunidadedevops-restapi

test:
	@black .
	@flake8 . --exclude .venv 
	@pytest -v --disable-warnings

compose:
	@docker-compose build
	@docker-compose up

heroku:
	@heroku container:login
	#O export abaixo só é necessário caso esteja utilizando MAC com Apple Silicon(M1 ou M2)
	@export DOCKER_DEFAULT_PLATFORM=linux/amd64  
	@heroku container:push -a $(APP) web
	@heroku container:release -a $(APP) web