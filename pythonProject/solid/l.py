"""
L- liksov substitution principle

A child class should have all properties of base class and we should not able to break properties of base while
implementing the child.
The base class should have minimal properties.

it states that objects of a superclass should be replaceable with objects of a subclass without affecting the
 correctness of the program.
if you have a base class and derived classes, you should be able to use any derived class in place of the
base class without breaking the program's behavior.
"""

#Problem
class Rectangle:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def set_width(self,width):
        self.width=width

    def set_height(self,height):
        self.height=height

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def set_width(self,width):
        self.side=width
        super().set_width(width)
        super().set_height(width)

    def set_height(self,height):
        self.side=height
        super().set_width(height)
        super().set_height(height)

# Solution

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.breadth*self.length

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2
