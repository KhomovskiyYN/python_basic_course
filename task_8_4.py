"""
Задание №3
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Warehouse:
    print("Склад оргтехники")


class OfficeEquipment(Warehouse):
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    amount_pr = 0


class Scanner(OfficeEquipment):
    """Класс сканер"""
    amount_sc = 0

class Xerox(OfficeEquipment):
    amount_x = 0



