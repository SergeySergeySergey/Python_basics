user_month=int(input("Введите месяц в виде целого числа: "))
winter=[12, 1, 2]
spring=[3, 4, 5]
summer=[6, 7, 8]
autumn=[9, 10, 11]
print("это зимний месяц" if user_month in winter else "")
print("это весенний месяц" if user_month in spring else "")
print("это летний месяц" if user_month in summer else "")
print("это осенний месяц" if user_month in autumn else "")