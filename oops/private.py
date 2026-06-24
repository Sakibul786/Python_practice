class Student:

    def __init__(self):
        self.__name = "Rifat"


s = Student()

# print(s.__name)  # Error

print(s._Student__name)