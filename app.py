from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import uuid
from db.initialize import ProductPriceTable
import pdb

product_price_table = ProductPriceTable()
class Application(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == '/orders':
            pdb.set_trace()
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)

            total_price = 0
            parts = []
            order_id = uuid.uuid4().hex
            if 'components' in data:
                for component in data['components']:
                    product = product_price_table.get_product(component)
                    if product:
                        total_price += product['price']
                        parts.append(product['part'])

            total_price = round(total_price, 2)

            response = {
                "order_id": order_id,
                "total": total_price,
                "parts": parts
            }

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'invalid endpoint'}).encode())

def run(server_class=HTTPServer, handler_class=Application, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()