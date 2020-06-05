def sum_func (num_1, num_2, num_3):
    num_min=min(num_1, num_2, num_3)
    num_sum=num_1+num_2+num_3-num_min
    return num_sum
print(sum_func(num_1=int(input("Введите первое число:")), num_2=int(input("Введите второе число:")), num_3=int(input("Введите третье число:"))))