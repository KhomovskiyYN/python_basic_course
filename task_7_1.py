"""
Задание №1
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин,
расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

class Matrix:
    def __init__(self, liist_of_lists):
        self.matr = liist_of_lists
        self.my_matrix = []

    def __str__(self):
        my_matrix = '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matr])
        return my_matrix

    def __add__(self, other):
        # result = []
        # numbers = []
        # for i in range(len(self.matr)):
        #     for j in range(len(self.matr[0])):
        #         summa = other.mat[i][j] + self.matr[i][j]
        #         numbers.append(summa)
        #         if len(numbers) == len(self.matr[0]):
        #             result.append(numbers)
        #             numbers = []

        return Matrix(list(map(lambda x, y: list(map(lambda z, w: z + w, x, y)),
            self.matr, other.matr)))


a = [[31, 22], [37, 43], [51, 86]]
a_1 = [[24, 33], [18, 12], [4, -31]]

b = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
c = [[3, 5, 8, 3], [8, 3, 7, 1]]

m_1 = Matrix(a)
m_2 = Matrix(a_1)
m_3 = Matrix(b)
M_4 = Matrix(c)

print(m_1)
print('_______')
print(m_2)
print('Сумма двух матриц:')
print(m_1 + m_2)
print('_______')
print(m_3)
print('_______')
print(m_4)