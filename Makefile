APP = restapi-flask

test:
	@bandit -r . -x '*/.venv/*','*/tests/*'
	@black .
	@flake8 . --exclude .venv 
	@pytest -v --disable-warnings

compose:
	@docker-compose build
	@docker-compose up

setup-dev:
	@kind create cluster --config kubernetes/config/config.yaml
	@kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
	@kubectl wait --namespace ingress-nginx \
  		--for=condition=ready pod \
  		--selector=app.kubernetes.io/component=controller \
  		--timeout=270s
# bitnami/mongodb nao disponivel para computadores com chips ARM ate o momento. 
	@helm upgrade --install \
		--set auth.rootPassword="root" \
		--set image.tag=5.0.8 \
		mongodb kubernetes/charts/mongodb
	@kubectl wait \
		--for=condition=ready pod \
		--selector=app.kubernetes.io/component=mongodb \
		--timeout=270s

teardown-dev:
	@kind delete clusters kind 

deploy-dev:
	@docker build -t $(APP):latest .
	@kind load docker-image $(APP):latest
	@kubectl apply -f kubernetes/manifests
	@kubectl rollout restart deploy restapi-flask

dev: setup-dev deploy-dev

# heroku:
# 	@heroku container:login
# 	#O export abaixo só é necessário caso esteja utilizando MAC com Apple Silicon(M1 ou M2)
# 	@export DOCKER_DEFAULT_PLATFORM=linux/amd64  
# 	@heroku container:push -a $(APP) web
# 	@heroku container:release -a $(APP) web