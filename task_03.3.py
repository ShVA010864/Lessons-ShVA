"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
 и возвращает сумму наибольших двух аргументов.
 """


# Вариант 1
def my_func(arg_1, arg_2, arg_3):
    """От суммы трех аргументов отнимаем величину минимального аргумента"""
    result = arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)
    print("Сумма двух наибольших аргументов = ", (result))


my_func(int(input("Введите значение первого аргумента >>> ")),
        int(input("Введите значение второго аргумента >>> ")),
        int(input("Введите значение третьего аргумента >>> ")))


# Вариант 2
def my_func(first, second, last):
    items = [first, second, last]
    items.remove(min(items))

    return sum(items)


a, b, c = int(input("Число а >>> ")), int(input("Число b >>> ")), int(input("Число c >>> "))
print(my_func(a, b, c))
