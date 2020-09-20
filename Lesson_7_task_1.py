class My_matrix:
    def __init__(self, matrix_1):
        self.matrix_1 = matrix_1

    def __add__(self, other):
        matrix_a = self.matrix_1
        matrix_b = other.matrix_1
        matrix_temp = []
        for el in range(len(matrix_a)):
            matrix_temp_row = []
            for i in range(len(matrix_b[el])):
                summ = matrix_a[el][i] + matrix_b[el][i]
                matrix_temp_row.append(summ)
            matrix_temp.append(matrix_temp_row)
        return My_matrix(matrix_temp)

    def __str__(self):
        result = '\n'.join(['\t\t'.join(map(str, self.matrix_1[i])) for i in range(len(self.matrix_1))])
        return f"Сумма матриц равна: \n {result}"


matrix_1 = My_matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = My_matrix([[7, 8], [9, 10], [11, 12]])
matrix_temp = []
print(matrix_1 + matrix_2)
