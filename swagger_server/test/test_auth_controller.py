# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.auth_bancologin_body import AuthBancologinBody  # noqa: E501
from swagger_server.models.auth_salacode_body import AuthSalacodeBody  # noqa: E501
from swagger_server.models.createplayer_code_body import CreateplayerCodeBody  # noqa: E501
from swagger_server.models.invalid_username import InvalidUsername  # noqa: E501
from swagger_server.models.refresh_token import RefreshToken  # noqa: E501
from swagger_server.models.success_login import SuccessLogin  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthController(BaseTestCase):
    """AuthController integration test stubs"""

    def test_auth_banco_login_post(self):
        """Test case for auth_banco_login_post

        Permite logar como \"Banco\"
        """
        body = AuthBancologinBody()
        response = self.client.open(
            '/auth/banco-login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_create_player_code_post(self):
        """Test case for auth_create_player_code_post

        Cria um player
        """
        body = CreateplayerCodeBody()
        response = self.client.open(
            '/auth/create-player/{code}'.format(code='code_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_refresh_post(self):
        """Test case for auth_refresh_post

        Recebe um 'refresh_token' e retorna um token atualizado
        """
        body = RefreshToken()
        response = self.client.open(
            '/auth/refresh',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_auth_sala_code_post(self):
        """Test case for auth_sala_code_post

        Verifica se uma sala existe e retorna o seu codigo
        """
        body = AuthSalacodeBody()
        response = self.client.open(
            '/auth/sala-code',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
