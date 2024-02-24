from . import TestBancoClass
from app.repository.sala_repository import SalaRepository

EXPECTED_PLAYER = {
    "username": "test",
    "money": 1500000,
    "sala_code": "1234"
}

class TestBancoViews(TestBancoClass):
    def test_criar_sala(self):
        response = self.client.post(
            "/banco/criar_sala", 
            headers=self.get_autorization_header(),
            json={
                "code": "1234"
            }
        )
        
        json_response = response.get_json()

        self.assertEqual("sala criada!", json_response["msg"])
        self.assertEqual(201, response.status_code)

    def test_criar_sala_sala_ja_criada(self):
        self.create_sala()
        response = self.client.post(
            "banco/criar_sala", 
            headers=self.get_autorization_header(),
        json={
            "code": "1234"
        })

        json_response = response.get_json()

        self.assertEqual("essa sala já foi criada!", json_response["msg"])
        self.assertEqual(401, response.status_code)

    
    def test_deletar_sala(self):
        self.create_sala()

        sala_code = "1234"

        response = self.client.delete(
            f"/banco/deletar_sala/{sala_code}", 
            headers=self.get_autorization_header()
        )

        json_response = response.get_json()
        
        self.assertEqual("sala deletada", json_response["msg"])
        self.assertEqual(200, response.status_code)
    
    def test_listar_salas(self):
        self.create_salas()

        response = self.client.get(
            "/banco/listar_salas", 
            headers=self.get_autorization_header()
        )

        self.assertEqual(200, response.status_code)

    def test_get_player(self):
        self.create_player()
        username = "test"

        response = self.client.get(
            f"/banco/get_player/{username}",
            headers=self.get_autorization_header()
        )

        json_response = response.get_json()

        self.assertEqual(200, response.status_code)
        self.assertEqual(EXPECTED_PLAYER, json_response)
    
    def test_get_none_player(self):
        self.create_player()
        invalid_username = "invalid_test"

        response = self.client.get(
            f"/banco/get_player/{invalid_username}",
            headers=self.get_autorization_header()
        )
      
        json_response = response.get_json()
              
        self.assertEqual("player não cadastrado", json_response["msg"])
    
    def test_start_players_insuficientes(self):
        self.create_player()
        sala_code = "1234"

        requeste = self.client.post(
            f"/banco/start/{sala_code}",
            headers=self.get_autorization_header()
        )

        json_response = requeste.get_json()
        self.assertEqual("jogadores insuficientes", json_response["msg"])