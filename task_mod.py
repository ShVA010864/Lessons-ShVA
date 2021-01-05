"""
Функция расчета заработной платы сотрудника.
Скрипт с параметрами.
"""
def salary():
    """
        :rtype: object
    """
    try:
        time = float(input('Выработка в часах '))
        rate = int(input('Ставка в у.е. '))
        bonus = int(input('Премия в у.е. '))
        res = time * rate + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a number')

