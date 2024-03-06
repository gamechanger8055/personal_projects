"""
State pattern is a behavioural design pattern that allows an object to alter its behaviour when its state changes.
This pattern is particularly useful when an object can have multiple states, and the transitions between these states
 should be well-defined and managed.
"""

# Vending Machine

# State interface
class State:
    def insert_coin(self):
        pass

    def select_product(self):
        pass

    def dispense_product(self):
        pass

class NoMoneyState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin inserted")
        self.vending_machine.change_state(self.vending_machine.has_money_state)

    def select_product(self):
        print("Cannot select product before inserting coins")

    def dispense_product(self):
        print("Cannot dispense product before selection")

class HasMoneyState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin already inserted")

    def select_product(self):
        print("Product Selected")
        self.vending_machine.change_state(self.vending_machine.sold_state)

    def dispense_product(self):
        print("Cannot dispense product before selection")


class DispenseState(State):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self):
        print("Coin already inserted")

    def select_product(self):
        print("Product already Selected")

    def dispense_product(self):
        print("Product dispensed")
        self.vending_machine.change_state(self.vending_machine.no_money_state)

class VendingMachine:
    def __init__(self):
        self.has_money_state=HasMoneyState(self)
        self.sold_state=DispenseState(self)
        self.no_money_state=NoMoneyState(self)
        self.current_state=self.no_money_state

    def change_state(self,new_state):
        self.current_state=new_state

    def insert_coin(self):
        self.current_state.insert_coin()

    def select_product(self):
        self.current_state.select_product()

    def dispense_product(self):
        self.current_state.dispense_product()

machine = VendingMachine()
machine.insert_coin()
machine.select_product()
machine.dispense_product()

