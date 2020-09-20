class Worker:
    name = input("Введите имя работника: ")
    surname = input("Введите фамилию работника: ")
    position = input("Введите должность работника: ")
    try:
        wage = int(input("Введите з.п. работника: "))
        bonus = int(input("Введите премию работника: "))
    except ValueError:
        print("Допустим ввод только цифр!")
    _income = {"оклад": wage, "премия": bonus}


class Position(Worker):
    def __init__(self):
        get_full_name = self.name + " " + self.surname
        get_total_income = Worker._income.setdefault("оклад") + Worker._income.setdefault("премия")
        print(f"Полный оклад работника {get_full_name} на должности {self.position} составляет {get_total_income}")


p = Position()
