"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса. В этом методе должна пересчитываться цена и
возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


class Item:
    def __init__(self, price):
        self.price = price


class ItemDiscount(Item):
    def __init__(self, price, discount):
        Item.__init__(self, price)
        self.discount = discount

    def __str__(self):
        if self.discount <= self.price:
            return f"Price with sale: {self.price - self.price * self.discount / 100}"
        return "Price should be greater than 0!"


item = Item(1000)
print(item.price)

item_sale = ItemDiscount(100, 150)
print(item_sale)

item_sale = ItemDiscount(100, 50)
print(item_sale)
