# Ferramenta para realização de testes unitários.
import pytest
from application import create_app


class TestApplication():

    @pytest.fixture
    def client(self):
        app = create_app('config.MockConfig')
        return app.test_client()
    
    @pytest.fixture
    def valid_user(self):
        return {
            "first_name": "Vitor",
            "last_name": "Costa",
            "cpf": "783.097.581-70",
            "email": "vitorcs.contato@gmail.com", 
            "birth_date": "1998-07-22"
        }

    @pytest.fixture
    def invalid_user(self):
        return {
            "first_name": "Vitor",
            "last_name": "Costa",
            "cpf": "783.097.581-77",
            "email": "vitorcs.contato@gmail.com", 
            "birth_date": "1998-07-22"
        }

    def test_get_users(self, client):
        response = client.get('/users')
        assert response.status_code == 200

    def test_post_user(self, client, valid_user, invalid_user):
        response = client.post('/user', json=valid_user)
        assert response.status_code == 200
        assert b"successfully" in response.data

        response = client.post('/user', json=invalid_user)
        assert response.status_code == 400
        assert b"invalid" in response.data
