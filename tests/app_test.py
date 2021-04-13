import unittest 

from app import app as flask_app

class Teste_index_route(unittest.TestCase):
    def setUp(self):
        app = flask_app.test_client()
        self.response = app.get("/")

    def test_get_index(self):
        self.assertEqual(200, self.response.status_code)


