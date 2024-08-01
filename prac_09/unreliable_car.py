from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """A UnreliableCar object"""
    def __init__(self, name, fuel, reliability):
        """construct a UnreliableCar object with name, fuel and reliability"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """drive the car"""
        random_number = randint(1, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = super().drive(0)
        return distance_driven
