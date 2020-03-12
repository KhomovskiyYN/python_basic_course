
"""
Задание №3
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_funk(*args):

    """ Функция принимает три *args аргумента и возвращает сумму наибольших двух
    args - это кортеж
    """
    """
    Более сложный способ:
    # my_list = []      #делаем из кортежа list
    # for num in args:
    #     my_list.append(num)
    # my_list.sort()
    # return  my_list[-2] + my_list[-1]
    """

    return sum(args) - min(args)

a = input('Введите 1-ое число: ')
b = input('Введите 2-ое число: ')
c = input('Введите 3-е число: ')

print('Сумма двух наибольших чисел: ', my_funk(int(a), int(b), int(c)))