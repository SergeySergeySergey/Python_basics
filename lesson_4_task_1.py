from sys import argv

script_name, working_hours, hour_payment, bonus = argv

try:
    working_hours=int(working_hours)
    hour_payment = int(hour_payment)
    bonus = int(bonus)
except:
    ValueError
    print("Вы ввели некорректные значения!")
def salary (working_hours, hour_payment, bonus):
    sum_salary=working_hours*hour_payment+bonus
    return sum_salary
print("Заработная плата сотрудника составляет:", salary(working_hours, hour_payment, bonus))