class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting")

class Car(Vehicle):
    def wheels(self):
        print(f"{self.brand} car has 4 wheels")

class Bike(Vehicle):
    def wheels(self):
        print(f"{self.brand} bike has 2 wheels")

v = Vehicle("Generic")
c = Car("Toyota")
b = Bike("Honda")

v.start()
c.start()
c.wheels()
b.start()
b.wheels()
