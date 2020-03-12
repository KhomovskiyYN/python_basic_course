"""
Задание №1
Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""

def my_division (my_dividended,my_divider):
    """
    Функция делит my_dividended на my_divider
    :param my_dividended: это делимое
    :param my_divider:  это делитьль
    :return: возвращает результат
    """

    try:
        result = my_dividended / my_divider
        return result

    except ZeroDivisionError:
        print('Делить на 0 нельзя')
        return None


a = input('введите делимое: ')
b = input('введите делитель: ')

print('Результат деления:', my_division(int(a),int(b)))