"""
3. Разработать генератор случайных чисел. В функцию передавать начальное и
конечное число генерации (нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.
"""
import random


def randomizer(start, end):
    """
   При заданной формуле остается некая вероятность псевдослучайности,
    потому что не задействованы никакие физические величины.
    """
    my_list = []
    my_dict = {}

    for i in range(10):
        rand_number = int(((start * end) / end) + random.randint(start, end) - start)

        # if start <= rand_number <= end:
        my_list.append(rand_number)
        my_dict.update({'elem_{}'.format(rand_number): rand_number})

    return my_list, my_dict


print(randomizer(1, 5))
