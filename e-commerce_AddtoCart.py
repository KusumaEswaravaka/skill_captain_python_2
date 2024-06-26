class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

   
    def __str__(self):
        return f"{self.name} - ${self.price:.2f} x {self.quantity}"

class Cart:
    def __init__(self, user_name):
        self.user_name = user_name
        self.products = []

    def add_to_cart(self, product):
        # Check if the product already exists in the cart
        for p in self.products:
            if p.name == product.name:
                p.quantity += product.quantity
                break
        else:
            self.products.append(product)

    def remove_from_cart(self, product_name):
        self.products = [p for p in self.products if p.name != product_name]

    def display_cart(self):
        if not self.products:
            print("Cart is empty.")
        else:
            print(f"{self.user_name}'s Cart contents:")
            for product in self.products:
                print(product)

# Sample usage
# Uncomment the following lines to test the code
cart = Cart("John Doe")
cart.add_to_cart(Product("Apple", 1.0, 3))
cart.add_to_cart(Product("Banana", 0.5, 5))
cart.add_to_cart(Product("Apple", 1.0, 2))
cart.display_cart()
cart.remove_from_cart("Banana")
cart.display_cart()
