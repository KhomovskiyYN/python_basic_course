
"""
Задание №5
Создать (программно) текстовый файл,
записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""



file = open('file_task_5_5.txt', 'w')
print('Введите числа через пробел: ')
while True:
    text = input()
    file.write(text + '\n')
    if text == "":
        break


file = open('file_task_5_5.txt', 'r')
my_list = file.read().split()
print(my_list, type(my_list))

total = 0
for elem in my_list:
    total += int(elem)
print("Сумма чисел = ", total)
file.close()