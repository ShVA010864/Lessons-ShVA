list_n = [7, 5, 3, 3, 2]
print(f"Рейтинг:  {list_n}")
number = int(input("Стоп - 000!!! Введите число >>> "))
while number != 000:
    for el in range(len(list_n)):
        if list_n[el] == number:
            list_n.insert(el + 1, number)
            break
        elif list_n[0] < number:
            list_n.insert(0, number)
        elif list_n[-1] > number:
            list_n.append(number)
        elif list_n[el] > number and list_n[el + 1] < number:
            list_n.insert(el + 1, number)
    print(f"текущий список - {list_n}")
    number = int(input("Введите число >>> "))

rating = [9, 8, 8, 7, 6, 6, 6, 5, 3, 2, 1]

while True:
    try:
        print(f"Рейтинг = {rating}")
        user_rate = int(input("Введите новый рейтинг >>> "))

        # Самый простой но долгий
        rating.append(user_rate)
        rating.sort(reverse=True)

        print(rating)
    except ValueError:
        print("Неверное число")
    except KeyboardInterrupt:
        exit()
