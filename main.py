#
# def my_func_3 (num, power):
#     """ Третий способ реализации функции"""
#     return (num * my_func_3(num, power - 1) if power > 0 else 1)
#
#
# a = int(input("Введите положительное число a: "))
# b = int(input("Введите положительное число b: "))
# print(my_func_3(a, b))

# old_list = ['1', '2', '3', '4', '5', '6', '7']
# new_list = list(map(int, old_list))
# print(new_list)
#
# [1, 2, 3, 4, 5, 6, 7]
#
#
# def miles_to_kilometers(num_miles):
#     """ Converts miles to the kilometers """
#     return num_miles * 1.6
#
#
# mile_distances = [1.0, 6.5, 17.4, 2.4, 9]
# kilometer_distances = list(map(miles_to_kilometers, mile_distances))
# print(kilometer_distances)
#
# [1.6, 10.4, 27.84, 3.84, 14.4]
#
# from functools import reduce
#
# items = [1, 2, 3, 4]
# sum_all = reduce(lambda x, y: x * y, items)
#
# print(sum_all)


file = open('file_task_5_2.txt', 'r')

lines = file.readlines()    # readlines - возвращает список
#print(lines, type(lines))

for line in lines:
    print(line)
    for el in line:
        print(el)

file.close()
