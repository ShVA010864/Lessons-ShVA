# Поменять местами соседние элементы списка. Если количество элементов нечетноея, то последний
# остается без изменений.

# data_n = input("Введите несколько любых элементов: >>> ")
# print(data_n)

list_n = ['a', 'b', 'c', 'd', 'e']
# list_n = tuple(data_n)
print(list_n)

i = 0
for i in range(int(len(list_n) / 2)):
    list_n[i], list_n[i + 1] = list_n[i + 1], list_n[i]
    i = i + 2
    print(i)
    print(list_n)

items = input("Укажите значения списка через запятую >>>").split(",")

max_idx = len(items) - 1

for idx in range(0, max_idx, 2): # диапазон от 0 до макс символа с шагом 2
    next_idx = idx + 1  # внутри цикла получаем текущий элемент и следующий
    items[idx], items[next_idx] = items[next_idx], items[idx]

print(items)
