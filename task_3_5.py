
"""
Задание №5
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
 Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
  Но если вместо числа вводится специальный символ, выполнение программы завершается.
  Если специальный символ введен после нескольких чисел,
  то вначале нужно добавить сумму этих чисел к полученной ранее сумме
и после этого завершить программу.
"""

"""
def my_summ(my_string):
    my_list = my_string.split()  # list из str

    my_result = []
    for i in my_list:
        my_result.append(int(i))
    return sum(my_result)


print('Специальный всимвол "n"')  #ВВОД ДОЛЖЕН ЗАКАНЧИВАТЬСЯ n, потом обязательно enter
result_sum = 0
while True:
    print('Специальный всимвол "n"')
    my_string = input('Введите строку:')

    if my_string.endswith('n'):      # если ввод
        my_string = my_string[:-1]
        result_sum += my_summ(my_string)
        print(result_sum)
        break
    else:
        result_sum += my_summ(my_string)
        print(result_sum)


"""
# Второй вариант: ЗАРАБОТАЛ!!!

def my_summ(my_string):
    my_list = my_string.split()  # list из str

    my_result = []
    for i in my_list:
        my_result.append(int(i))
    return sum(my_result)


print('Специальный всимвол "n"')
result_sum = 0
while True:

    my_string = input('Введите строку:')

    swith = True


    indx = 0
    for i in my_string:             # Проверяем на наличие n  в вводимой строке

        if i == 'n':
            swith = False
            break
        indx = indx + 1
        #print(indx)

    if swith:
        result_sum += my_summ(my_string)
        print(result_sum)
    else:
        my_string = my_string[:int(indx - 1)]           #Проход функции по строке до символа n
        # print(indx)
        # print(my_string)

        result_sum += my_summ(my_string)
        print(result_sum)
        break


