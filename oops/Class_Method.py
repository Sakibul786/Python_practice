class Student:

    university = "AIUB"

    @classmethod
    def show_university(cls):
        print("University:", cls.university)


Student.show_university()