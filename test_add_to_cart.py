import unittest
from io import StringIO
import sys

from test_add_to_cart import Product, Cart

class TestProductAndCart(unittest.TestCase):

    def test_product_initialization(self):
        product = Product("Shirt", 19.99, 2)
        self.assertEqual(product.name, "Shirt")
        self.assertEqual(product.price, 19.99)
        self.assertEqual(product.quantity, 2)

    def test_cart_initialization(self):
        cart = Cart("John")
        self.assertEqual(cart.user_name, "John")
        self.assertEqual(cart.products, [])

    def test_add_to_cart(self):
        cart = Cart("John")
        product1 = Product("Shirt", 19.99, 2)
        product2 = Product("Jeans", 29.99, 1)

        cart.add_to_cart(product1)
        cart.add_to_cart(product2)

        self.assertEqual(len(cart.products), 2)
        self.assertEqual(cart.products[0].name, "Shirt")
        self.assertEqual(cart.products[0].price, 19.99)
        self.assertEqual(cart.products[0].quantity, 2)
        self.assertEqual(cart.products[1].name, "Jeans")
        self.assertEqual(cart.products[1].price, 29.99)
        self.assertEqual(cart.products[1].quantity, 1)

    def test_remove_from_cart(self):
        cart = Cart("John")
        product1 = Product("Shirt", 19.99, 2)
        product2 = Product("Jeans", 29.99, 1)

        cart.add_to_cart(product1)
        cart.add_to_cart(product2)
        cart.remove_from_cart("Shirt")

        self.assertEqual(len(cart.products), 1)
        self.assertEqual(cart.products[0].name, "Jeans")

        cart.remove_from_cart("Jeans")
        self.assertEqual(len(cart.products), 0)

    def test_display_cart(self):
        cart = Cart("John")
        product1 = Product("Shirt", 19.99, 2)
        product2 = Product("Jeans", 29.99, 1)

        cart.add_to_cart(product1)
        cart.add_to_cart(product2)

        captured_output = StringIO()
        sys.stdout = captured_output
        cart.display_cart()
        sys.stdout = sys.__stdout__

        expected_output = (
            "Cart Contents for John\n"
            "Product Information:\n"
            "Name: Shirt\n"
            "Price: 19.99\n"
            "Quantity: 2\n"
            "Product Information:\n"
            "Name: Jeans\n"
            "Price: 29.99\n"
            "Quantity: 1\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

        cart.remove_from_cart("Shirt")
        captured_output = StringIO()
        sys.stdout = captured_output
        cart.display_cart()
        sys.stdout = sys.__stdout__

        expected_output = (
            "Cart Contents for John\n"
            "Product Information:\n"
            "Name: Jeans\n"
            "Price: 29.99\n"
            "Quantity: 1\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

        cart.remove_from_cart("Jeans")
        captured_output = StringIO()
        sys.stdout = captured_output
        cart.display_cart()
        sys.stdout = sys.__stdout__

        expected_output = (
            "Cart Contents for John\n"
            "Cart is empty.\n"
        )
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
