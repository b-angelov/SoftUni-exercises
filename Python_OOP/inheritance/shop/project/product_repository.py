from project.product import Product

class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        product = [product for product in self.products if product.name == product_name]
        if product:
            return product[0]

    def remove(self, product_name):
        product = [product for product in self.products if product.name == product_name]
        if product:
            self.products.remove(product[0])

    def __repr__(self):
        return '\n'.join(f"{product.name}: {product.quantity}" for product in self.products)
