from flask import Flask
from flask_restful import Api
from .db import init_db
from .app import User, Users


# app, Start objeto, Criando a Aplicação Flask (Padrão encontrado na Doc)
# api, "app" significa o objeto da aplicação flask na qual será extendido para restfull api e o MongoEngine
def create_app(config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config)
    init_db(app)

    # Utilização das classes endpoints.
    api.add_resource(Users, '/users')
    api.add_resource(User, '/user', '/user/<string:cpf>')
    return app
