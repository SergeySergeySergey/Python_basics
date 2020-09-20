my_list=[7, 5, 3, 3, 2]
user_number=int(input("Введите число: "))
if user_number <= 2:
    print(my_list.append(user_number))
if user_number <= 3:
    print(my_list.insert(4,user_number))
if user_number <= 4:
    print(my_list.insert(2,user_number))
if user_number <= 5:
    print(my_list.insert(2, user_number))
if user_number <= 6:
    print(my_list.insert(1, user_number))
if user_number <= 7:
    print(my_list.insert(1, user_number))
if user_number >= 8:
    print(my_list.insert(0, user_number))
print(my_list)