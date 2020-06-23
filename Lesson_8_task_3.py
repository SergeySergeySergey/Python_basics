class TotalError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_list = []

while user_list.count("stop") == 0:
    try:
        user_list_input = input("Введите числа, для завершения работы программы введите stop: ")
        if user_list_input == 'stop':
            raise TotalError("Команда stop останавливает выполнение программы")
            exit(0)
        if int(user_list_input) > 0 or int(user_list_input) <= 0:
            user_list.append(user_list_input)
    except ValueError:
        print("Допустим ввод только чисел")
    except TotalError as err:
        print(user_list)
        print(err)
        exit(0)
    else:
        print(user_list)
