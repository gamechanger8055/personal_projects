"""
The Abstract Factory pattern is a creational design pattern that provides an interface for creating families
of related or dependent objects without specifying their concrete classes.
It's used when you need to ensure that the created objects work together harmoniously.
"""

from abc import ABC, abstractmethod

# Abstract Product interfaces
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class Tire(ABC):
    @abstractmethod
    def rotate(self):
        pass

class StandardEngine(Engine):
    def start(self):
        print("Normal engine start")

class SportsEngine(Engine):
    def start(self):
        print("Sports engine started")

class StandardTire(Tire):
    def rotate(self):
        print("Standard tire rotating")

class SportsTire(Tire):
    def rotate(self):
        print("Sports tire rotating")

class CarFactory(ABC):
    @abstractmethod
    def create_engine(self):
        pass

    @abstractmethod
    def create_tire(self):
        pass

class StandardCarFactory(CarFactory):
    def create_engine(self):
        return StandardEngine()
    def create_tire(self):
        return StandardTire()

class SportsCarFactory(CarFactory):
    def create_engine(self):
        return SportsEngine()
    def create_tire(self):
        return SportsTire()

#client code
def assemble_car(car_factory):
    engine=car_factory.create_engine()
    tire=car_factory.create_tire()
    engine.start()
    tire.rotate()

standard_car_factory = StandardCarFactory()
sports_car_factory = SportsCarFactory()

assemble_car(standard_car_factory)
assemble_car(sports_car_factory)