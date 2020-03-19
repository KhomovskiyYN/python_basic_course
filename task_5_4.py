
"""
Задание №4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу,
открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""

file = open('file_task_5_4.txt', 'r+', encoding='UTF-8')

lines = file.readlines()
print(lines)

new_words = ['Один', 'Два', 'Три', 'Четыре']
main_list = []

for value in lines:
     main_list.extend(value.split())
print(main_list,)


i = 0
for el in range(0, len(main_list), 3):
    main_list[el] = new_words[i]
    i +=1
print(main_list)

new_file = open('file_task_5_4.txt', 'w', encoding='UTF-8')
new_file.writelines(main_list)
file.close()

# Выводило в одну строку, попытался сделать с переносом, но возникает лишний перенос:

# new_file = open('file_task_5_4.txt', 'w', encoding='UTF-8')
# for j in range(12):
#     if j % 3:
#         new_file.write(main_list[j] +'\n')
#     else:
#         new_file.write(main_list[j])
# print(new_file)
# file.close()