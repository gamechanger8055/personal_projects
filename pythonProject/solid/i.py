"""
I - interface segregation principle

Interfaces should be such that client should not implement unnecessary details they dont need.
minimal base class which can be used by max sub classes.
The Interface Segregation Principle (ISP) is one of the SOLID principles and states that a class
should not be forced to implement interfaces it does not use.
In other words, classes should have specific, focused interfaces tailored to their needs.
"""

#Problem: Here engineers do not attend meetings then also they need to implement attend function

class Worker:
    def work(self):
        pass
    def attend_meetings(self):
        pass

class Manager(Worker):
    def work(self):
        pass
    def attend_meetings(self):
        pass

class Developer(Worker):
    def work(self):
        pass
    def attend_meetings(self):
        pass

#Solution: Now engineer need not need to implement attend function

class Workable:
    def work(self):
        pass

class AttendingMeetings:
    def attend_meetings(self):
        pass

class Manager(Workable,AttendingMeetings):
    def work(self):
        pass

    def attend_meetings(self):
        pass

class Developer(Workable):
    def work(self):
        pass

