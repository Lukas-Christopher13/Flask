from flask import url_for

from .test_case import FlaskAuthTestCase

class TestRegister(FlaskAuthTestCase):
   
    def test_deve_retornar_status_code_201(self):
        response = self.create_user()
        self.assertEqual(201, response.status_code)
    
    def test_login_invalid_email(self):
        self.create_user()
        response = self.client.post(url_for('api.login'), json={
            "email": "email_invalido",
            "password": "123"
        })

        data = response.get_json()

        self.assertEqual('invalid email', data['error'])
        self.assertEqual(401, response.status_code)
        
    def test_login_invalid_password(self):
        self.create_user()
        response = self.client.post(url_for('api.login'), json={
            "email": "teste96@gmail.com",
            "password": "senhar_incorreta"
        })

        data = response.get_json()

        self.assertEqual('invalid password', data['error'])
        self.assertEqual(401, response.status_code)
         
    def test_valid_login(self):
        self.create_user()
        response = self.client.post(url_for('api.login'), json={
            "email": "teste96@gmail.com",
            "password": "123"
        })

        self.assertEqual(200, response.status_code)

    def test_protected_rout_fail(self):
        response = self.client.get(url_for('api.protected'))
        data = response.get_json()
        self.assertEqual('Missing Authorization Header', data['msg'])
    
    def test_protected_rout(self):
        self.create_user()
        response = self.client.post(url_for('api.login'), json={
            "email": "teste96@gmail.com",
            "password": "123"
        })
        token = response.get_json()

        headers = {'Authorization': f'Bearer {token["access_token"]}'}

        response = self.client.get(url_for('api.protected'), headers=headers)

        self.assertEqual(200, response.status_code)
