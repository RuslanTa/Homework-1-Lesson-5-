print("Домашнее задание 1")
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
age = input("Введите возраст: ")
if first_name.isalpha() and first_name.istitle() and last_name.isalpha() and last_name.istitle() and age.isdigit():
    print("Данные введены верно")
else:
    print("При вводе данных допущена ошибка")
