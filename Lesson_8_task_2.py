#в качестве "уникальной ошибки" я добавил деление на 2.
class TotalError (Exception):
    def __init__(self, txt):
        self.txt = txt
user_num = input("Введите делитель, кроме 2: ")
try:
    user_num = int(user_num)
    if user_num == 2:
        raise TotalError("На 2 делить категорически запрещено условием")
    print(100 / user_num)
except ValueError:
    print("Вы ввели не число")
except ZeroDivisionError:
    print("Вы ввели ноль, а на него делить нельзя")
except TotalError as err:
    print(err)
else:
    print("Окнончание работы программы")
