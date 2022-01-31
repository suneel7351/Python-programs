class Vehicle:

    def __init__(self, name, maxSpeed, mileage):
        self.name = name
        self.maxSpeed = maxSpeed
        self.mileage = mileage


class Bus(Vehicle):
    def display(self):
        print("Name : ", self.name + "\n" +
              "Max-speed : ", str(self.maxSpeed) + "\n" + "Mileage : ", str(self.mileage))


class Car(Vehicle):
    def display(self):
        print("Name : ", self.name + "\n" +
              "Max-speed : ", str(self.maxSpeed) + "\n" + "Mileage : ", str(self.mileage))


class Truck(Vehicle):
    def display(self):
        print("Name : ", self.name + "\n" +
              "Max-speed : ", str(self.maxSpeed) + "\n" + "Mileage : ", str(self.mileage))


car = Car("Fortuner", 160, 17)
bus = Bus("ford", 110, 9)
truck = Truck("TATA", 120, 5)
car.display()
bus.display()
truck.display()
