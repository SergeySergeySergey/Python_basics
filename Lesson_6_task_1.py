import time
class TrafficLight:
    _color_ = 1
    def running (self):
        while T._color_ > 0:
            T._color_="red"
            print(f"\033[31m {T._color_}")
            time.sleep(7)
            T._color_="yellow"
            print(f"\033[33m {T._color_}")
            time.sleep(2)
            T._color_="green"
            print(f"\033[32m {T._color_}")
            time.sleep(2)
            T._color_ = 1
T=TrafficLight()
T.running()