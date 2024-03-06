"""
O- Open and closed pprinciple

Class should be open for extension but closed for modification.
A class which is live in production shall not be prone to changes in a new feature whereas the new feature
shall be added as a child class instead of interfering in base class.
"""

'''Problem-- In below if we need to add new shapes new if else statements needs to be added which makes it vague
'''

from abc import ABC, abstractmethod
class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        if self.name == "circle":
            self.draw_circle()
        elif self.name == "rectangle":
            self.draw_rectangle()

    def draw_circle(self):
        print("Drawing a circle")

    def draw_rectangle(self):
        print("Drawing a rectangle")

class Circle(Shape):
    def __init__(self):
        super().__init__("circle")

class Rectangle(Shape):
    def __init__(self):
        super().__init__("rectangle")

if __name__ == "__main__":
    circle = Circle()
    rectangle = Rectangle()

    circle.draw()
    rectangle.draw()

#Solution-- use abc to make multiple classes of different shapes and use them

#abstract base class
class DrawStrategy(ABC):
    @abstractmethod
    def draw(self):
        pass

#concrete classes
class CircleDrawStrategy(DrawStrategy):
    def draw(self):
        print("Drawing a circle new")

class SquareDrawStrategy(DrawStrategy):
    def draw(self):
        print("Drawing a square new")

class ElipseDrawStrategy(DrawStrategy):
    def draw(self):
        print("Drawing a elipse new")

# creating shape class that takes draw strategy

class Shape:
    def __init__(self,draw_strategy):
        self.draw_strategy=draw_strategy

    def draw(self):
        self.draw_strategy.draw()


circle=Shape(CircleDrawStrategy())
square=Shape(SquareDrawStrategy())
elipse=Shape(ElipseDrawStrategy())

circle.draw()
square.draw()
elipse.draw()

