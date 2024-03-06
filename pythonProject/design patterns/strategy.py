""""
Strategy pattern is behavioural pattern that defines family of algorithms encapsulates each and make them
 interchangeable.
It allows you to choose an algorithm or strategy at runtime, independently of the context that uses the
 strategy.
"""

class PaymentStrategy:
    def pay(self,amount):
        pass

class CreditPay(PaymentStrategy):
    def pay(self,amount):
        print("Paid {} by credit card".format(amount))

class Paypal(PaymentStrategy):
    def pay(self,amount):
        print("Paid {} by paypal".format(amount))

class ShoppingCart:
    def __init__(self,payment_startegy):
        self.items=[]
        self.payment_strategy=payment_startegy

    def add_item(self, item):
        self.items.append(item)

    def checkout(self):
        total = sum(item['price'] for item in self.items)
        self.payment_strategy.pay(total)

credit_card_strategy = CreditPay()
paypal_strategy = Paypal()

# Create a shopping cart with a payment strategy
cart1 = ShoppingCart(credit_card_strategy)
cart2 = ShoppingCart(paypal_strategy)

# Add items to the shopping carts
cart1.add_item({"product": "Laptop", "price": 1000})
cart1.add_item({"product": "Mouse", "price": 20})
cart2.add_item({"product": "Book", "price": 50})

# Perform checkout with the chosen strategy
cart1.checkout()
cart2.checkout()
