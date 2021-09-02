# Task1

class Matrix:
    def __init__(self, lists: list):
        self.lists = lists
# Решение для "реализовать перегрузку метода str() для вывода матрицы в привычном виде"
    def __str__(self):
        for row in self.lists:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''


# Решение для "реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц)"
    # def __str__(self):
    #     return '\n'.join(map(str, self.lists))
    #
    # def __str__(self):
    #     return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.lists]))
    #
    # def __add__(self, other):
    #     for i in range(len(self.lists)):
    #         for y in range(len(other.lists[i])):
    #             self.lists[i][y] = self.lists[i][y] + other.lists[i][y]
    #     return Matrix.__str__(self)


list_1 = Matrix([[3, 5, 8, 3],
                 [8, 3, 7, 1]])

list_2 = Matrix([[7, 5, 2, 7],
                 [2, 7, 3, 9]])

# Решение для "реализовать перегрузку метода str() для вывода матрицы в привычном виде"
print(list_1)
print(list_2)

# Решение для "реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц)"
# print(list_1.__add__(list_2))

