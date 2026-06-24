class Father:

    def house(self):
        print("House")


class Mother:

    def jewelry(self):
        print("Jewelry")


class Child(Father, Mother):

    pass


c = Child()

c.house()
c.jewelry()