from http import HTTPStatus

from . import TestSalaClass

class TestSalaClass(TestSalaClass):
    def test_get_sala(self):
        self.create_sala()
        self.create_player()

        response = self.client.get(f"/sala/{self.sala.code}")

        self.assertEqual(HTTPStatus.OK, response.status_code)