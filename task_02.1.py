# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
# поверки типа данных элементов с помощью функции type(). Элементы указать в явном виде.

int_n = 7
float_n = 2.5
str_n = "Python text"
bool_n = (1 > 1)
list_n = ['a', '7', '@']
tupl_n = ("a", "7", "@")
dict_n = {'name': 'Vadim', 'age': '25'}

general_list = [int_n, float_n, str_n, bool_n, list_n, tupl_n, dict_n]
for i in general_list:
    print(f'{i} - {type(i)}')

example_list = ["String", 10, 25, 78, False, "True", []]
for item in example_list:
    print(type(item))
