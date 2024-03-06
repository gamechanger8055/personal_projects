'''
S- Single responsiblity principle.

Class should have a single reason to change. Like, a class should be doing one function instead of many.
When a class has multiple responsibilities, it becomes more difficult to maintain, test, and understand.
'''

# Voilation SRP

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def create_order(self, product):
        # Order processing logic here
        pass

    def update_customer_info(self, new_name, new_email):
        # Customer information update logic here
        pass

# Solution

class CustomerManager:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def update_customer_info(self, new_name, new_email):
        # Customer information update logic here
        pass

class OrderManager:
    def create_order(self, customer, product):
        # Order processing logic here
        pass

