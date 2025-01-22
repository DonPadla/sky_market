import pytest

from src.catalog import Category
from src.product import Product


@pytest.fixture
def product_first_phone():
    """ Добавляем продукт """
    return Product("phonei", "not iphone", 78900.0, 1)


@pytest.fixture
def category_calls(product_first_phone, for_test_new_product):
    return Category("phones", "phones for callsses", [
        product_first_phone, for_test_new_product
    ])


@pytest.fixture
def for_test_new_product():
    return Product("phonei over9000", "not a joke", 100500.0, 3)


@pytest.fixture
def one_category():
    product1 = Product("a", "b", 1.0, 1)
    product2 = Product("c", "d", 2.0, 2)
    product3 = Product("e", "f", 3.0, 3)
    category = Category("abc", "def", [product1, product2, product3])
    return category
