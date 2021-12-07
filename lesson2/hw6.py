"""
6. Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара, а вторая — его цены.
Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemDiscountReportChild1(ItemDiscountReport):
    def get_info(self):
        print(f"Name: {self.get_name}")


class ItemDiscountReportChild2(ItemDiscountReport):
    def get_info(self):
        print(f"Price: {self.get_price}")


p = ItemDiscount('aaa', 100)
c1 = ItemDiscountReportChild1('bbb', 200)
c2 = ItemDiscountReportChild2('ccc', 300)
print(p.get_name)
print(p.get_price)

c1.get_info()
c2.get_info()

