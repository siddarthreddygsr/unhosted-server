import unittest
import threading
import http.client
import json
from http.server import HTTPServer
from app import Application


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
        data = {'components': ["A", "F", "I", "D", "K"]}
        conn = http.client.HTTPConnection('localhost', 8000)
        headers = {'Content-type': 'application/json'}
        conn.request('POST', '/orders', json.dumps(data), headers)
        response = conn.getresponse()

        self.assertEqual(response.status, 200)
        response_data = json.loads(response.read().decode('utf-8'))
        self.assertIn('order_id', response_data)
        self.assertEqual(response_data['total'], 142.3)
        self.assertEqual(
            response_data['parts'], [
                'LED screen',
                'USB-C Port',
                'Android OS',
                'Wide-Angle Camera',
                'Metallic Body'
            ])

    def test_do_POST_invalid_endpoint(self):
        conn = http.client.HTTPConnection('localhost', 8000)
        conn.request('POST', '/invalid_endpoint')
        response = conn.getresponse()

        self.assertEqual(response.status, 404)
        response_data = json.loads(response.read().decode('utf-8'))
        self.assertIn('error', response_data)


if __name__ == '__main__':
    unittest.main()
