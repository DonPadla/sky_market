from src.product import Product


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
            raise TypeError
            # print("Не является объектом класса \"Product\"")

    @property
    def products(self):
        """ Возвращает строку с описанием всех продуктов в категории """

        product_str = ""
        for element in self.__products:
            product_str += f"""{
                                element.name}, {element.description}, {
                                element.price} руб. Остаток: {
                                element.quantity} шт.\n"""
        return product_str

    def __str__(self):
        """ Возвращает имя категории и колличество продуктов """

        amount = 0
        for element in self.__products:
            amount += element.quantity

        return f"{self.name}, колличество продуктов: {amount}"

    def middle_price(self):
        """ Метод, высчитывающий средний ценник всех товаров """

        try:
            total_cost = 0
            for product in self.__products:
                total_cost += product.price * product.quantity
            return round(total_cost / sum([product.quantity for
                                           product in self.__products]), 2)

        except ZeroDivisionError:
            return 0
