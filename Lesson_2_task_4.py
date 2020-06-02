user_string=list(input("Введите слова:  " '').split())
for num, el, in enumerate(user_string, 1):
    print(str(num) + "-" + str(el[:10]) + " ")

