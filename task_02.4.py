# Пользователь вводит несколько слов с пробелами.
# Вывести каждое слово с новой строки и пронумеровать.
# В длинном слове выводить только первые 10 букв.

str_n = input("Введите несколько слов через пробел: ")
words_n = []
num = 1
for el in range(str_n.count(' ') + 1):
    words_n = str_n.split()
    if len(str(words_n)) <= 10:
        print(f" {num} {words_n[el]}")
        num += 1
    else:
        print(f" {num} {words_n[el][0:10]}")
        num += 1

words = input("Введите строку из нескольких слов >>> ").split()

for idx, value in enumerate(words, start=1):
    print(f"{idx}. {value[:10]}")
