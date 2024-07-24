products = [
    {"id": 1, "name": "Running Shoes", "price": 99.99, "image": "shoe.png", "description": "Comfortable running shoes for all levels."},
    {"id": 2, "name": "Basketball", "price": 29.99, "image": "basketball.png", "description": "Official size basketball."},
    # ... more products
]

class SportsStore(tk.Tk):
    # ... (rest of the code)

    def __init__(self):
        # ... (rest of the code)

        self.shopping_cart = []

    def add_to_cart(self, product_id):
        product = next((p for p in self.products if p["id"] == product_id), None)
        if product:
            self.shopping_cart.append(product)
            # Update shopping cart display

    def remove_from_cart(self, product_id):
        self.shopping_cart = [p for p in self.shopping_cart if p["id"] != product_id]
        # Update shopping cart display