# seconde = input("Укажите количество секунд: ")
# c = int(seconde)  # Переводим из строки в число
# b = minute_num = 60
# a = hour_num = 3600
# Оператор (//) дает деление без показа дробной части.
# print(f"Часы, {c // a}, Минуты {c // b}, Секунды {c}")
# Это неверное решение


sec = input("Укажите количество секунд: ")

if not sec.isdigit():
    print("Неверный формат числа!")
    exit()

user_c = int(sec)  # Переводим из строки в число
# a = hours = user_c // 3600
# b = minutes = (user_c % 3600) // 60
# c = secondes = (user_c % 3600) % 60
# print(a:, b:, c)

a, b, c = user_c // 3600, (user_c % 3600) // 60, (user_c % 3600) % 60

print(f"{a:>02}:{b:>02}:{c:>02}")
