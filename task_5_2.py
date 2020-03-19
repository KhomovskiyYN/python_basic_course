
"""
Задание №2
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

file = open('file_task_5_2.txt', 'r')

lines = file.readlines()    # readlines - возвращает список
#print(lines, type(lines))

for idx, value in enumerate(lines):
    num_words = len(value.split())
    print(f'Line number = {idx + 1}; and quantity words = {num_words} ')

file.close()

