class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, id):
        super().__init__(name)
        self.id = id


s = Student("Rifat", 101)

print(s.name)
print(s.id)