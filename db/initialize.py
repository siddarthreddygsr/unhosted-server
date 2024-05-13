
class ProductPriceTable:
    def __init__(self):
        self.table = {}
        self.add_product(id="A", price=10.28, part_name="LED screen")
        self.add_product(id="B", price=24.07, part_name="OLED screen")
        self.add_product(id="C", price=33.30, part_name="AMOLED screen")
        self.add_product(id="D", price=25.94, part_name="Wide-Angle Camera")
        self.add_product(
            id="E",
            price=32.39,
            part_name="Ultra-Wide-Angle Camera")
        self.add_product(id="F", price=18.77, part_name="USB-C Port")
        self.add_product(id="G", price=15.13, part_name="Micro-USB Port")
        self.add_product(id="H", price=20.00, part_name="Lightning Port")
        self.add_product(id="I", price=42.31, part_name="Android OS")
        self.add_product(id="J", price=45.00, part_name="iOS OS")
        self.add_product(id="K", price=45.00, part_name="Metallic Body")
        self.add_product(id="L", price=30.00, part_name="Plastic Body")

    def add_product(self, id, price, part_name):
        if id not in self.table:
            self.table[id] = {'price': price, 'part': part_name}
        else:
            print(f"Product with ID '{id}' already exists.")

    def remove_product(self, id):
        if id in self.table:
            del self.table[id]
        else:
            print(f"Product with ID '{id}' does not exist.")

    def get_product(self, id):
        if id in self.table:
            return self.table[id]
        else:
            return None


class OrdersTable:
    def __init__(self):
        self.table = {}

    def add_entry(self, order_id, total_price, parts):
        if order_id not in self.table:
            self.table[order_id] = {'total': total_price, 'parts': parts}
        else:
            print(f"Entry with ID '{id}' already exists.")

    def show_data(self):
        return self.table

    def get_product(self, id):
        if id in self.table:
            return self.table[id]
        else:
            return None
