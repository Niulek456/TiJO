import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_product(self):
        result = self.cart.add_product("Apple", 3, 5)
        self.assertTrue(result)
        self.assertIn("Apple", self.cart.products)

    def test_add_existing_product(self):
        self.cart.add_product("Apple", 3, 5)
        result = self.cart.add_product("Apple", 3, 5)
        self.assertFalse(result)

    def test_remove_product(self):
        self.cart.add_product("Banana", 2, 3)
        result = self.cart.remove_product("Banana")
        self.assertTrue(result)
        self.assertNotIn("Banana", self.cart.products)

    def test_remove_nonexistent_product(self):
        result = self.cart.remove_product("Orange")
        self.assertFalse(result)

    def test_update_quantity(self):
        self.cart.add_product("Milk", 4, 2)
        result = self.cart.update_quantity("Milk", 5)
        self.assertTrue(result)
        self.assertEqual(self.cart.products["Milk"]["quantity"], 5)

    def test_update_nonexistent_product(self):
        result = self.cart.update_quantity("Water", 10)
        self.assertFalse(result)

    def test_get_products(self):
        self.cart.add_product("X", 1, 1)
        self.cart.add_product("Y", 2, 2)
        names = self.cart.get_products()
        self.assertListEqual(sorted(names), ["X", "Y"])

    def test_count_products(self):
        self.cart.add_product("A", 1, 2)
        self.cart.add_product("B", 2, 3)
        self.assertEqual(self.cart.count_products(), 5)

    def test_get_total_price_no_discount(self):
        self.cart.add_product("A", 10, 2)
        self.cart.add_product("B", 5, 4)
        self.assertEqual(self.cart.get_total_price(), 10*2 + 5*4)

    def test_apply_discount_code_valid(self):
        self.cart.add_product("A", 100, 1)
        self.cart.apply_discount_code("SAVE10")
        self.assertEqual(self.cart.get_total_price(), 90)

    def test_apply_discount_code_invalid(self):
        result = self.cart.apply_discount_code("BADCODE")
        self.assertFalse(result)

    def test_checkout_success(self):
        self.cart.add_product("A", 1, 1)
        result = self.cart.checkout()
        self.assertTrue(result)
        self.assertEqual(len(self.cart.products), 0)

    def test_checkout_empty_cart(self):
        result = self.cart.checkout()
        self.assertFalse(result)

    def tearDown(self):
        self.cart = None

if __name__ == "__main__":
    unittest.main()
