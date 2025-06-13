class ShoppingCart:
    def __init__(self):
        self.products = {}
        self.discount = 0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        if product_name in self.products:
            return False
        self.products[product_name] = {'price': price, 'quantity': quantity}
        return True

    def remove_product(self, product_name: str) -> bool:
        if product_name in self.products:
            del self.products[product_name]
            return True
        return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        if product_name in self.products:
            self.products[product_name]['quantity'] = new_quantity
            return True
        return False

    def get_products(self):
        return list(self.products.keys())

    def count_products(self) -> int:
        return sum(p['quantity'] for p in self.products.values())

    def get_total_price(self) -> int:
        total = sum(p['price'] * p['quantity'] for p in self.products.values())
        return total - int(total * self.discount)

    def apply_discount_code(self, discount_code: str) -> bool:
        if discount_code == "SAVE10":
            self.discount = 0.10
            return True
        return False

    def checkout(self) -> bool:
        if not self.products:
            return False
        self.products.clear()
        self.discount = 0
        return True
