
def my_func_3 (num, power):
    """ Третий способ реализации функции"""
    return (num * my_func_3(num, power - 1) if power > 0 else 1)


a = int(input("Введите положительное число a: "))
b = int(input("Введите положительное число b: "))
print(my_func_3(a, b))