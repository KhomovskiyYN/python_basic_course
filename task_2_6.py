
"""
Задание №6
*Реализовать структуру данных «Товары».
Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Необходимо собрать аналитику о товарах.
 Реализовать словарь, в котором каждый ключ — характеристика товара,
  например название, а значение — список значений-характеристик,
  например список названий товаров.
"""

characteristic = ['название', 'цена', 'количество', 'ед']

n = int(input("Введите какое количество техники вы хотите ввести: "))

product = []
cost = []
amount = []
numeration = []
for i in range(1, n + 1):
    print(f'введите все для {i} товара')
    prod  = input('название')
    product.append(prod)
    price = input('цена')
    cost.append(price)
    am = input('количество')
    amount.append(am)
    num = input('ед')
    numeration.append(num)

for i in range(n):
    dict = {characteristic[0] : product[i],
            characteristic[1] : cost[i],
            characteristic[2] : amount[i],
            characteristic[3] : numeration[i]}
    i += 1
    list = [('Номер товара: '+ str(i), dict)]
    print(list)

print('Аналитика: ')

dict_product = {'название' : product,
                'цена' : cost,
                'количество' : amount,
                'ед' : numeration}

j = 0
for j in range(0, 4):
    print(characteristic[j], dict_product[characteristic[j]])
    j += 1



# НИЖЕ ПЫТАЛСЯ СДЕЛАТЬ ЧЕРЕЗ СОЗДАНИЕ ДЛЯ КАЖДОГО ПРОДУКТА СВОЕГО КОРТЕЖА
#  НО НЕ ПОЛУЧИЛОСЬ СОЗДАВАТЬ В КАЖДОМ ПРОХОДЕ ЦИКЛА НОВЫЙ КОРТЕЖ

# num_product = input('введите количество продуктов')
#
# my_list = []
#
# wordbook = {}  # создать можно через wordbook = dict()
#
# for num in range(1, int(num_product) +1):
#
#     # my_list.append(num)
#     #print(my_list)
#     name = input('Введите название:')
#     price = input('Введите цену:')
#     amount = input('Введите количество:')
#     units = input('Введите единицы измерения:')
#     wordbook['название'] = name
#     wordbook['цена'] = price
#     wordbook['количество'] = amount
#     wordbook['ед'] = units
#     print(wordbook)
#
#     name_tuple = {}
#     name_tuple[name] = (wordbook)
#     print(name_tuple[name])
#     #my_tuple = (num, wordbook)
#
#     #my_list.append(name_tuple(name))
#
# print(my_list)

