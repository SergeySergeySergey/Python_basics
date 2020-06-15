class Road:
    try:
        _length=int(input("Введите длинну дорожного полотона в метрах: "))
    except ValueError:
        print("Допустим ввод только цифр!")
    try:
        _width=int(input("Введите ширину дорожного полотна в метрах: "))
    except ValueError:
        print("Допустим ввод только цифр!")
    def __init__(self):
        formula=(Road._length*Road._width*25*5)/1000
        print(f"Расчетная масса асфальта: {formula} тонн")
r=Road()
