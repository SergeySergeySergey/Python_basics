user_list=[el for el in range(100,1001,2)]
def user_mult(user_list):
    result=1
    for el in user_list:
        result=result*el
    return result
print(user_mult(user_list))