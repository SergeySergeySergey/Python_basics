class Calc():
    def __init__(self,size):
        self.size=size
class Suit(Calc):
    @property
    def suit_calc(self):
        return (round(((2 * self.size) + 0.3), 2))
class Coat(Calc):
    @property
    def coat_calc(self):
        return (round(((self.size / 6.5) + 0.5), 2))

print("Добро пожаловать в калькулятор подсчета расхода ткани!")
try:
    suit = Suit(int(input("Введите рост для подсчета расхода ткани на костюм: ")))
except ValueError:
    print("Введите число!")
    exit(0)
try:
    coat= Coat(int(input("Введите размер пальто для подсчета расхода ткани: ")))
except ValueError:
    print("Введите число!")
    exit(0)
common=suit.suit_calc + coat.coat_calc
print(f"Расход ткани для пошива костюма размера 32 - {suit.suit_calc}")
print(f"Расход ткани для пошива пальто на 180 рост - {coat.coat_calc}")
print(f"Общий расход ткани для костюма 32 замера и пальто на 180 рост равно {common}")
