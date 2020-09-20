# пример числа взял из задачи по ссылке,которую вы прислали
class Complex:
    def __init__(self, num_1):
        self.num = num_1

    def __add__(self, other):
        return Complex(self.num + other.num)

    def __str__(self):
        return f'Сумма комплексных чисел равна - {self.num}'


class Complex_mul(Complex):
    def __mul__(self, other):
        return Complex_mul(self.num * other.num)

    def __str__(self):
        return f'Произведение комплексных чисел равно - {self.num}'


a = 3 + 1j
b = 2 - 3j
num_1 = Complex(a)
num_2 = Complex(b)
num_1 = Complex_mul(a)
num_2 = Complex_mul(b)
print(num_1 + num_2)
print(num_1 * num_2)
