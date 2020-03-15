
"""
Задание №6
 Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""
#  Скрипт b:

from itertools import cycle

first_num = [int(el) for el in input('Введите начальное число: ').split()]

for el in cycle(first_num):
        print(el)


#  Ниже -  другая вариация вывода:
# iter = cycle(first_num)
# while True:
#     print(next(iter))




