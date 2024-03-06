'''
D - dependancy inversion principle

Child classes or other classes should depend on interfaces rather than concrete classes.
abstractions should not depend on details; details should depend on abstractions.
In essence, DIP promotes the decoupling of high-level and low-level modules through the use of abstractions.
'''

#Problem

class LightBulb:
    def turn_on(self):
        print("light bulb on")

    def turn_off(self):
        print("light bulb off")


class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        if self.bulb.is_on:
            self.bulb.turn_off()
        else:
            self.bulb.turn_on()




#Solution

from abc import ABC,abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def is_on(self):
        pass
# Step 2: Create a concrete class that implements the Switchable interface
class LightBulb(Switchable):
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on=True
        print("Light bulb is on")

    def turn_off(self):
        self.is_on=False
        print("Light bulb is off")

    def is_on(self):
        return self.is_on

# Step 3: Create a class that depends on the Switchable abstraction
class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()

bulb=LightBulb()
switch=Switch(bulb)
switch.operate()






