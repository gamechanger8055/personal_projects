"""
Type: Structural Pattern

Use: It separates the abstraction from its implementation, allowing both to evolve independently.
 It's helpful when you want to avoid a permanent binding between an abstraction and its implementation,
 or when you have multiple platforms or variations of a feature.

 Example: A universal remote control that separates the abstraction (remote control) from its implementation (devices like TVs and stereos).
  This allows you to switch between different devices without changing the remote control.
"""

# TV remote

#abstraction
class RemoteControl:
    def __init__(self, device):
        self.device=device

    def power_on(self):
        self.device.power_on()

    def power_off(self):
        self.device.power_off()

#Implementor
class Device:
    def power_on(self):
        pass

    def power_off(self):
        pass

# Concrete Implementors
class TV(Device):
    def power_on(self):
        print("TV is powered on")

    def power_off(self):
        print("TV is powered off")

class Stereo(Device):
    def power_on(self):
        print("Stereo is powered on")

    def power_off(self):
        print("Stereo is powered off")

remote=RemoteControl(TV())
remote.power_on()
remote.power_off()