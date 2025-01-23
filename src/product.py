from src.base_product import BaseProduct
from src.print_mixin import MixinLog


class Product(MixinLog, BaseProduct):
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
        super().__init__()

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

        if type(other) is self.__class__:
            return (self.__price * self.quantity +
                    other.__price * other.quantity)

        else:
            raise TypeError


class Smartphone(Product):
    """ Класс со смартфонами """

    efficiency = str
    model = str
    memory = int
    color = str

    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)

        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """ Класс с травой """

    country = str
    germination_period = str
    color = str

    def __init__(self, name, description, price, quantity,
                 counry, germenation_period, color):
        super().__init__(name, description, price, quantity)

        self.country = counry
        self.germination_period = germenation_period
        self.color = color
