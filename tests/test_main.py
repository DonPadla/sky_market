import pytest

from main import Category, Product


@pytest.fixture
def product_first_phone():
    """ Добавляем продукт """
    return Product("phonei", "not iphone", 78900.0, 1)


def test_init(product_first_phone):
    """ Тестируем инициализацию нового продукта """
    assert product_first_phone.name == "phonei"
    assert product_first_phone.description == "not iphone"
    assert product_first_phone.price == 78900.0
    assert product_first_phone.quantity == 1


@pytest.fixture
def category_phones():
    """ Добавляем категорию """
    return Category("phones", "devices for calls", ["youphone", "phonei"])


def test_category(category_phones):
    """ Тестируем инициализацию новой категории """
    assert category_phones.name == "phones"
    assert category_phones.description == "devices for calls"
    assert category_phones.products == ["youphone", "phonei"]


@pytest.fixture
def category_calls():
    """ Добавляем еще три категории """
    category_1 = Category("a", "b", ["c", "d"])
    category_2 = Category("1", "2", ["3", "4"])
    category_3 = Category(".", ",", ["!", "?"])
    return category_1, category_2, category_3


def test_counters(category_calls):
    """ Тестируем счетчики """
    assert Category.product_count == 8  # "youphone" и "phonei" тоже тут
    assert Category.category_count == 4  # + "phones"
