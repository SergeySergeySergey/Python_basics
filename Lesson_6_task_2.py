class Road:
    _length = input("Введите длинну дорожного полотона в метрах: ")
    _width = input("Введите ширину дорожного полотна в метрах: ")
    def __init__(self):
        try:
            Road._length = int(Road._length)
        except ValueError:
            print("Допустим ввод только цифр!")
            exit(0)
        try:
            Road._width = int(Road._width)
        except ValueError:
            print("Допустим ввод только цифр!")
            exit(0)
        formula=(Road._length*Road._width*25*5)/1000
        print(f"Расчетная масса асфальта: {formula} тонн")
r=Road()
