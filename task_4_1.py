"""

Задание №1
Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, prod_in_hours, rate_per_hour, premium = argv

print('Script name: ', script_name)  #На русском языке не вывыодит в консоле git bash
print('Production in hours: ', prod_in_hours)
print('Rate per hour: ', rate_per_hour)
print('Premium: ', premium)

print('Salary: ', (float(prod_in_hours) * float(rate_per_hour)) + float(premium))