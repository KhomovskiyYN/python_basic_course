
"""
Задание №3
Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

"""
file = open('file_task_5_3.txt', 'r', encoding='UTF-8')

lines = file.readlines()
print(lines)


result = 0
for ind, value in enumerate(lines):
    last_name, salary = value.split()
    salary = int(salary)
    result += salary
    if  salary < 20000:
        print(last_name)
print(result / (ind + 1))

file.close()