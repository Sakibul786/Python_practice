class Teacher:

    def __init__(self, name):
        self.name = name


class Department:

    def __init__(self, teacher):
        self.teacher = teacher


teacher = Teacher("Mr. Rahman")

department = Department(teacher)

print(department.teacher.name)