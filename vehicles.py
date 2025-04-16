class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

class Bike(Vehicle):
    def move(self):
        return "Cycling 🚴"

# Demonstration of polymorphism
def travel(vehicle: Vehicle):
    print(vehicle.move())

if __name__ == "__main__":
    vehicles = [Car(), Plane(), Boat(), Bike()]
    for v in vehicles:
        travel(v)
