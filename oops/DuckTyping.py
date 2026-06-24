class Bird:

    def fly(self):
        print("Bird flying")


class Plane:

    def fly(self):
        print("Plane flying")


def start_flying(obj):
    obj.fly()


start_flying(Bird())
start_flying(Plane())