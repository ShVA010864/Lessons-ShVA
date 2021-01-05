""" Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

# Вариант 1
def func_divizi(arg_1, arg_2):
    try:
        result = arg_1 / arg_2
        return (round(result, 2))
        """ возвращаем результат деления, с округлением до двух знаков после запятой """
    except ZeroDivisionError:
        print("На ноль делить нельзя!!!")


print(func_divizi(int(input("Введите делимое >>> ")), int(input("Введите делитель >>> "))))

# Вариант 2
def main(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления"


x = int(input("Введите число x >>> "))
y = int(input("Введите число y >>> "))

print(main(x, y))
