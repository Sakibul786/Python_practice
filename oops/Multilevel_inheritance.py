class GrandFather:

    def land(self):
        print("Grandfather's land")


class Father(GrandFather):

    pass


class Son(Father):

    pass


s = Son()

s.land()