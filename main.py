class Product:
    """ Класс для работы с информацией о продукте """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """ Функция инициализации продукта"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_element):
        """ Создает объект класса из словаря """

        name = new_element["name"]
        description = new_element["description"]
        price = new_element["price"]
        quantity = new_element["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self):
        """ Возвращает приватный атрибут "price" """

        return self.__price

    @price.setter
    def price(self, cost):
        """ Проверяет "price" на положительность """

        if cost <= 0:
            print("Цена не должна быть нулевая или отрицательная")

        else:
            self.__price = cost

    def __str__(self):
        """ Выводит строку с именем, ценой и колличеством продукта """

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Возвращает сумму продуктов """

        return self.__price * self.quantity + other.__price * other.quantity


class Category:
    """ Класс для работы с категориями """

    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list

    def __init__(self, name, description, products):
        """ Функция инициализации категории """

        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def add_product(self, product: Product):
        """ Метод добавляющий новый продукт """

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1

        else:
            print("Не является объектом класса \"Product\"")

    @property
    def products(self):

        """ Возвращает строку с описанием всех продуктов в категории """
        product_str = ""
        for element in self.__products:
            product_str += \
                f"""{element.name}, {element.description}, {
                element.price} руб. Остаток: {element.quantity} шт.\n"""
        return product_str

    def __str__(self):
        """ Возвращает имя категории и колличество продуктов """

        amount = 0
        for element in self.__products:
            amount += element.quantity

        return f"{self.name}, колличество продуктов: {amount}"


if __name__ == '__main__':
    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5)
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8)
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        """Смартфоны, как средство не только коммуникации,"
         но и получения дополнительных функций для удобства жизни""",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
