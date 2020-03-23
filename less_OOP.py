class Person:
    name = 'Ivan'
    age = 10

    def _set(self, name, age):
        self.name = name
        self.age = age

class Student (Person):
    course = 1

igor = Student()
igor._set('Igor', 19)
igor.course = 2
print(igor.name, igor.age, igor.course)

vlad = Person()
vlad._set("Vlad", 25)
print(vlad.name + ' ' + str(vlad.age))
print(vlad._set)

ivan = Person()

print(ivan.name + ' ' + str(ivan.age))

