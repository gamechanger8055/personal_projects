"""
Type: Structural pattern
Intent: Attaches additional responsiblities to an object dynamically without altering its structure.
Use: Customizing a coffee order with add-ons like milk, sugar, and caramel.
    Each add-on is a decorator that modifies the cost of the base coffee without changing the underlying coffee object.
"""

# Component interface
class Coffee:
    def cost(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5

#Decorator
class CoffeeDecorator(Coffee):
    def __init__(self,coffee):
        self._coffee=coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

class CaramelDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 3

coffee = SimpleCoffee()
print(f"Cost: ${coffee.cost()}")

coffee_with_milk = MilkDecorator(coffee)
print(f"Cost: ${coffee_with_milk.cost()}")

coffee_with_sugar = SugarDecorator(coffee_with_milk)
print(f"Cost: ${coffee_with_sugar.cost()}")

coffee_with_caramel = CaramelDecorator(coffee_with_sugar)
print(f"Cost: ${coffee_with_caramel.cost()}")



