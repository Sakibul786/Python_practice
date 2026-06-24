from abc import ABC, abstractmethod


# Abstraction base class
class Person(ABC):

    def __init__(self, name):
        self.name = name  # public attribute

    @abstractmethod
    def role(self):
        pass  # must be implemented by child classes

    def show_name(self):
        print("Name:", self.name)


# Composition class (Engine belongs to Student)
class Engine:

    def start(self):
        print("Engine started")


# Student class demonstrating most OOP concepts
class Student(Person):

    university = "AIUB"  # class variable shared by all objects

    def __init__(self, name, student_id, age):
        super().__init__(name)

        # encapsulated (private) variables
        self.__student_id = student_id
        self.__age = age

        # composition (object inside object)
        self.engine = Engine()

    # method overriding (polymorphism)
    def role(self):
        print("Role: Student")

    # instance method
    def show_info(self):
        print("Name:", self.name)
        print("ID:", self.__student_id)
        print("Age:", self.__age)
        print("University:", Student.university)

    # property getter
    @property
    def age(self):
        return self.__age

    # property setter
    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print("Invalid age")

    # class method
    @classmethod
    def change_university(cls, name):
        cls.university = name

    # static method
    @staticmethod
    def add(a, b):
        return a + b

    # magic method
    def __str__(self):
        return f"Student: {self.name}"

    # operator overloading
    def __add__(self, other):
        return self.__age + other.__age

    # encapsulation access method
    def get_id(self):
        return self.__student_id

    # composition usage
    def start_study(self):
        self.engine.start()


# Another child class (polymorphism example)
class Teacher(Person):

    def role(self):
        print("Role: Teacher")


# Aggregation example (Department has Student)
class Department:

    def __init__(self, student):
        self.student = student

    def show(self):
        print("Department student:", self.student.name)


# Creating objects
s1 = Student("Rifat", 101, 22)
s2 = Student("Sakib", 102, 25)
t1 = Teacher("Mr. Rahman")


# Using methods
s1.show_info()
s1.role()
t1.role()

print()

# Encapsulation access
print("ID:", s1.get_id())

# Property usage
print("Age:", s1.age)
s1.age = 23
print("Updated Age:", s1.age)

print()

# Class method
Student.change_university("Dhaka University")
print("University:", s1.university)

# Static method
print("Sum:", Student.add(10, 20))

print()

# Magic method
print(s1)

# Operator overloading
print("Age total:", s1 + s2)

print()

# Composition
s1.start_study()

print()

# Aggregation
dept = Department(s1)
dept.show()

print()

# Polymorphism
people = [s1, t1]

for p in people:
    p.role()