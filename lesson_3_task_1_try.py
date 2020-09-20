user_number_1=(input("Введите делимое число: "))
user_number_2=(input("Введите делитель,кроме нуля: "))
try:
    user_number_1=int(user_number_1)
    user_number_2=int(user_number_2)
    user_number_2!=0
    print(user_number_1/user_number_2)
except ValueError:
    print("Вы ввели не числа!")
except ZeroDivisionError:
    print("На ноль делитиь нельзя!")
