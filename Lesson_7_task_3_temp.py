class Cell:
    def __init__(self, cell_1, cell_2):
        self.cell_1=cell_1
        self.cell_2=cell_2
    def __add__(self, other):
        return Cell(self.cell_1+other.cell_1, self.cell_2+other.cell_2)
    def __str__(self):
        return f"Сумма клеток равна - {self.cell_1}"

cell_1 = Cell(22,0)
cell_2 = Cell(12,0)
print(cell_1 + cell_2)