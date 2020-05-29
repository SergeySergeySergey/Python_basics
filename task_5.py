revenue=int(input("Введите сумму выручки: "))
expenses=int(input("Введите сумму издержек: "))
profit=revenue-expenses
loss=expenses-revenue
if profit>loss:
    print("Сумма прибыли составляет: ", profit )
elif loss>profit:
    print("Сумма убытка составляет: ", loss )
if profit>loss:
    roa=revenue/profit
    print("Рентабельность выручки: ", roa)
    man=int(input("Введите численность сотрудников: "))
    man_profit= profit/man
    print("Прибыль на одного сотрудника составляет: ", man_profit)