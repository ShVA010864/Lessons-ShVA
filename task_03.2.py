"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
  Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой.
 """


def personal_data(name, surname, year, city, email, telephone):
    return (name, surname, year, city, email, telephone)


print("Введите ваши данные:")
print(personal_data(name=input("Имя:  "), surname=input("Фамилия: "), year=input("Год рождения: "),
                    city=input("Город проживания: "), email=input("Email: "),
                    telephone=input("Номер тлф: ")))

