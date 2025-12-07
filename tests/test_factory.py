from core.factory import Factory
from repositories.product_repo import ProductRepo

def test_factory():
    assert isinstance(Factory.get_product_repo(), ProductRepo)
