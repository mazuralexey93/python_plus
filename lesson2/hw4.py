"""
4. Реализовать возможность переустановки значения цены товара.
Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
(функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def get_name(self):
        return self.__name

    @property
    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f"Name: {self.get_name}, Price: {self.get_price}")


Parent = ItemDiscount('pear', 10)
print(Parent.get_price)
Parent.set_price(15)
print(Parent.get_price)

Child = ItemDiscountReport('apple', 5)
Child.get_parent_data()
Child.set_price(8)
Child.get_parent_data()
