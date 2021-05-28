import unittest 

from app import app as flask_app

class Teste_index_route(unittest.TestCase):
    def setUp(self):
        app = flask_app.test_client()
        self.response_index = app.get("/")
        self.response_outra_rota = app.get("/outra-rota")

    def test_get_index(self):
        self.assertEqual(200, self.response_index.status_code)

    def test_get_outra_rota(self):
        self.assertEqual(200, self.response_outra_rota.status_code)
