"""
Type: Behavioral Pattern

Intent: Encapsulates a request as an object, allowing parameterization of clients with queues, requests, and operations.
Example: A TV remote control where each button press represents a command (e.g., turn on, change channel, adjust volume).
This allows you to encapsulate and execute commands dynamically.
"""

#Command interface
class Command:
    def execute(self):
        pass

# Concrete Command classes
class TurnOnCommand(Command):
    def __init__(self,tv):
        self.tv=tv

    def execute(self):
        self.tv.turn_on()

class TurnOffCommand(Command):
    def __init__(self,tv):
        self.tv=tv

    def execute(self):
        self.tv.turn_off()

# Receiver
class TV:
    def turn_on(self):
        print("TV is turned on")

    def turn_off(self):
        print("TV is turned off")

#invoker
class RemoteControl:
    def __init__(self):
        self.command=None

    def set_command(self,command):
        self.command=command

    def execute(self):
        self.command.execute()

tv=TV()
turn_off=TurnOffCommand(tv)
turn_on=TurnOnCommand(tv)

rc=RemoteControl()
rc.set_command(turn_on)
rc.execute()
rc.set_command(turn_off)
rc.execute()


