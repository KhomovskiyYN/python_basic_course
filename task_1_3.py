
"""
Задание №3
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""


my_numb = input('Введите число n:')
if int(my_numb) > 0 and int(my_numb) < 10:  #Если использовать однозначное число, то можно решить проще -
                                            #  умножая на 11, 111, 1111...
    print(f'сумму чисел {my_numb} + {my_numb}{my_numb} + {my_numb}{my_numb}{my_numb}'
          ' равна:', int(my_numb) +int(my_numb) * 11 + int(my_numb) * 111)

elif int(my_numb) > 10:  # при двузначном и более создаю list, состоящий из str, поэтому могу корректно сделать
                        # запись типа nn, nnn (например: для числа 12 - 1212 и 121212)
                        #затем перевожу в int для сложения

    result_num = 0
    list = [my_numb, my_numb * 2, my_numb * 3]
    for i in list:
        result_num += int(i)
    print(f'сумму чисел {my_numb} + {my_numb}{my_numb} + {my_numb}{my_numb}{my_numb}'
          ' равна:',result_num)

else:
    print('Gри отрицательных числах -некорректная получатся запсь')
