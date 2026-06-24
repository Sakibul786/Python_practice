class Student:

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Student:", self.name)


s1 = Student("Rifat")

s1.show()