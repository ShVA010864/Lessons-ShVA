# Поль-ль вводит порядковый номер месяца (1-12). Вывести к какому времени года он относится. Решение через list и
# через dict.

month = int(input("Введите порядковый номер месяца: "))
if month <= 12 and month >= 1:
    month_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
                  9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
    month_list = list(month_dict.values())
else:
    print("Вы неверно ввели номер месяца!")
    exit()
for i, el in enumerate(month_list):
    if i == month - 1:
        print(f"Из листа вы выбрали: {month_list[i]}")
        break
print(f"Ваш месяц из словаря: {month_dict[month]}")

# seasons_l = ["winter", "spring", "summer", "autumn"]
seasons_d = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
if month == 12 or month == 1 or month == 2:
    #    print(seasons_l[0])
    print("Это", seasons_d.get(1))
if month == 3 or month == 4 or month == 5:
    #    print(seasons_l[1])
    print("Это", seasons_d.get(2))
if month == 6 or month == 7 or month == 8:
    #    print(seasons_l[2])
    print("Это", seasons_d.get(3))
if month == 9 or month == 10 or month == 11:
    #    print(seasons_l[3])
    print("Это", seasons_d.get(4))

month = int(input("Укажите номер месяца >>> "))



year_dict = {
    "Зима": (12, 1, 2),
    "Весна": (3, 4, 5),
    "Лето": (6, 7, 8),
    "Осень": (9, 10, 11),
}
for season, months in year_dict.items():
    if month in months:
        print(f"Время года = {season}")
        break
