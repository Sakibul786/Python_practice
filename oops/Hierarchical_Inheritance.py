class Parent:

    def property(self):
        print("Property")


class Child1(Parent):

    pass


class Child2(Parent):

    pass


c1 = Child1()
c2 = Child2()

c1.property()
c2.property()