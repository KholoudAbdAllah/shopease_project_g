from models.product import Product

class ProductRepo:
    def get_product(self):
        return Product(1, "Test Product")
