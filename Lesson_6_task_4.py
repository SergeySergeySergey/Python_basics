import random
class Car:
    try:
        speed = int(input("Выберите скорость движения км/ч: "))
        if speed > 110:
            print("Выбранная вами скорость движения недопустима на дорогах общественного пользования. Досвидания.")
            exit(0)
    except ValueError:
        print("Вы ввели не число!")
    is_police = input("Автомобиль полицейский? Да/Нет ")
    name = input("Укажите модель автомобиля: ")
    color = input("Укажите цвет автомобиля: ")
    def go (self):
        print("Машина поехала.")
    def stop (self):
        print("Машина остановилась.")
    def turn (self):
        where_turn=random.randrange(1,100)
        if where_turn > 50:
            print("Машина поворачивает налево")
        if where_turn < 50:
            print("Машина поворачивает направо")
    def show_speed (self):
        print(f"Машина движется со скоростью: {c.speed} км/ч")
class TownCar (Car):
    def __init__(self):
        print(f"Вы выбрали Городской автомобиль, модель: {c.name} цвета: {c.color}")
        c.go()
        c.show_speed()
        print("Вы привысили скорость! Вас остановила полиция, дальше пешком!") if c.speed > 60 else print("Вы не привышаете скорость, спасибо за соблюдение ПДД!")
        if c.speed > 60:
            exit(0)
        c.turn()
        c.stop()
class WorkCar (Car):
    def __init__(self):
        c.go()
        c.show_speed()
        print("Вы привысили скорость! Вас остановила полиция, дальше пешком!"), exit(0) if c.speed > 40 else print("Вы не привышаете скорость, спасибо за соблюдение ПДД!")
        if c.speed > 40:
            exit(0)
        c.turn()
        c.stop()
class SportCar (Car):
    def __init__(self):
        c.go()
        c.show_speed()
        c.turn()
        c.stop()
class PoliceCar (Car):
    def __init__(self):
        c.go()
        if c.speed > 60:
            print("В связи с превышением скорости включаем спец сигнал.")
        c.show_speed()
        c.turn()
        c.stop()
        exit(0)
c=Car()
PC = PoliceCar() if c.is_police == "Да" else print("Продолжаете ввод данных")
choise=input("Выберете автомобиль Городской, Спортивный, Рабочий: " )
if choise == "Городской":
    TC=TownCar()
if choise == "Рабочий":
    WC=WorkCar()
if choise == "Спортивный":
    SC=SportCar()

