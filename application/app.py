# Realizando a importação do Framework flask
# jsonify: É uma função que vai converter a saídas para JSON para ser retornado ao browser
from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse  # Flask-RESTful is an extension for Flask  that adds support for quickly building REST APIs. 

from mongoengine import NotUniqueError
import re  # Regular Expression  

# Start objeto, Criando a Aplicação Flask (Padrão encontrado na Doc)
app = Flask(__name__)  

# Conexão com o Banco de dados
app.config['MONGODB_SETTINGS'] = {  
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

# "app" significa o objeto da aplicação flask na qual será extendido para restfull api e o MongoEngine
api = Api(app)





# Endpoint criados a partir do restfull para get and post no banco
class Users(Resource):  
    def get(self):
        return jsonify(UserModel.objects())  # Teste conexão Banco. 
        #return {"message": "user 1"}

class User(Resource):

    def validate_cpf(self, cpf):

        # Has the correct mask?
        if not re.match(r'\d{3}\.\d{3}\.\d{3}.\d{2}', cpf):
            return False

        # Grab only numbers
        numbers = [int(digit) for digit in cpf if digit.isdigit()]

        # Dows it have 11 digits ?
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        # Validate first digit after -
        sum_of_products = sum(a*b for a, b in zip(numbers[0:9],
                                                  range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        # Validate second digit after -
        sum_of_products = sum(a*b for a, b in zip(numbers[0:10],
                                                  range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    def post(self):
        data = _user_parser.parse_args()
        
        if not self.validate_cpf(data["cpf"]):
            return {"message": "CPF is invalid!"}, 400
        
        try: 
            response = UserModel(**data).save()
            return {"message": "User %s succefully created!" % response.id}
        except NotUniqueError:
            return {"message": "CPF already exists in database!"}, 400
        #return data
        #return {"message": "teste"}

    def get(self, cpf):
        response = UserModel.objects(cpf=cpf)

        if response:
            return jsonify(response)

        return {"message": "User does not exist in database!"}, 400

# Utilização das classes endpoints.
api.add_resource(Users, '/users') 
api.add_resource(User, '/user', '/user/<string:cpf>')

# Parte de execução do Script.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")