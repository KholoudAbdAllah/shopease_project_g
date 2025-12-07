from repositories.product_repo import ProductRepo

def test_repo():
    repo = ProductRepo()
    assert repo.get_product().id == 1
