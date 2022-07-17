# Create an abstract class called Vehicle that should have abstract methods drive and refuel. Cre
# ate 2 vehicles that inherit the Vehicle class (a Car and a Truck) and simulates driving and refueling them. 
# Car and Truck both receive fuel_quantity and fuel_consumption in liters per km upon initialization. 
# They both can be driven a given distance: drive(distance) and refueled with a given amount of fuel: refuel(fuel). It is summer, so both vehicles use 
# air conditioners, and their fuel consumption per km when driving is increased by 0.9 liters for the car and 1.6 liters for the truck. 
# Also, the Truck has a tiny hole in its tank, and when it is refueled, it keeps only 95% of the given fuel. The car has no problems and adds all the given fuel 
# to its tank. If a vehicle cannot travel the given distance, its fuel does not change.

from abc import ABC, abstractmethod


class Vehicles(ABC):
    AC_FUEL_CONSUMPTION = 0

    def __init__(self, fuel_quantity, fuel_consumption ):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass



class Car(Vehicles):
    AC_FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicles):
    AC_FUEL_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        fuel_needed = distance * (self.fuel_consumption + self.AC_FUEL_CONSUMPTION)
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * 0.95)

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
