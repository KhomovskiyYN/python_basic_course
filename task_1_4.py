
"""
Задание №4
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

my_numb = int(input('Введите число целое положительное число:'))
remains = my_numb       #можно было не вводить переменную лишнюю, но для понимания логики, решил оставить
max_number = 0

while remains > 0:                  # В цикле вычленяем последнюю цифру (%10) и сокращаем само число на 1 знак (//10)
    digit_of_number = remains % 10
    remains = remains//10
    #print(digit_of_number)   # Испольлзовал для проверки
    #print(remains)

    if  digit_of_number >= max_number:
        max_number = digit_of_number

print(max_number)


