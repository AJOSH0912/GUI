import tkinter as tk
from tkinter import ttk


products = [
    {"id": 1, "name": "Running Shoes", "price": 99.99, "image": "shoe.png", "description": "Comfortable running shoes for all levels."},
    {"id": 2, "name": "Basketball", "price": 29.99, "image": "basketball.png", "description": "Official size basketball."},
    # ... more products
]

class SportsStore(tk.Tk):
    # Add an indented block of code here
    pass
    # ... (rest of the code)

    def __init__(self):
        super().__init__()
        self.title("Online Sports Store")
        self.geometry("800x600")

        self.shopping_cart = []

        # Create main frames
        self.product_list_frame = ttk.Frame(self)
        self.product_details_frame = ttk.Frame(self)
        self.shopping_cart_frame = ttk.Frame(self)
        self.checkout_frame = ttk.Frame(self)

        self.product_list_frame.grid(row=0, column=0, sticky="nsew")
        self.product_details_frame.grid(row=0, column=1, sticky="nsew")
        self.shopping_cart_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.checkout_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        # Product list frame
        self.product_list = ttk.Treeview(self.product_list_frame)
        self.product_list["columns"] = ("name", "price")
        self.product_list.heading("name", text="Product Name")
        self.product_list.heading("price", text="Price")

        for product in products:
            self.product_list.insert("", "end", values=(product["name"], f"${product['price']:.2f}"))

        self.product_list.pack()

        # Product details frame
        self.product_image = ttk.Label(self.product_details_frame)
        self.product_name = ttk.Label(self.product_details_frame, text="")
        self.product_price = ttk.Label(self.product_details_frame, text="")
        self.product_description = ttk.Label(self.product_details_frame, text="")
        
        self.product_image.pack()
        self.product_name.pack()
        self.product_price.pack()
        self.product_description.pack()