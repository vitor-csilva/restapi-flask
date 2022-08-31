# ORM utilizada para realizar a integração com o Banco de Dados
from flask_mongoengine import MongoEngine

# Cria uma instância do mongoEngine.
db = MongoEngine()


# Função utilizada para iniciar a aplicação flask.
def init_db(app):
    db.init_app(app)
