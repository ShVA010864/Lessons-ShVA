"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа
 в степень.
** Подсказка:** попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""
1.


def my_func_1(x, y):
    return (round(1 / x ** abs(y), 5))  # Ограничимся 5 знаками после запятой.


print("Вариант (**)")
print(my_func_1(int(input("Введите возводимое в степень число >>> ")),
                int(input("Введите степень числа >>> "))))

2.


def my_func_2(x, y):
    for i in range(abs(y - 1)):
        x *= y
    return (round(1 / x, 5))  # Ограничимся 5 знаками после запятой.


print("Вариант (Цикл)")
print(my_func_1(int(input("Введите возводимое в степень число >>> ")),
                int(input("Введите степень числа >>> "))))

3.


def my_func_3(x, y):
    powered = x

    if y > 0:
        for _ in range(1, y):
            powered *= x    # (powered = powered * x)
    else:
        for _ in range(1, y, -1):   # От 1 до y с шагом -1
            powered /= x
    return powered


a, b = int(input("Число a >>> ")), int(input("Число b >>> "))

print(my_func_3(a, b))
