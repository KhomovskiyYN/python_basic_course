

"""
Задание №2
 Для списка реализовать обмен значений соседних элементов,
 т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
 При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []
number_elements = input()           # Сначала узнаем чилсо элементов в списке

for i in range(int(number_elements)):          # Заплняем спсок
    my_list.append(int(input()))

print(my_list)


my_new_list = []

if len(my_list) % 2 == 0:
    for elem in my_list[0::2]:
        #print(elem)
        my_new_list.append(elem+1)

        my_new_list.append(elem)

else:
    for elem in my_list[0:-2:2]:            # Для нечетного -  идем циклом до предпоследнего
        #print(elem)                        # и добавляем в новый список последний
        my_new_list.append(elem + 1)
        my_new_list.append(elem)
    my_new_list.append(my_list[-1])

print(my_new_list)


