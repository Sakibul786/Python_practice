class Student:

    # Class variable
    university = "AIUB"

    def __init__(self, name):
        self.name = name


s1 = Student("Rifat")
s2 = Student("Sakib")

print(s1.university,s1.name)
print(s2.university,s2.name)