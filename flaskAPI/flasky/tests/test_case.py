import unittest

from flask import url_for

from app import create_app, db

class FlaskAuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)
        self.user = None

    def tearDown(self):
        db.session.rollback()
        db.drop_all()
        self.app_context.pop()

    def create_user(self):
        if self.user is None:
            self.user = self.client.post(url_for('api.register'),json={
                "email": "teste96@gmail.com",
                "username": "fulano123567579",
                "password": "123"
            })
        return self.user