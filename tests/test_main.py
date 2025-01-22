import pytest

from main import Category, Product
from src.product import Smartphone, LawnGrass


def test_init(product_first_phone):
    """ Тестируем инициализацию нового продукта """
    assert product_first_phone.name == "phonei"
    assert product_first_phone.description == "not iphone"
    assert product_first_phone.price == 78900.0
    assert product_first_phone.quantity == 1


def test_new_product(for_test_new_product):
    assert for_test_new_product.name == "phonei over9000"
    assert for_test_new_product.description == "not a joke"
    assert for_test_new_product.price == 100500.0
    assert for_test_new_product.quantity == 3


def test_price(product_first_phone):
    product_first_phone.price = 100500.0
    assert product_first_phone.price == 100500.0


def test_price_invalid(product_first_phone):
    product_first_phone.price = 0.0
    assert product_first_phone.price == 78900.0


def test_category_init(category_calls):
    assert category_calls.name == "phones"
    assert category_calls.description == "phones for callsses"


def test_counters(category_calls):
    assert Category.product_count == 4
    assert Category.category_count == 2


def test_add_product_to_category():
    product1 = Product("a", "b", 1.0, 1)
    product2 = Product("c", "d", 2.0, 2)
    product3 = Product("e", "f", 3.0, 3)
    category = Category("abc", "def", [product1, product2, product3])
    product4 = Product("g", "i", 4.0, 4)
    category.add_product(product4)
    assert Category.product_count == 8


def test_products(one_category):
    assert one_category.products == (
        "a, b, 1.0 руб. Остаток: 1 шт.\n"
        "c, d, 2.0 руб. Остаток: 2 шт.\n"
        "e, f, 3.0 руб. Остаток: 3 шт.\n"
    )


def test_str_product(product_first_phone):
    assert str(product_first_phone) == "phonei, 78900.0 руб. Остаток: 1 шт."


def test_add_product(product_first_phone, for_test_new_product):
    assert product_first_phone + for_test_new_product == 380400.0


def test_invalid_add_product():
    with pytest.raises(TypeError):
        Category.add_product("Что-то не то")


def test_str_category(one_category):
    assert str(one_category) == "abc, колличество продуктов: 6"


def test_init_smartphone():
    phone_for_test = Smartphone("Samsung Galaxy S23 Ultra",
                                "256GB, Серый цвет," "200MP камера",
                                180000.0, 5, 95.5,
                                "S23 Ultra", 256, "Серый")
    assert phone_for_test.efficiency == 95.5
    assert phone_for_test.model == "S23 Ultra"
    assert phone_for_test.memory == 256
    assert phone_for_test.color == "Серый"


def test_init_lawn_grass():
    grass_for_test = LawnGrass("Газонная трава",
                               "Элитная трава для газона", 500.0, 20,
                               "Россия", "7 дней", "Зеленый")
    assert grass_for_test.country == "Россия"
    assert grass_for_test.germination_period == "7 дней"
    assert grass_for_test.color == "Зеленый"
