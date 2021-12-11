"""
5. Усовершенствовать первую функцию из предыдущего примера.
Необходимо во втором списке часть строковых значений заменить на значения типа example345
(строка+число).
Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений.
Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
состоящих из букв и цифр, например: example345.
"""
import os


def setup_file():
    if os.path.exists('file.txt'):
        print('File already exists and will overwritten')

    with open('file.txt', 'w') as f:
        lst1 = [x for x in range(1, 2000, 100)]
        lst2 = ['somedata' for i in range(12)]
        lst2[3] = ('somedata777')
        lst2.append('somedata777')

        for text, value in zip(lst2, lst1):
            data = f'{text} {value} \n'
            f.write(str(data))

    read_file()


def read_file():
    pattern = '777'

    with open('file.txt', 'r') as f_read:
        for line in f_read:
            # if pattern in line:           # first row which contains pattern
            #     print(line)
            #     break

            # if pattern in line:           # all rows which contains pattern
            #     print(line.strip())
            #
            # if pattern in line:           # replace all matches
            #     print(line.replace('777', '666').strip())

            if pattern in line:              # replace row
                line = 'broken line'
            print(line.strip())


setup_file()
