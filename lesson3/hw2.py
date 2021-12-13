""" 2. Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False."""


def check_number():
    try:
        user_number = input('Type int or float number: ')

        if ',' in user_number:
            user_number = user_number.replace(',', '.')
        converted_number = float(user_number)

        is_float = float(converted_number) - int(converted_number)
        if not is_float:
            print('Integer number!')
            return 0

        integer_part = int(converted_number)
        fractional_part = round(float(converted_number) - int(converted_number), 10)
        print(f'This is float number, integer part = {integer_part}, fractional part = {fractional_part}')

        len_of_int_part = len(str(integer_part))
        after_sep_number = fractional_part * (10 ** len_of_int_part)

        if integer_part == after_sep_number:
            return True
        return False

    except Exception:
        return 'Type int or float only!'


print(check_number())
