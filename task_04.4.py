"""4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]"""

list_n = [5, 3, 7, 6, 2, 9, 1, 5, 8, 4, 6, 2, 6]
print("Исходный список", list_n)

from collections import Counter
counter = Counter(list_n) # Посчитали количество повторений

result_list = [x for x,n in counter.items() if n==1] # Выбрали числа с количеством повторений =1
print("Неповторяющиеся числа", result_list)