
"""
Задание №2
Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
 Для формирования списка использовать генератор.

"""

def grow_sequence (ny_str):


    my_list = [int(el) for el in my_str.split()]   # использовал генератор

    my_result = []

    for i in range(1, len(my_list)):
       if my_list[i] > my_list[i - 1]:
            my_result.append(my_list[i])

    return(my_result)


my_str = input('Введите исходную строку через пробел: ')
print(grow_sequence(my_str))

