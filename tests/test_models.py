from models.product import Product

def test_product():
    p = Product(1, "A")
    assert p.name == "A"
