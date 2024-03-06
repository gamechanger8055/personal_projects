"""
Factory pattern is a creational pattern that provides an interface for creating objects in a superclass but
allows subclasses to alter type of objects that will be created.
It promotes loose coupling between the client code and the created objects.
"""

#GUI library interface

from abc import ABC, abstractmethod

class UIElement(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete UI Element classes
class Button(UIElement):
    def draw(self):
        print("Draw a button")

class TextBox(UIElement):
    def draw(self):
        print("Draw a text box")

# Creator class with Factory Method
class UIElementFactory(ABC):
    @abstractmethod
    def create_element(self):
        pass

    def display_element(self):
        element=self.create_element()
        element.draw()

class ButtonFactory(UIElementFactory):
    def create_element(self):
        return Button()

class TextBoxFactory(UIElementFactory):
    def create_element(self):
        return TextBox()

button_factory = ButtonFactory()
button_factory.display_element()

textbox_factory = TextBoxFactory()
textbox_factory.display_element()

