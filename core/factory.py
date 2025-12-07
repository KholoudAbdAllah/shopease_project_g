from repositories.product_repo import ProductRepo

class Factory:
    @staticmethod
    def get_product_repo():
        return ProductRepo()
