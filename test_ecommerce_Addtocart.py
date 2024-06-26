import unittest
from test_ecommerce_Addtocart import Product, Cart  # Ensure this path is correct

class TestProductAndCart(unittest.TestCase):

    def test_product_initialization(self):
        product = Product("Apple", 1.0, 3)
        self.assertEqual(product.name, "Apple")
        self.assertEqual(product.price, 1.0)
        self.assertEqual(product.quantity, 3)

    def test_cart_initialization(self):
        cart = Cart("John Doe")
        self.assertEqual(cart.user_name, "John Doe")
        self.assertEqual(cart.products, [])

    def test_add_to_cart(self):
        cart = Cart("John Doe")
        product = Product("Apple", 1.0, 3)
        cart.add_to_cart(product)
        self.assertEqual(len(cart.products), 1)
        self.assertEqual(cart.products[0].name, "Apple")
        self.assertEqual(cart.products[0].price, 1.0)
        self.assertEqual(cart.products[0].quantity, 3)

        # Adding the same product should increase its quantity
        cart.add_to_cart(Product("Apple", 1.0, 2))
        self.assertEqual(len(cart.products), 1)
        self.assertEqual(cart.products[0].quantity, 5)

        # Adding a different product
        cart.add_to_cart(Product("Banana", 0.5, 5))
        self.assertEqual(len(cart.products), 2)
        self.assertEqual(cart.products[1].name, "Banana")
        self.assertEqual(cart.products[1].price, 0.5)
        self.assertEqual(cart.products[1].quantity, 5)

    def test_remove_from_cart(self):
        cart = Cart("John Doe")
        cart.add_to_cart(Product("Apple", 1.0, 3))
        cart.add_to_cart(Product("Banana", 0.5, 5))

        cart.remove_from_cart("Apple")
        self.assertEqual(len(cart.products), 1)
        self.assertEqual(cart.products[0].name, "Banana")

        cart.remove_from_cart("Banana")
        self.assertEqual(len(cart.products), 0)

    def test_display_cart(self):
        cart = Cart("John Doe")
        cart.add_to_cart(Product("Apple", 1.0, 3))
        cart.add_to_cart(Product("Banana", 0.5, 5))

        

if __name__ == '__main__':
    unittest.main()
