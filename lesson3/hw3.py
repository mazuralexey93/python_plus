"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи,
во втором — значения. Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""

list_keys = ['a', 'b', 'c']
# list_values = [1, 2, 3, 4]      # {'a': 1, 'b': 2, 'c': 3}
list_values = [1, ]           # {'a': 1, 'b': None, 'c': None}


def make_dict():
    while len(list_keys) > len(list_values):
        list_values.append(None)

    zipped = dict(zip(list_keys, list_values))
    return zipped


print(make_dict())
