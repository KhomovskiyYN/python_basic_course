
"""
Задание №1
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
и метод running (запуск). Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

from time import sleep

class TrafficLight:
    color = ['red', 'yellow', 'green']

    def running(self, color):
        if self.color[0] == color:
            print(color)
            sleep(7)
        elif self.color[1] == color:
            print(color)
            sleep(2)
        elif self.color[2] == color:
            print(color)
            sleep(3)
        else:
            print('wrong color')

new_color = [(el) for el in input('Введите 3 цвета (red, yellow, green): ').split()] #сами вводим цвета
my_color = TrafficLight()
#print(my_color.color)
while True:
    if not new_color == my_color.color:     # проверка на нарушение порядка
        print('wrong sequence' )
        break
    for i in new_color:
        my_color.running(i)
    break


# Можно проще:
    # __color = 'color'
    #
#     def running(self):
#         print('Red')
#         sleep(7)
#         print('Yellow')
#         sleep(2)
#         print('Green')
#         sleep(3)
#
# my_color = TrafficLight()
# while True:
#     my_color.running()