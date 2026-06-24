# Parent Class
class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Name:", self.name)


# Child Class
class Student(Person):

    # Constructor
    def __init__(self, name, student_id):

        # Call parent constructor
        super().__init__(name)

        self.student_id = student_id

    # Overriding method
    def introduce(self):
        print("Student Name:", self.name)
        print("Student ID:", self.student_id)


# Create object
s1 = Student("Rifat", 101)

# Call method
s1.introduce()