
"""
Задание №4
  Пользователь вводит строку из нескольких слов, разделённых пробелами.
  Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
  Если в слово длинное, выводить только первые 10 букв в слове.
"""


my_string = input('Введите строку:')

my_list = my_string.split()    #можно быстрее: my_list = input().split() -
                                # сразу вводим list, разделяемый пробелами

counter = 0  #количество строк

 # print(type(my_list))

for element in my_list:
    counter += 1
    print(counter, end=" ")

    if len(element) > 10:
        print(element[:10])  # вывод с 0 по 10 не включительно
    else:
        print(element)

    #print(type(element))

