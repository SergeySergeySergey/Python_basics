user_list=input("Введите список целых чисел черезе пробел:").split()
try:
    user_list = list(map(int, user_list))
except:
    ValueError
    print("Вы ввели не целые числа!")
    exit()
result_list=[i for i in user_list if user_list.count(i)<2]
print(result_list)
