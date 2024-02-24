from http import HTTPStatus

from . import TestAuthClass

class TestAuthBancoLogin(TestAuthClass):
    def test_banco_login(self):
        self.create_banco()
        request = self.client.post(
            "auth/banco-login", 
            json={
                "username": "test",
                "password": "123"
            }
        )

        self.assertEqual(200, request.status_code)
    
    def test_banco_invalid_username(self):
        self.create_banco()
        request = self.client.post(
            "auth/banco-login", 
            json={
                "username": "invalido",
                "password": "123"
            }
        )

        self.assertEqual(HTTPStatus.UNAUTHORIZED, request.status_code)

    def test_banco_invalid_password(self):
        self.create_banco()
        request = self.client.post(
            "auth/banco-login", 
            json={
                "username": "test",
                "password": "invalido"
            }
        )

        self.assertEqual(HTTPStatus.UNAUTHORIZED, request.status_code)
    
    def test_logar_in_banco_with_a_player_jwt(self):
        pass

