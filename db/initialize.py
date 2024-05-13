class ProductPriceTable:
    def __init__(self):
        self.table = {}
        self.add_product(id="A", price=10.28, part_name="LED screen")
        self.add_product(id="B", price=24.07, part_name="OLED screen")
        self.add_product(id="C", price=33.30, part_name="AMOLED screen")
        self.add_product(id="D", price=25.94, part_name="Wide-Angle Camera")
        self.add_product(id="E", price=32.39, part_name="Ultra-Wide-Angle Camera")
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

    def update_product(self, id, price=None, part_name=None):
        if id in self.table:
            if price is not None:
                self.table[id]['price'] = price
            if part_name is not None:
                self.table[id]['part'] = part_name
        else:
            print(f"Product with ID '{id}' does not exist.")

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

    def display_table(self):
        print("Product Price Table:")
        for id, product in self.table.items():
            print(f"ID: {id}, Price: {product['price']}, Part: {product['part']}")

# # Create an instance of the ProductPriceTable
# product_price_table = ProductPriceTable()


# # Display the product price table
# product_price_table.display_table()