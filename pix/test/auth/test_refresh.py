from . import TestAuthClass
from http import HTTPStatus

class TestRefresh(TestAuthClass):
    def test_refresh_banco_token(self):
        tokens = self.get_banco_tokens()

        refresh_token = tokens["refresh_token"]

        response = self.client.post("/auth/refresh", 
        headers={
            "Authorization": f"Bearer {refresh_token}"
        })

        self.assertEqual(HTTPStatus.OK, response.status_code) 
    
    def test_refresh_banco_token_by_passing_wrong_token(self):
        tokens = self.get_banco_tokens()

        token = tokens["access_token"]

        response = self.client.post("/auth/refresh", 
        headers={
            "Authorization": f"Bearer {token}"
        })

        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)

    def test_refresh_player_token(self):
        tokens = self.get_player_token()
        refresh_token = tokens["refresh_token"]

        response = self.client.post("/auth/refresh",
            headers={
                "Authorization": f"Bearer {refresh_token}"
            })
        
        self.assertEqual(HTTPStatus.OK, response.status_code)
    
    def test_refresh_player_by_passing_wrong_token(self):
        tokens = self.get_player_token()

        token = tokens["access_token"]

        response = self.client.post("/auth/refresh", 
        headers={
            "Authorization": f"Bearer {token}"
        })

        self.assertEqual(HTTPStatus.UNPROCESSABLE_ENTITY, response.status_code)
        

        


