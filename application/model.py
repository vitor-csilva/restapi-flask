from .db import db


# Declaração da Classe do Banco de Dados, fazendo o esquema de dados do Banco.
class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required=True)


class HealthCheckModel(db.Document):
    status = db.StringField(required=True)
