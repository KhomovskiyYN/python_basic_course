
"""
Задание №3
Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    name = str()
    surname = str()
    position = str()
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):

    def get_full_name(self, name, surname):
        self.name = name
        self.surname = surname
        print(f'Ваша фамилия: {surname}, Ваше имя: {name} ')

    def get_total_income(self, wage, bonus):
        self._income["wage"] = wage
        self._income["bonus"] = bonus
        print('Ваш доход: ', wage + bonus)



my_full_name = Position()
my_full_name.get_full_name('Ivan', 'Ivanov')

my_income = Position()
my_income.get_total_income(20, 30)
#print(my_income._income)