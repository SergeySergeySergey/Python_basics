num=int(input("Введите целое положительное число: "))
biggest_num = 0
while num > 0:
    last_num = num % 10
    if last_num > biggest_num:
        biggest_num = last_num
        if biggest_num == 9:
            break
    num= num //10
print(f"Наибольшая цифра в числе {biggest_num}")