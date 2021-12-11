"""1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения)."""

import os

# path_name = r'C:\Users\user\PycharmProjects\testfile.txt'
path_name = r'C:\Users\user\PycharmProjects\testfile.tar.gz'


def get_filename(file_name) -> str:
    full_name = os.path.basename(file_name)
    name = full_name.split('.')[0]
    return name


print(get_filename(path_name))
