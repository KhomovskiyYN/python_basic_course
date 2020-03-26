﻿"""
Задание №3
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (add()),
вычитание (sub()), умножение (mul()), деление (truediv()).Данные методы должны применяться только к клеткам
и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида **\n\n***..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: **\n\n.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: **\n\n***.
"""
class Cell:
    def __init__(self):
        self.result = 0
        self.row = []
        self.matr = []


    def __add__(self, other):
        return self.result + other

    def __sub__(self, other):
        return self.result - other

    def __mul__(self, other):
        return self.result * other

    def __truediv__(self, other):
        return round(self.result / other)

    def make_cell(self, am, n):

        self.row = [['*' for i in range(n) if am > n] for m in range(0, (round(am / n)))]  #заполняем list элементами
                                                                                           # кратными n, если am > n
        self.row.append(['*' for j in range(am % n)])  #дозаполняем остатком от деления am / n
        #print(self.row)
        self.matr = '\n'.join([''.join(['%10s' % '*' for i in row]) for row in self.row])  #выводим в виде матрицы

        print(self.matr)

c = Cell()
c.make_cell(15, 5)