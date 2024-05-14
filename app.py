from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import uuid
from db.initialize import ProductPriceTable, OrdersTable
product_price_table = ProductPriceTable()
orders_table = OrdersTable()


class Application(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_valid_ids(self, ids):
        id_set = set(ids)
        return (
            (len(id_set & {'A', 'B', 'C'}) == 1 and
             len(id_set & {'D', 'E'}) == 1 and
             len(id_set & {'F', 'G', 'H'}) == 1 and
             len(id_set & {'I', 'J'}) == 1 and
             len(id_set & {'K', 'L'}) == 1)
        )

    def do_POST(self):
        if self.path == '/orders':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            INVALID_CHOICE = {"error": "invalid choice of parts"}
            total_price = 0
            parts = []
            order_id = uuid.uuid4().hex
            if 'components' in data:
                if len(data['components']) != 5:
                    response = INVALID_CHOICE
                if not self.is_valid_ids(data['components']):
                    response = INVALID_CHOICE
                else:
                    for component in data['components']:
                        product = product_price_table.get_product(component)
                        if product:
                            total_price += product['price']
                            parts.append(product['part'])
                    total_price = round(total_price, 2)
                    if len(parts) != 5:
                        response = INVALID_CHOICE
                    else:
                        response = {
                            "order_id": order_id,
                            "total": total_price,
                            "parts": parts
                        }
                    orders_table.add_entry(
                        order_id=order_id,
                        total_price=total_price,
                        parts=parts,
                    )
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(
                {
                    'error': 'invalid endpoint'
                }).encode())

    def do_GET(self):
        if self.path == "/get_orders":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = orders_table.show_data()
            self.wfile.write(json.dumps(data).encode())


def run(server_class=HTTPServer, handler_class=Application, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()


if __name__ == '__main__':
    run()
