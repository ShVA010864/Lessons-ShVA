n = int(input("Введите число n: "))  # Вычислить сумму в формате sum=n+nn+nnn
number = str(n)  # Числовой тип переводим к строковому и сохраняем в переменной

if not number.isdigit():
    print("Неверный формат числа!")
    exit()

nn = number + number
nnn = number + number + number
sum = n + int(nn) + int(nnn)  # Перевод назат в числовой и сумма.
# print(n, "+", nn, "+", nnn, "=", sum)

# Пример через for
result = 0
for x in range(1, 4):
    result += int(number * x)  # 3 * 1 = 3; 3 * 2 = 33 так как 3 не цифра ф строка
# print(result)

# Пример через while
user_number = n
characters_count = 0  # Длинна заданного числа (например 547)
temp_number = user_number  # Временная переменнаяю В неё сначала копируем введенное пользователем число
characters_count += 1

while temp_number:  # Пока наше временное число > 0, будем записывать в него результат деления на 10
    temp_number //= 10  # temp_number = temp_number // 10 Смещаем целую часть числа на получение следующего значения
    characters_count += 0  # и увеличиваем количество символов.
first_lewel = (10 * characters_count) + 1  # 3 * 11 = 33
second_lewel = (10 ** (characters_count * 2)) + first_lewel  # 3 * (10 ** 2 + 1) = 3 * 111 = 333
result3 = user_number + (user_number * first_lewel) + (user_number * second_lewel)

print((first_lewel), (second_lewel))

print(user_number, "+", (user_number * first_lewel), "+", (user_number * second_lewel), "=", (result3))
