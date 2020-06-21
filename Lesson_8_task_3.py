class TotalError (Exception):
    def __init__(self, txt):
        self.txt = txt
user_list=[]

while user_list.count("stop") == 0:
    try:
        user_list_input = int(input("Введите числа, для завершения ввода введите q: "))
        user_list.append(user_list_input)
        if user_list.count("stop") > 0:
            print(user_list)
            exit(0)
            raise TotalError ("Вы ввели ключевое слово, работа программы остановлена")
    except ValueError:
        print("Допустим ввод только чисел")
    except TotalError as err:
        print(err)
    else:
        print(user_list)
user_list