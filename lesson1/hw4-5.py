"""
4. Написать программу «Банковский депозит».
Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами
(begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и
выполнять расчет по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.

 5. Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.
"""


def get_rate(summa, period):
    """ В зависимости от суммы вклада возвращает значение процентной ставки"""
    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5}
    )

    for rate in rates:
        if rate['begin_sum'] <= summa < rate['end_sum']:
            return rate[period]
    return False


def deposit(summa, period):
    """Расчет прибыли за перод"""
    if 6 <= period < 12:
        period = 6
    elif 12 <= period < 24:
        period = 12
    elif 24 <= period:
        period = 24

    rate = get_rate(summa, period) / 100

    new_summa = summa
    for i in range(period):
        gain = new_summa * rate / 12
        new_summa += gain
    print(f'Сумма вклада на конец срока: {round(new_summa, 3)},'
          f' процентная ставка : {round(rate * 100, 1)}%, '
          f'доход: {round(new_summa - summa, 3)}')


deposit(120000, 16)


def monthly_payment_deposit(summa, period, payment=0):
    """Если период указан не равный 6, 12, 24,
     процентная ставка доп.вложенных средств будет начисляться как за минимильный период,
     """
    if 6 <= period < 12:
        period = 6
    elif 12 <= period < 24:
        period = 12
    elif 24 <= period:
        period = 24
    else:
        raise AttributeError('Period should be gt 6 months')

    rate = get_rate(summa, period) / 100
    new_summa = summa
    payment_summa = 0

    for i in range(period):
        gain = new_summa * rate / 12
        new_summa += gain
        if i != 0 and i != period - 1:
            payment_summa += payment + payment * rate / 12
        new_summa += payment_summa
    print(f'Сумма вклада на конец срока: {round(new_summa, 3)},'
              f' процентная ставка : {round(rate * 100, 1)}%, '
              f'доход: {round(new_summa - summa, 3)}, '
          f'доп.вложенные средства: {round(payment_summa, 3)}')


monthly_payment_deposit(120000, 12, 1000)