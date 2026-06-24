# Creating a class

class Student:

    # Constructor runs automatically when object is created
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating objects
student1 = Student("Rifat", 22)
student2 = Student("Sakib", 21)

# Calling methods
student1.show_info()
student2.show_info()