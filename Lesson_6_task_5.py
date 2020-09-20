class Stationary:
    title="Рисование"
    def draw (self):
        print(f"Запуск отрисовки")
class Pen (Stationary):
    def draw (self):
        print(f"Рисуем ручкой")
class Pensil (Stationary):
    def draw (self):
        print(f"Рисуем карандашом")
class Handle (Stationary):
    def draw (self):
        print(f"Рисуем маркером")
class Finish (Stationary):
    def draw (self):
        print(f"Рисунок готов!")
drawing_start=Stationary()
drawing_start.draw()
drawing_pen=Pen()
drawing_pen.draw()
drawing_pensil=Pensil()
drawing_pensil.draw()
drawing_handle=Handle()
drawing_handle.draw()
drawing_finish=Finish()
drawing_finish.draw()