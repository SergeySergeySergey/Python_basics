def anketa (name,last_name, birth_year, email, phone):
    return name, last_name, birth_year, email, phone
name=input("Введи Ваше имя: ")
last_name=input("Введите вашу фамилию: ")
birth_year=input("Введите год рождения: ")
email=input("Введите Ваш email: ")
phone=input("Введите Ваш номер телефона: ")
print(anketa(name,last_name, birth_year, email, phone))