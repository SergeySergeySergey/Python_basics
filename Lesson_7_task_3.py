class Cell:
    def __init__(self, cell):
        self.cell = cell

    def make_order(self, row):
        num_stars = self.cell // row
        stars_left = self.cell % row
        star = '*'
        gen = [star * row for i in range(num_stars)]
        res_gen = '\n'.join(gen)
        print(res_gen)
        result_stars_left = star * stars_left
        print(result_stars_left)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __str__(self):
        return f"Сумма клеток равна - {self.cell}"


class Cell_sub(Cell):
    def __sub__(self, other):
        return Cell_sub(self.cell - other.cell) if self.cell < 0 else "Вычетание с указанными данными невыполнимо!"

    def __str__(self):
        return f"Разность клеток равна - {self.cell}"


class Cell_mul(Cell):
    def __mul__(self, other):
        return Cell_mul(self.cell * other.cell)

    def __str__(self):
        return f"Число ячеек общей клетки (умножение) - {self.cell}"


class Cell_div(Cell):
    def __floordiv__(self, other):
        return Cell_div(self.cell // other.cell)

    def __str__(self):
        return f"Число ячеек общей клетки после деления (деление) - {self.cell}"


cell_1 = Cell(24)
cell_2 = Cell(12)
cell_1.make_order(5)
print(cell_1 + cell_2)
cell_1 = Cell_sub(12)
cell_2 = Cell_sub(22)
print(cell_1 - cell_2)
cell_1 = Cell_mul(22)
cell_2 = Cell_mul(12)
print(cell_1 * cell_2)
cell_1 = Cell_div(22)
cell_2 = Cell_div(12)
print(cell_1 // cell_2)
