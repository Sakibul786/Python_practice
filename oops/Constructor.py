class Car:

    # Constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print(self.brand, self.model)


car1 = Car("Toyota", "Corolla")

car1.display()