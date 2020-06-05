def my_func (x,y):
    x=x ** y
    return x
x=int(input("Введите действительное положительное число: "))
y=int(input("Введите целое отрицательное число, степнь числа: "))
print(my_func(x,y))