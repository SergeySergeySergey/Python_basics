class Road:
    _length=int(input("Введите длинну дорожного полотона в метрах: "))
    _width=int(input("Введите ширину дорожного полотна в метрах: "))
    def road_formula(self):
        formula=(Road._length*Road._width*25*5)/1000
        print(f"Расчетная масса асфальта: {formula} тонн")
r=Road()
r.road_formula()


