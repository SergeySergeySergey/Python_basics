user_list=input("Введите список целых чисел:").split()
#print(user_list, type(user_list))
user_list=list(map(int, user_list))
print(user_list)
end_list=[user_list[i]for i in range(1,len(user_list)) if user_list[i]>user_list[i-1]]
print(end_list)
