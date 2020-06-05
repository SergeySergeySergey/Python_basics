user_number_1=(int(input("Введите делимое число: ")))
user_number_2=(int(input("Введите делитель,кроме нуля: ")))
def division_calc():
    global division_calc
    division_calc = user_number_1 / user_number_2
    return division_calc
division_result=division_calc()
print(division_result)