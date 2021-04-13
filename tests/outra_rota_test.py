
from app import app as flaskapp

from unittest import TestCase


class Teste_outra_rota(TestCase):
    def setUp(self):
        app = flaskapp.test_client()
        self.response = app.get('/outra_rota')

    def teste_outra_rota(self):
        self.assertEqual(200, self.response.status_code)


