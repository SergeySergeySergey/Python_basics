revenue=float(input("Введите сумму выручки: "))
expenses=float(input("Введите сумму издержек: "))
profit=revenue-expenses
loss=expenses-revenue
if profit>loss:
    print(f"Сумма прибыли составляет: {profit:.3f}" )
elif loss>profit:
    print(f"Сумма убытка составляет: {loss:.3f}" )
if profit>loss:
    roa=revenue/profit
    print(f"Рентабельность выручки: {roa:.3f}")
    man=int(input("Введите численность сотрудников: "))
    man_profit= profit/man
    print(f"Прибыль на одного сотрудника составляет: {man_profit:.3f}")