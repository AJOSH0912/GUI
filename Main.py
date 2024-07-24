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

class SportsStore(tk.Tk):
    # ... (rest of the code)

    def checkout(self):
        total_price = sum(p["price"] for p in self.shopping_cart)
        # Display order summary
        # Process payment (integrate with payment gateway)
        # Clear shopping cart

class SportsStore(tk.Tk):
    # ... (rest of the code)

    def search(self, query):
        # Filter products based on query
        search_results = [p for p in self.products if query.lower() in p["name"].lower()]
        # Update product list display

class SportsStore(tk.Tk):
    # ... (rest of the code)

    def login(self, username, password):
        # Authenticate user
        # Store user information (session or database)

        def register(self, username, password, email):
        # Create new user account