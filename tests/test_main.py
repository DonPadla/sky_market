from main import Category, Product


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
