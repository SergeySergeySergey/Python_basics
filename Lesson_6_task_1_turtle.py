import turtle
import time
class TrafficLight:
    _color_ = 1
    def running (self):
        while T._color_ > 0:
            T._color_="red"
            turtle.begin_fill()
            turtle.color("red")
            turtle.circle(100)
            turtle.end_fill()
            time.sleep(7)
            turtle.clear()
            T._color_="yellow"
            turtle.begin_fill()
            turtle.color("yellow")
            turtle.circle(100)
            turtle.end_fill()
            time.sleep(2)
            turtle.clear()
            T._color_="green"
            turtle.begin_fill()
            turtle.color("green")
            turtle.circle(100)
            turtle.end_fill()
            time.sleep(2)
            turtle.clear()
            T._color_ = 1
T=TrafficLight()
T.running()
