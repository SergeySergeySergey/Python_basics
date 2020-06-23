class Calend:
    @staticmethod
    def extractor(date):
        d_1 = int(date[0])
        month = int(date[1])
        year = int(date[2])
        print(d_1, month, year)
        Calend.check(d_1, month, year)

    def check(d_1, month, year):
        if d_1 <= 0:
            print("Вы ввели некорректные данные")
        if d_1 > 31:
            print("Вы ввели некорректные данные")
        if month <= 0:
            print("Вы ввели некорректные данные")
        if month > 12:
            print("Вы ввели некорректные данные")
        if year < 0:
            print("Вы ввели некорректные данные")


Calend.extractor([20, 6, 2020])
