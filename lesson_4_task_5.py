from functools import reduce
user_list=[el for el in range(100,1001,2)]
user_list_mult=reduce((lambda x,y:x*y),user_list)
print(user_list_mult)
