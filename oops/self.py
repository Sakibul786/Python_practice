class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)


p1 = Person("Rifat")

p1.greet()