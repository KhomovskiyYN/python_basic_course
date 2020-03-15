
"""
Задание №4
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элеме
нты вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
"""
my_list = [int(i) for i in input('Введите числа через пробел: ').split()]

# Через генератор:
my_result_1 = [num for num in my_list if my_list.count(num) == 1]

# С использованием функции фильтр:
my_result_2 = list(filter(lambda num: my_list.count(num) == 1, my_list))


print('Числа без повторений:', my_result_1)
print('Числа без повторений:', my_result_2)
