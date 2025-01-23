from src.product import Product


def test_print_mixin(capsys):
    Product("phonei", "not iphone", 78900.0, 1)
    message = capsys.readouterr()
    assert message.out == 'Product, phonei, not iphone, 78900.0, 1\n'