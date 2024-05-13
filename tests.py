import unittest
import threading
import requests
import json

# Import your Application class and other necessary modules
from http.server import HTTPServer
from app import Application 
from db.initialize import ProductPriceTable

class TestApplication(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server_thread = threading.Thread(target=cls.start_server)
        cls.server_thread.start()

    @classmethod
    def start_server(cls):
        server_address = ('localhost', 8000)
        cls.httpd = HTTPServer(server_address, Application)
        cls.httpd.serve_forever()

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()

    def test_do_POST_valid_request(self):
        data = {'components': ['component1', 'component2']}
        response = requests.post('http://localhost:8000/orders', json=data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn('order_id', response_data)
        self.assertIn('total', response_data)
        self.assertIn('parts', response_data)


    def test_do_POST_invalid_endpoint(self):
        response = requests.post('http://localhost:8000/invalid_endpoint')
        self.assertEqual(response.status_code, 404)
        response_data = response.json()
        self.assertIn('error', response_data)

if __name__ == '__main__':
    unittest.main()
