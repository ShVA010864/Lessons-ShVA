"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

import task_mod
task_mod.salary()
time = float(input('Выработка в часах '))
rate = int(input('Ставка в у.е. '))
bonus = int(input('Премия в у.е. '))
print(task_mod)
