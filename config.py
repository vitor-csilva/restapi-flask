import os

# Conexão com o Banco de dados
class DevConfig():

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'username': os.getenv('MONGODB_USERNAME'),
        'password': os.getenv('MONGODB_PASSWORD')
    }

class MockConfig:

    MONGODB_SETTINGS = {
        'db': 'users',
        'host': 'mongomock://localhost',
    }
