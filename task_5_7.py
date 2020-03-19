
"""
Задание №7
Cоздать (не программно) текстовый файл,
в котором каждая строка должна содержать данные о фирме:
 название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
 а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
 а также словарь со средней прибылью. Если фирма получила убытки,
также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

file = open('file_task_5_7.txt', encoding='UTF-8')
str_in_file = file.read().split('\n')
print(str_in_file)

dict_profit = {}
dict_average_profit = {}

for item in str_in_file:
    key = item.split(" ")[0]
    value = item.split(" ")[2:]
    revenue = item.split(" ")[2:-1]     # выручка
    revenue = int(revenue[0])
    profit = int(value[0]) - int(value[1])  # прибыль
    rent = profit / revenue * 100  # рентабельность
    rent = int(rent)
    dict_profit[key] = profit
    dict_average_profit[key] = profit, rent

print(dict_profit)

dict_middle_profit = {}
middle_profit = sum(dict_profit.values())/len(dict_profit)
dict_middle_profit['Средняя прибыль всех компаний'] = middle_profit
print(dict_middle_profit)


list = [dict_average_profit, dict_middle_profit]
print("\n\n", list)