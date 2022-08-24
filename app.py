# Realizando a importação do Framework flask
# jsonify: É uma função que vai converter a saídas para JSON para ser retornado ao browser
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse  # Flask-RESTful is an extension for Flask  that adds support for quickly building REST APIs. 
from flask_mongoengine import MongoEngine  # ORM utilizada para realizar a integração com o Banco de Dados

app = Flask(__name__)  # Start objeto, Criando a Aplicação Flask (Padrão encontrado na Doc)

app.config['MONGODB_SETTINGS'] = {  # Conexão com o Banco de dados
    'db': 'users',
    'port': 27017,
    'host': 'mongodb',
    'username': 'admin',
    'password': 'admin'
}

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name',
                           type=str,
                           required=True,
                           help="This field cannot be blank"
                           )

_user_parser.add_argument('last_name',
                           type=str,
                           required=True,
                           help="This field cannot be blank"
                           )

_user_parser.add_argument('cpf',
                           type=str,
                           required=True,
                           help="This field cannot be blank"
                           )

_user_parser.add_argument('email',
                           type=str,
                           required=True,
                           help="This field cannot be blank"
                           )

_user_parser.add_argument('birth_date',
                           type=str,
                           required=True,
                           help="This field cannot be blank"
                           )

api = Api(app)  # "app" significa o objeto da aplicação flask na qual será extendido para restfull api e o MongoEngine
db = MongoEngine(app)


class UserModel(db.Document):  # Declaração da Classe na qual irá se conectar com o Banco de Dados.
    cpf = db.StringField(required = True, unique = True)
    first_name = db.StringField(required = True)
    last_name = db.StringField(required = True)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required = True)


# Endpoint criados a partir do restfull para get and post no banco
class Users(Resource):  
    def get(self):
        # return jsonify(UserModel.objects())   Teste conexão Banco. 
        return {"message": "user 1"}

class User(Resource):
    def post(self):
        data = _user_parser.parse_args()
        UserModel(**data).save()
        #return data
        #return {"message": "teste"}

    def get(self, cpf):
        return {"message": "CPF"}

# Utilização das classes endpoints.
api.add_resource(Users, '/users') 
api.add_resource(User, '/user', '/user/<string:cpf>')

# Parte de execução do Script.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
